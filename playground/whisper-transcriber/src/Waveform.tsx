import { useEffect, useRef } from "react";

interface WaveformProps {
  samples: Float32Array;
  isRecording: boolean;
}

const BAR_WIDTH = 3;
const BAR_GAP = 1;
const CANVAS_HEIGHT = 120;

export default function Waveform({ samples, isRecording }: WaveformProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const animFrameRef = useRef<number>(0);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    cancelAnimationFrame(animFrameRef.current);

    const draw = () => {
      const dpr = window.devicePixelRatio || 1;
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * dpr;
      canvas.height = CANVAS_HEIGHT * dpr;
      ctx.scale(dpr, dpr);

      const w = rect.width;
      const h = CANVAS_HEIGHT;

      // Background
      ctx.fillStyle = "#0a0a0f";
      ctx.fillRect(0, 0, w, h);

      // Draw center line
      ctx.strokeStyle = "rgba(120, 200, 255, 0.08)";
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(0, h / 2);
      ctx.lineTo(w, h / 2);
      ctx.stroke();

      if (samples.length === 0) {
        // Idle state: draw a flat line with a subtle glow
        ctx.strokeStyle = isRecording
          ? "rgba(255, 90, 90, 0.3)"
          : "rgba(120, 200, 255, 0.15)";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, h / 2);
        ctx.lineTo(w, h / 2);
        ctx.stroke();
        return;
      }

      const numBars = Math.floor(w / (BAR_WIDTH + BAR_GAP));
      const step = Math.max(1, Math.floor(samples.length / numBars));

      for (let i = 0; i < numBars; i++) {
        const idx = Math.min(i * step, samples.length - 1);
        const amplitude = Math.abs(samples[idx]);
        const barHeight = Math.max(2, amplitude * h * 0.9);

        // Color gradient from cyan to hot pink based on amplitude
        const t = Math.min(amplitude * 3, 1);
        const r = Math.round(80 + t * 175);
        const g = Math.round(200 - t * 140);
        const b = Math.round(255 - t * 55);

        const x = i * (BAR_WIDTH + BAR_GAP);
        const y = (h - barHeight) / 2;

        // Glow effect for louder bars
        if (amplitude > 0.15) {
          ctx.shadowColor = `rgba(${r}, ${g}, ${b}, 0.5)`;
          ctx.shadowBlur = 6;
        } else {
          ctx.shadowBlur = 0;
        }

        ctx.fillStyle = `rgb(${r}, ${g}, ${b})`;
        ctx.beginPath();
        ctx.roundRect(x, y, BAR_WIDTH, barHeight, 1.5);
        ctx.fill();
      }

      ctx.shadowBlur = 0;
    };

    draw();

    return () => {
      cancelAnimationFrame(animFrameRef.current);
    };
  }, [samples, isRecording]);

  return (
    <canvas
      ref={canvasRef}
      style={{
        width: "100%",
        height: `${CANVAS_HEIGHT}px`,
        borderRadius: "8px",
        display: "block",
      }}
    />
  );
}
