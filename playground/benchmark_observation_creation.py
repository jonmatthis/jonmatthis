"""
Benchmark: Per-frame observation object creation strategies.

Compares 4 approaches for storing per-frame tracking data:
1. Write into pre-allocated numpy array (no per-frame object)
2. Slotted dataclass (stores array references)
3. Numpy record array created per frame
4. Pydantic BaseModel

Each "observation" contains:
- frame_number: int
- body_xy: (33, 2) float64 array
- right_hand_xy: (21, 2) float64 array
- left_hand_xy: (21, 2) float64 array
- face_contour_xy: (127, 2) float64 array
- confidence: (202,) float64 array
"""

import dataclasses
import time
import statistics

import numpy as np


# ============================================================
# Pydantic substitute: simulates validation overhead
# Since we can't install pydantic in this environment, we
# replicate the overhead pattern: type checking, dict creation,
# field validation, __init__ with validators.
# Real Pydantic v2 is somewhat faster than v1 but still does
# schema validation, so this is a reasonable approximation.
# ============================================================
class FakePydanticBase:
    """
    Mimics Pydantic BaseModel overhead:
    - Validates types on construction
    - Creates internal __dict__ and __fields_set__
    - Runs per-field validation
    """
    __slots__ = ()  # subclasses define their own

    # noinspection PyUnusedLocal
    def __init_subclass__(cls, **kwargs: object) -> None:
        # Simulate model_rebuild / schema generation cost (one-time, not benchmarked)
        pass

    def __init__(self, **kwargs: object) -> None:
        # Simulate Pydantic's validated __init__:
        # 1. Check all fields present
        annotations = self.__class__.__annotations__
        for field_name, field_type in annotations.items():
            if field_name not in kwargs:
                raise ValueError(f"Missing field: {field_name}")
            value = kwargs[field_name]
            # 2. Type validation (Pydantic checks isinstance, coerces, etc.)
            if field_type is int:
                if not isinstance(value, (int, np.integer)):
                    raise TypeError(f"Expected int for {field_name}, got {type(value)}")
            elif field_type is np.ndarray:
                if not isinstance(value, np.ndarray):
                    raise TypeError(f"Expected ndarray for {field_name}, got {type(value)}")
            # 3. Store (Pydantic stores in __dict__ with additional metadata)
            object.__setattr__(self, field_name, value)

        # 4. Simulate __fields_set__ tracking
        object.__setattr__(self, "_fields_set", frozenset(kwargs.keys()))

    def __setattr__(self, name: str, value: object) -> None:
        # Pydantic models are quasi-immutable by default
        raise AttributeError("Cannot set attributes on validated model")

# ============================================================
# Constants matching mediapipe tracker dimensions
# ============================================================
NUM_BODY_POINTS: int = 33
NUM_HAND_POINTS: int = 21
NUM_FACE_CONTOUR_POINTS: int = 127
NUM_TOTAL_POINTS: int = NUM_BODY_POINTS + 2 * NUM_HAND_POINTS + NUM_FACE_CONTOUR_POINTS  # 202

FRAME_COUNTS: list[int] = [100, 1_000, 10_000, 50_000]
NUM_WARMUP_RUNS: int = 3
NUM_TIMED_RUNS: int = 5


# ============================================================
# Fake data generators (simulating what a detector would output)
# ============================================================
def generate_fake_frame_data() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    body_xy = np.random.rand(NUM_BODY_POINTS, 2).astype(np.float64)
    right_hand_xy = np.random.rand(NUM_HAND_POINTS, 2).astype(np.float64)
    left_hand_xy = np.random.rand(NUM_HAND_POINTS, 2).astype(np.float64)
    face_contour_xy = np.random.rand(NUM_FACE_CONTOUR_POINTS, 2).astype(np.float64)
    confidence = np.random.rand(NUM_TOTAL_POINTS).astype(np.float64)
    return body_xy, right_hand_xy, left_hand_xy, face_contour_xy, confidence


# ============================================================
# Approach 1: Pre-allocated numpy arrays
# ============================================================
class PreallocatedArrayRecorder:
    __slots__ = ("body_xy", "right_hand_xy", "left_hand_xy", "face_contour_xy", "confidence", "frame_count")

    def __init__(self, *, max_frames: int) -> None:
        self.body_xy: np.ndarray = np.empty((max_frames, NUM_BODY_POINTS, 2), dtype=np.float64)
        self.right_hand_xy: np.ndarray = np.empty((max_frames, NUM_HAND_POINTS, 2), dtype=np.float64)
        self.left_hand_xy: np.ndarray = np.empty((max_frames, NUM_HAND_POINTS, 2), dtype=np.float64)
        self.face_contour_xy: np.ndarray = np.empty((max_frames, NUM_FACE_CONTOUR_POINTS, 2), dtype=np.float64)
        self.confidence: np.ndarray = np.empty((max_frames, NUM_TOTAL_POINTS), dtype=np.float64)
        self.frame_count: int = 0

    def record(
        self,
        *,
        body_xy: np.ndarray,
        right_hand_xy: np.ndarray,
        left_hand_xy: np.ndarray,
        face_contour_xy: np.ndarray,
        confidence: np.ndarray,
    ) -> None:
        i = self.frame_count
        self.body_xy[i] = body_xy
        self.right_hand_xy[i] = right_hand_xy
        self.left_hand_xy[i] = left_hand_xy
        self.face_contour_xy[i] = face_contour_xy
        self.confidence[i] = confidence
        self.frame_count += 1


# ============================================================
# Approach 2: Slotted dataclass
# ============================================================
@dataclasses.dataclass(frozen=True, slots=True)
class DataclassObservation:
    frame_number: int
    body_xy: np.ndarray
    right_hand_xy: np.ndarray
    left_hand_xy: np.ndarray
    face_contour_xy: np.ndarray
    confidence: np.ndarray


# ============================================================
# Approach 3: Numpy record array per frame
# ============================================================
OBSERVATION_RECORD_DTYPE = np.dtype([
    ("frame_number", np.int64),
    ("body_xy", np.float64, (NUM_BODY_POINTS, 2)),
    ("right_hand_xy", np.float64, (NUM_HAND_POINTS, 2)),
    ("left_hand_xy", np.float64, (NUM_HAND_POINTS, 2)),
    ("face_contour_xy", np.float64, (NUM_FACE_CONTOUR_POINTS, 2)),
    ("confidence", np.float64, (NUM_TOTAL_POINTS,)),
])


def create_record_array_observation(
    *,
    frame_number: int,
    body_xy: np.ndarray,
    right_hand_xy: np.ndarray,
    left_hand_xy: np.ndarray,
    face_contour_xy: np.ndarray,
    confidence: np.ndarray,
) -> np.recarray:
    rec = np.recarray(shape=(1,), dtype=OBSERVATION_RECORD_DTYPE)
    rec[0].frame_number = frame_number
    rec[0].body_xy = body_xy
    rec[0].right_hand_xy = right_hand_xy
    rec[0].left_hand_xy = left_hand_xy
    rec[0].face_contour_xy = face_contour_xy
    rec[0].confidence = confidence
    return rec


# ============================================================
# Approach 4: Pydantic BaseModel
# ============================================================
class PydanticObservation(FakePydanticBase):
    __slots__ = ("frame_number", "body_xy", "right_hand_xy", "left_hand_xy", "face_contour_xy", "confidence", "_fields_set")
    frame_number: int
    body_xy: np.ndarray
    right_hand_xy: np.ndarray
    left_hand_xy: np.ndarray
    face_contour_xy: np.ndarray
    confidence: np.ndarray


# ============================================================
# Benchmark runners
# ============================================================
def bench_preallocated(num_frames: int, fake_data: list[tuple]) -> float:
    recorder = PreallocatedArrayRecorder(max_frames=num_frames)
    start = time.perf_counter_ns()
    for i in range(num_frames):
        body_xy, right_hand_xy, left_hand_xy, face_contour_xy, confidence = fake_data[i]
        recorder.record(
            body_xy=body_xy,
            right_hand_xy=right_hand_xy,
            left_hand_xy=left_hand_xy,
            face_contour_xy=face_contour_xy,
            confidence=confidence,
        )
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


def bench_dataclass(num_frames: int, fake_data: list[tuple]) -> float:
    observations: list[DataclassObservation] = []
    start = time.perf_counter_ns()
    for i in range(num_frames):
        body_xy, right_hand_xy, left_hand_xy, face_contour_xy, confidence = fake_data[i]
        obs = DataclassObservation(
            frame_number=i,
            body_xy=body_xy,
            right_hand_xy=right_hand_xy,
            left_hand_xy=left_hand_xy,
            face_contour_xy=face_contour_xy,
            confidence=confidence,
        )
        observations.append(obs)
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


def bench_record_array(num_frames: int, fake_data: list[tuple]) -> float:
    observations: list[np.recarray] = []
    start = time.perf_counter_ns()
    for i in range(num_frames):
        body_xy, right_hand_xy, left_hand_xy, face_contour_xy, confidence = fake_data[i]
        rec = create_record_array_observation(
            frame_number=i,
            body_xy=body_xy,
            right_hand_xy=right_hand_xy,
            left_hand_xy=left_hand_xy,
            face_contour_xy=face_contour_xy,
            confidence=confidence,
        )
        observations.append(rec)
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


def bench_pydantic(num_frames: int, fake_data: list[tuple]) -> float:
    observations: list[PydanticObservation] = []
    start = time.perf_counter_ns()
    for i in range(num_frames):
        body_xy, right_hand_xy, left_hand_xy, face_contour_xy, confidence = fake_data[i]
        obs = PydanticObservation(
            frame_number=i,
            body_xy=body_xy,
            right_hand_xy=right_hand_xy,
            left_hand_xy=left_hand_xy,
            face_contour_xy=face_contour_xy,
            confidence=confidence,
        )
        observations.append(obs)
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


# ============================================================
# Also benchmark: bulk read-back (simulating "get all data as array")
# ============================================================
def bench_readback_preallocated(num_frames: int, fake_data: list[tuple]) -> float:
    recorder = PreallocatedArrayRecorder(max_frames=num_frames)
    for i in range(num_frames):
        recorder.record(
            body_xy=fake_data[i][0],
            right_hand_xy=fake_data[i][1],
            left_hand_xy=fake_data[i][2],
            face_contour_xy=fake_data[i][3],
            confidence=fake_data[i][4],
        )
    start = time.perf_counter_ns()
    # Just slice — near zero cost
    _ = recorder.body_xy[:recorder.frame_count]
    _ = recorder.right_hand_xy[:recorder.frame_count]
    _ = recorder.left_hand_xy[:recorder.frame_count]
    _ = recorder.face_contour_xy[:recorder.frame_count]
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


def bench_readback_dataclass(num_frames: int, observations: list[DataclassObservation]) -> float:
    start = time.perf_counter_ns()
    _ = np.stack([obs.body_xy for obs in observations])
    _ = np.stack([obs.right_hand_xy for obs in observations])
    _ = np.stack([obs.left_hand_xy for obs in observations])
    _ = np.stack([obs.face_contour_xy for obs in observations])
    elapsed_ns = time.perf_counter_ns() - start
    return elapsed_ns


# ============================================================
# Reporting
# ============================================================
def format_time(ns: float) -> str:
    if ns < 1_000:
        return f"{ns:.0f} ns"
    elif ns < 1_000_000:
        return f"{ns / 1_000:.1f} μs"
    elif ns < 1_000_000_000:
        return f"{ns / 1_000_000:.2f} ms"
    else:
        return f"{ns / 1_000_000_000:.3f} s"


def run_benchmark(
    *,
    name: str,
    bench_fn: callable,
    num_frames: int,
    fake_data: list[tuple],
) -> dict[str, float]:
    # Warmup
    for _ in range(NUM_WARMUP_RUNS):
        bench_fn(num_frames, fake_data)

    # Timed runs
    times_ns: list[float] = []
    for _ in range(NUM_TIMED_RUNS):
        elapsed = bench_fn(num_frames, fake_data)
        times_ns.append(elapsed)

    median_ns = statistics.median(times_ns)
    per_frame_ns = median_ns / num_frames

    return {
        "name": name,
        "num_frames": num_frames,
        "median_total_ns": median_ns,
        "per_frame_ns": per_frame_ns,
        "min_ns": min(times_ns),
        "max_ns": max(times_ns),
    }


def print_results_table(results: list[dict[str, float]]) -> None:
    # Group by frame count
    frame_counts = sorted(set(r["num_frames"] for r in results))

    for fc in frame_counts:
        fc_results = [r for r in results if r["num_frames"] == fc]
        fc_results.sort(key=lambda r: r["per_frame_ns"])

        fastest_per_frame = fc_results[0]["per_frame_ns"]

        print(f"\n{'=' * 90}")
        print(f"  {fc:,} frames — CREATION benchmark")
        print(f"{'=' * 90}")
        print(f"  {'Approach':<30} {'Total (median)':<16} {'Per Frame':<14} {'Relative':<10}")
        print(f"  {'-' * 28}   {'-' * 14} {'-' * 12} {'-' * 8}")

        for r in fc_results:
            relative = r["per_frame_ns"] / fastest_per_frame
            print(
                f"  {r['name']:<30} "
                f"{format_time(r['median_total_ns']):<16} "
                f"{format_time(r['per_frame_ns']):<14} "
                f"{relative:>6.1f}x"
            )


def main() -> None:
    print("Observation Creation Benchmark")
    print(f"Dimensions: body={NUM_BODY_POINTS}x2, hand={NUM_HAND_POINTS}x2, face={NUM_FACE_CONTOUR_POINTS}x2, total_points={NUM_TOTAL_POINTS}")
    print(f"Warmup runs: {NUM_WARMUP_RUNS}, Timed runs: {NUM_TIMED_RUNS}")

    benchmarks: dict[str, callable] = {
        "1. Pre-allocated numpy": bench_preallocated,
        "2. Slotted dataclass": bench_dataclass,
        "3. Numpy record array": bench_record_array,
        "4. Pydantic-like validated": bench_pydantic,
    }

    all_results: list[dict[str, float]] = []

    for num_frames in FRAME_COUNTS:
        print(f"\nGenerating {num_frames:,} frames of fake data...")
        fake_data = [generate_fake_frame_data() for _ in range(num_frames)]

        for name, bench_fn in benchmarks.items():
            print(f"  Benchmarking: {name} @ {num_frames:,} frames...")
            result = run_benchmark(
                name=name,
                bench_fn=bench_fn,
                num_frames=num_frames,
                fake_data=fake_data,
            )
            all_results.append(result)

    print_results_table(all_results)

    # ============================================================
    # Readback benchmark (list-of-objects → stacked array vs pre-allocated slice)
    # ============================================================
    print(f"\n\n{'=' * 90}")
    print(f"  READBACK benchmark: converting stored data back to contiguous numpy arrays")
    print(f"{'=' * 90}")

    for num_frames in [1_000, 10_000, 50_000]:
        fake_data = [generate_fake_frame_data() for _ in range(num_frames)]

        # Build dataclass list
        dc_observations = [
            DataclassObservation(
                frame_number=i,
                body_xy=fake_data[i][0],
                right_hand_xy=fake_data[i][1],
                left_hand_xy=fake_data[i][2],
                face_contour_xy=fake_data[i][3],
                confidence=fake_data[i][4],
            )
            for i in range(num_frames)
        ]

        # Warmup + time preallocated readback
        for _ in range(NUM_WARMUP_RUNS):
            bench_readback_preallocated(num_frames, fake_data)
        prealloc_times = [bench_readback_preallocated(num_frames, fake_data) for _ in range(NUM_TIMED_RUNS)]
        prealloc_median = statistics.median(prealloc_times)

        # Warmup + time dataclass readback (np.stack)
        for _ in range(NUM_WARMUP_RUNS):
            bench_readback_dataclass(num_frames, dc_observations)
        dc_times = [bench_readback_dataclass(num_frames, dc_observations) for _ in range(NUM_TIMED_RUNS)]
        dc_median = statistics.median(dc_times)

        ratio = dc_median / max(prealloc_median, 1)

        print(f"\n  {num_frames:,} frames:")
        print(f"    Pre-allocated slice:      {format_time(prealloc_median):<16} ({format_time(prealloc_median / num_frames)} / frame)")
        print(f"    Dataclass → np.stack:     {format_time(dc_median):<16} ({format_time(dc_median / num_frames)} / frame)")
        print(f"    Ratio (stack/slice):       {ratio:.0f}x slower")


if __name__ == "__main__":
    main()
