from ctypes import *
import sys, enum, logging
from collections.abc import Callable
from contextlib import contextmanager
import numpy as np
from numpy import ctypeslib
import platform

__all__ = ["uvc_req_code", "UVCContext", "UVCDevice", "UVCDeviceDescriptor", "uvc_frame_format", "UVCFrame", "UVCControls"]

log = logging.getLogger(__name__)

class uvc_context_t(Structure): pass
p_uvc_context_t = POINTER(uvc_context_t)
class uvc_device_t(Structure): pass
p_uvc_device_t = POINTER(uvc_device_t)
class uvc_device_handle_t(Structure): pass
p_uvc_device_handle_t = POINTER(uvc_device_handle_t)

class uvc_req_code(enum.IntEnum):
    UVC_RC_UNDEFINED = 0x00
    UVC_SET_CUR = 0x01
    UVC_GET_CUR = 0x81
    UVC_GET_MIN = 0x82
    UVC_GET_MAX = 0x83
    UVC_GET_RES = 0x84
    UVC_GET_LEN = 0x85
    UVC_GET_INFO = 0x86
    UVC_GET_DEF = 0x87

class UVCError(Exception): pass

# Determine the correct library name based on the operating system
def get_libuvc_library_name():
    system = platform.system()
    if system == 'Windows':
        return "libuvc.dll"  # Windows library naming
    elif system == 'Darwin':
        return "libuvc.dylib"  # macOS library naming
    else:
        return "libuvc.so.0"  # Linux/Unix library naming

try:
    libuvc = cdll.LoadLibrary(get_libuvc_library_name())
except OSError as e:
    log.error(f"Failed to load libuvc library: {e}")
    log.error("Make sure libuvc is installed and in your system's library path.")
    if platform.system() == 'Windows':
        log.error("On Windows, ensure libuvc.dll is in your PATH or in the same directory as this script.")
    elif platform.system() == 'Darwin':
        log.error("On macOS, ensure libuvc is installed via homebrew or libuvc.dylib is in your library path.")
    else:
        log.error("On Linux, ensure libuvc is installed via your package manager or libuvc.so.0 is in your library path.")
    raise

uvc_strerror = libuvc.uvc_strerror
uvc_strerror.argtypes = [c_int]
uvc_strerror.restype = c_char_p
def raise_error(e):
    raise UVCError(f"{e}: {uvc_strerror(e).decode()}")

uvc_init = libuvc.uvc_init
uvc_init.argtypes = [POINTER(p_uvc_context_t), c_void_p]
uvc_init.restype = c_int
def init() -> p_uvc_context_t:
    ctx = p_uvc_context_t()
    res = uvc_init(byref(ctx), None)
    if res < 0: raise_error(res)
    return ctx
uvc_exit = libuvc.uvc_exit
uvc_exit.argtypes = [p_uvc_context_t]
uvc_exit.restype = None
def wrapped_exit(ctx: p_uvc_context_t): uvc_exit(ctx)

uvc_find_device = libuvc.uvc_find_device
uvc_find_device.argtypes = [p_uvc_context_t, POINTER(p_uvc_device_t), c_int, c_int, c_char_p]
uvc_find_device.restype = c_int
def find_device(ctx: p_uvc_context_t, vid: int = 0, pid: int = 0, serial: bytes | None = None) -> p_uvc_device_t:
    dev = p_uvc_device_t()
    res = uvc_find_device(ctx, byref(dev), vid, pid, serial)
    if res < 0: raise_error(res)
    return dev

"""
uvc_error_t uvc_get_device_list(
    uvc_context_t *ctx,
    uvc_device_t ***list);
void uvc_free_device_list(uvc_device_t **list, uint8_t unref_devices);
"""
pp_uvc_device_t = POINTER(p_uvc_device_t)
uvc_get_device_list = libuvc.uvc_get_device_list
uvc_get_device_list.argtypes = [p_uvc_context_t, POINTER(pp_uvc_device_t)]
uvc_get_device_list.restype = c_int
def get_device_list(ctx: p_uvc_context_t) -> pp_uvc_device_t:
    ret = pp_uvc_device_t()
    res = uvc_get_device_list(ctx, byref(ret))
    if res < 0: raise_error(res)
    return ret
uvc_free_device_list = libuvc.uvc_free_device_list
uvc_free_device_list.argtypes = [POINTER(p_uvc_device_t)]
uvc_free_device_list.restype = None
def free_device_list(lst: pp_uvc_device_t):
    uvc_free_device_list(lst)

"""
uint8_t uvc_get_bus_number(uvc_device_t *dev);
uint8_t uvc_get_device_address(uvc_device_t *dev);
"""
uvc_get_bus_number = libuvc.uvc_get_bus_number
uvc_get_bus_number.argtypes = [p_uvc_device_t]
uvc_get_bus_number.restype = c_uint8
def get_bus_number(dev: p_uvc_device_t) -> int: return uvc_get_bus_number(dev)
uvc_get_device_address = libuvc.uvc_get_device_address
uvc_get_device_address.argtypes = [p_uvc_device_t]
uvc_get_device_address.restype = c_uint8
def get_device_address(dev: p_uvc_device_t) -> int: return uvc_get_device_address(dev)

"""
uvc_error_t uvc_find_devices(
    uvc_context_t *ctx,
    uvc_device_t ***devs,
    int vid, int pid, const char *sn);
"""
uvc_find_devices = libuvc.uvc_find_devices
uvc_find_devices.argtypes = [p_uvc_context_t, POINTER(pp_uvc_device_t), c_int, c_int, c_char_p]
uvc_find_devices.restype = c_int
def find_devices(ctx: p_uvc_context_t, vid: int = 0, pid: int = 0, serial: bytes | None = None) -> pp_uvc_device_t:
    ret = pp_uvc_device_t()
    res = uvc_find_devices(ctx, byref(ret), vid, pid, serial)
    if res < 0: raise_error(res)
    return ret

class UVCDeviceList():
    def __init__(self, ctx: "UVCContext", lst: pp_uvc_device_t):
        self.ctx = ctx
        self.lst = lst
        self.len = 0
        #print(f"{lst=!r} {lst[0]=!r}"); print(f"{lst[0].contents=!r}"); print(f"{lst[1].contents=!r}")
        # https://stackoverflow.com/a/32386504 "NULL Pointers have a boolean False value"
        while lst[self.len]: self.len += 1
    
    def __len__(self) -> int: return self.len
    def __getitem__(self, key: int) -> "UVCDevice":
        assert isinstance(key, int)
        if key < 0: key = self.len - key
        assert key >= 0
        assert key < self.len
        return UVCDevice(self.ctx, self.lst[key], self)
    def __iter__(self):
        for i in range(self.len):
            yield self[i]
    
    def sorted(self) -> "list[UVCDevice]":
        l = list(self)
        l.sort(key=lambda a: a.getLocationString())
        return l
    
    def __del__(self): free_device_list(self.lst)

uvc_open = libuvc.uvc_open
uvc_open.argtypes = [p_uvc_device_t, POINTER(p_uvc_device_handle_t)]
uvc_open.restype = c_int
def wrapped_open(dev: p_uvc_device_t) -> p_uvc_device_handle_t:
    devh = p_uvc_device_handle_t()
    res = uvc_open(dev, byref(devh))
    if res < 0: raise_error(res)
    return devh
uvc_close = libuvc.uvc_close
uvc_close.argtypes = [p_uvc_device_handle_t]
uvc_close.restype = None
def close(devh: p_uvc_device_handle_t): uvc_close(devh)

"""
/** Structure representing a UVC device descriptor.
 *
 * (This isn't a standard structure.)
 */
typedef struct uvc_device_descriptor {
  /** Vendor ID */
  uint16_t idVendor;
  /** Product ID */
  uint16_t idProduct;
  /** UVC compliance level, e.g. 0x0100 (1.0), 0x0110 */
  uint16_t bcdUVC;
  /** Serial number (null if unavailable) */
  const char *serialNumber;
  /** Device-reported manufacturer name (or null) */
  const char *manufacturer;
  /** Device-reporter product name (or null) */
  const char *product;
} uvc_device_descriptor_t;
"""
class uvc_device_descriptor_t(Structure):
    _fields_ = \
    [   #/** Vendor ID */
        ("idVendor", c_uint16)
        #/** Product ID */
    ,   ("idProduct", c_uint16)
        #/** UVC compliance level, e.g. 0x0100 (1.0), 0x0110 */
    ,   ("bcdUVC", c_uint16)
        #/** Serial number (null if unavailable) */
    ,   ("serialNumber", c_char_p)
        #/** Device-reported manufacturer name (or null) */
    ,   ("manufacturer", c_char_p)
        #/** Device-reporter product name (or null) */
    ,   ("product", c_char_p)
    ]
p_uvc_device_descriptor_t = POINTER(uvc_device_descriptor_t)
uvc_get_device_descriptor = libuvc.uvc_get_device_descriptor
uvc_get_device_descriptor.argtypes = [p_uvc_device_t, POINTER(p_uvc_device_descriptor_t)]
uvc_get_device_descriptor.restype = c_int
def get_device_descriptor(dev) -> p_uvc_device_descriptor_t:
    desc = p_uvc_device_descriptor_t()
    res = uvc_get_device_descriptor(dev, byref(desc))
    if res < 0: raise_error(res)
    return desc
uvc_free_device_descriptor = libuvc.uvc_free_device_descriptor
uvc_free_device_descriptor.argtypes = [p_uvc_device_descriptor_t]
uvc_free_device_descriptor.restype = None

class UVCDeviceDescriptor():
    def __init__(self, desc: p_uvc_device_descriptor_t):
        self.desc = desc
    
    @property
    def struct(self) -> uvc_device_descriptor_t: return self.desc.contents
    @property
    def product(self) -> bytes | None: return self.struct.product
    @property
    def manufacturer(self) -> bytes | None: return self.struct.manufacturer
    @property
    def serialNumber(self) -> bytes | None: return self.struct.serialNumber
    
    def __del__(self): uvc_free_device_descriptor(self.desc)

uvc_set_sharpness = libuvc.uvc_set_sharpness
uvc_set_sharpness.argtypes = [p_uvc_device_handle_t, c_uint16]
uvc_set_sharpness.restype = c_int
def set_sharpness(devh: p_uvc_device_handle_t, val: int):
    res = uvc_set_sharpness(devh, val)
    if res < 0: raise_error(res)

uvc_get_saturation = libuvc.uvc_get_saturation
uvc_get_saturation.argtypes = [p_uvc_device_handle_t, POINTER(c_uint16), c_int]
uvc_get_saturation.restype = c_int
def get_saturation(devh: p_uvc_device_handle_t, req_code: uvc_req_code = uvc_req_code.UVC_GET_CUR) -> int:
    val = c_uint16()
    res = uvc_get_saturation(devh, byref(val), req_code)
    if res < 0: raise_error(res)
    return val.value

class UVCControls(enum.StrEnum):
    """supported controls from any of the libuvc *_ctrl_selector enums"""
    #processing unit
    BRIGHTNESS = "brightness" #UVC_PU_BRIGHTNESS_CONTROL
    CONTRAST = "contrast" #UVC_PU_CONTRAST_CONTROL
    GAIN = "gain" #UVC_PU_GAIN_CONTROL
    POWER_LINE_FREQUENCY = "power_line_frequency" #UVC_PU_POWER_LINE_FREQUENCY_CONTROL
    HUE = "hue" #UVC_PU_HUE_CONTROL
    SATURATION = "saturation" #UVC_PU_SATURATION_CONTROL
    SHARPNESS = "sharpness" #UVC_PU_SHARPNESS_CONTROL
    GAMMA = "gamma" #UVC_PU_GAMMA_CONTROL
    #camera terminal
    ZOOM = "zoom_abs" #UVC_CT_ZOOM_ABSOLUTE_CONTROL

CTRL_TYPES = \
{   UVCControls.BRIGHTNESS: c_uint16
,   UVCControls.CONTRAST: c_uint16
,   UVCControls.GAIN: c_uint16
,   UVCControls.POWER_LINE_FREQUENCY: c_uint8
,   UVCControls.HUE: c_uint16
,   UVCControls.SATURATION: c_uint16
,   UVCControls.SHARPNESS: c_uint16
,   UVCControls.GAMMA: c_uint16
,   UVCControls.ZOOM: c_uint16
}

def _get_control_getter(c, t):
    get_func = libuvc[f"uvc_get_{str(c)}"]
    get_func.argtypes = [p_uvc_device_handle_t, POINTER(t), c_int]
    get_func.restype = c_int
    def wrapped_getter(devh: p_uvc_device_handle_t, req_code: uvc_req_code = uvc_req_code.UVC_GET_CUR) -> int:
        val = t()
        res = get_func(devh, byref(val), req_code)
        if res < 0: raise_error(res)
        return val.value
    return wrapped_getter

def _get_control_setter(c, t):
    set_func = libuvc[f"uvc_set_{str(c)}"]
    set_func.argtypes = [p_uvc_device_handle_t, t]
    set_func.restype = c_int
    def wrapped_setter(devh: p_uvc_device_handle_t, val: int):
        res = set_func(devh, val)
        if res < 0: raise_error(res)
    return wrapped_setter

CTRLS = \
{ c:{   "getter": _get_control_getter(c, t)
    ,   "setter": _get_control_setter(c, t)
} for c, t in CTRL_TYPES.items()}

"""
/** A callback function to handle incoming assembled UVC frames
 * @ingroup streaming
 */
typedef void(uvc_frame_callback_t)(struct uvc_frame *frame, void *user_ptr);

/** Streaming mode, includes all information needed to select stream
 * @ingroup streaming
 */
typedef struct uvc_stream_ctrl {
  uint16_t bmHint;
  uint8_t bFormatIndex;
  uint8_t bFrameIndex;
  uint32_t dwFrameInterval;
  uint16_t wKeyFrameRate;
  uint16_t wPFrameRate;
  uint16_t wCompQuality;
  uint16_t wCompWindowSize;
  uint16_t wDelay;
  uint32_t dwMaxVideoFrameSize;
  uint32_t dwMaxPayloadTransferSize;
  uint32_t dwClockFrequency;
  uint8_t bmFramingInfo;
  uint8_t bPreferredVersion;
  uint8_t bMinVersion;
  uint8_t bMaxVersion;
  uint8_t bInterfaceNumber;
} uvc_stream_ctrl_t;
"""
class uvc_stream_ctrl_t(Structure):
    _fields_ = \
    [   ("bmHint", c_uint16)
    ,   ("bFormatIndex", c_uint8)
    ,   ("bFrameIndex", c_uint8)
    ,   ("dwFrameInterval", c_uint32)
    ,   ("wKeyFrameRate", c_uint16)
    ,   ("wPFrameRate", c_uint16)
    ,   ("wCompQuality", c_uint16)
    ,   ("wCompWindowSize", c_uint16)
    ,   ("wDelay", c_uint16)
    ,   ("dwMaxVideoFrameSize", c_uint32)
    ,   ("dwMaxPayloadTransferSize", c_uint32)
    ,   ("dwClockFrequency", c_uint32)
    ,   ("bmFramingInfo", c_uint8)
    ,   ("bPreferredVersion", c_uint8)
    ,   ("bMinVersion", c_uint8)
    ,   ("bMaxVersion", c_uint8)
    ,   ("bInterfaceNumber", c_uint8)
    ]
p_uvc_stream_ctrl_t = POINTER(uvc_stream_ctrl_t)

"""
/** Color coding of stream, transport-independent
 * @ingroup streaming
 */
enum uvc_frame_format {
  UVC_FRAME_FORMAT_UNKNOWN = 0,
  /** Any supported format */
  UVC_FRAME_FORMAT_ANY = 0,
  UVC_FRAME_FORMAT_UNCOMPRESSED,
  UVC_FRAME_FORMAT_COMPRESSED,
  /** YUYV/YUV2/YUV422: YUV encoding with one luminance value per pixel and
   * one UV (chrominance) pair for every two pixels.
   */
  UVC_FRAME_FORMAT_YUYV,
  UVC_FRAME_FORMAT_UYVY,
  /** 24-bit RGB */
  UVC_FRAME_FORMAT_RGB,
  UVC_FRAME_FORMAT_BGR,
  /** Motion-JPEG (or JPEG) encoded images */
  UVC_FRAME_FORMAT_MJPEG,
  UVC_FRAME_FORMAT_H264,
  /** Greyscale images */
  UVC_FRAME_FORMAT_GRAY8,
  UVC_FRAME_FORMAT_GRAY16,
  /* Raw colour mosaic images */
  UVC_FRAME_FORMAT_BY8,
  UVC_FRAME_FORMAT_BA81,
  UVC_FRAME_FORMAT_SGRBG8,
  UVC_FRAME_FORMAT_SGBRG8,
  UVC_FRAME_FORMAT_SRGGB8,
  UVC_FRAME_FORMAT_SBGGR8,
  /** YUV420: NV12 */
  UVC_FRAME_FORMAT_NV12,
  /** YUV: P010 */
  UVC_FRAME_FORMAT_P010,
  /** Number of formats understood */
  UVC_FRAME_FORMAT_COUNT,
};
"""
class uvc_frame_format(enum.IntEnum):
  UVC_FRAME_FORMAT_ANY = 0
  UVC_FRAME_FORMAT_UNCOMPRESSED = 1
  UVC_FRAME_FORMAT_COMPRESSED = 2
  UVC_FRAME_FORMAT_YUYV = 3
  UVC_FRAME_FORMAT_UYVY = 4
  UVC_FRAME_FORMAT_RGB = 5
  UVC_FRAME_FORMAT_BGR = 6
  UVC_FRAME_FORMAT_MJPEG = 7
  UVC_FRAME_FORMAT_H264 = 8
  UVC_FRAME_FORMAT_GRAY8 = 9
  UVC_FRAME_FORMAT_GRAY16 = 10
  UVC_FRAME_FORMAT_BY8 = 11
  UVC_FRAME_FORMAT_BA81 = 12
  UVC_FRAME_FORMAT_SGRBG8 = 13
  UVC_FRAME_FORMAT_SGBRG8 = 14
  UVC_FRAME_FORMAT_SRGGB8 = 15
  UVC_FRAME_FORMAT_SBGGR8 = 16
  UVC_FRAME_FORMAT_NV12 = 17
  UVC_FRAME_FORMAT_P010 = 18
  UVC_FRAME_FORMAT_COUNT = 19

"""
uvc_error_t uvc_get_stream_ctrl_format_size(
    uvc_device_handle_t *devh,
    uvc_stream_ctrl_t *ctrl,
    enum uvc_frame_format format,
    int width, int height,
    int fps
    );
"""
uvc_get_stream_ctrl_format_size = libuvc.uvc_get_stream_ctrl_format_size
uvc_get_stream_ctrl_format_size.argtypes = [p_uvc_device_handle_t, p_uvc_stream_ctrl_t, c_int, c_int, c_int, c_int]
uvc_get_stream_ctrl_format_size.restype = c_int
def get_stream_ctrl_format_size(devh: p_uvc_device_handle_t, format: uvc_frame_format = uvc_frame_format.UVC_FRAME_FORMAT_YUYV, width: int = 640, height: int = 480, fps: int = 57) -> uvc_stream_ctrl_t:
    ctrl = uvc_stream_ctrl_t()
    ret = uvc_get_stream_ctrl_format_size(devh, byref(ctrl), format, width, height, fps)
    if ret < 0: raise_error(ret)
    return ctrl

class UVCStreamControl():
    def __init__(self, devh: "UVCDeviceHandle", ctrl: uvc_stream_ctrl_t):
        self.devh = devh
        self.ctrl = ctrl
    
    def __repr__(self): return f"<UVCStreamControl {self.ctrl.wKeyFrameRate=!r} {self.ctrl.dwFrameInterval=!r} {10000000/self.ctrl.dwFrameInterval=!r}>"

"""
/** An image frame received from the UVC device
 * @ingroup streaming
 */
typedef struct uvc_frame {
  /** Image data for this frame */
  void *data;
  /** Size of image data buffer */
  size_t data_bytes;
  /** Width of image in pixels */
  uint32_t width;
  /** Height of image in pixels */
  uint32_t height;
  /** Pixel data format */
  enum uvc_frame_format frame_format;
  /** Number of bytes per horizontal line (undefined for compressed format) */
  size_t step;
  /** Frame number (may skip, but is strictly monotonically increasing) */
  uint32_t sequence;
  /** Estimate of system time when the device started capturing the image */
  struct timeval capture_time;
  /** Estimate of system time when the device finished receiving the image */
  struct timespec capture_time_finished;
  /** Handle on the device that produced the image.
   * @warning You must not call any uvc_* functions during a callback. */
  uvc_device_handle_t *source;
  /** Is the data buffer owned by the library?
   * If 1, the data buffer can be arbitrarily reallocated by frame conversion
   * functions.
   * If 0, the data buffer will not be reallocated or freed by the library.
   * Set this field to zero if you are supplying the buffer.
   */
  uint8_t library_owns_data;
  /** Metadata for this frame if available */
  void *metadata;
  /** Size of metadata buffer */
  size_t metadata_bytes;
} uvc_frame_t;
"""
class uvc_frame(Structure):
    # TODO: incomplete
    _fields_ = \
    [   # /** Image data for this frame */
        ("data", c_void_p)
        # /** Size of image data buffer */
    ,   ("data_bytes", c_size_t)
        # /** Width of image in pixels */
    ,   ("width", c_uint32)
        # /** Height of image in pixels */
    ,   ("height", c_uint32)
    ]
p_uvc_frame = POINTER(uvc_frame)

"""
void uvc_free_frame(uvc_frame_t *frame);
"""
uvc_free_frame = libuvc.uvc_free_frame
uvc_free_frame.argtypes = [p_uvc_frame]
uvc_free_frame.restype = None
def free_frame(frame: p_uvc_frame): uvc_free_frame(frame)

c_uint8_p = POINTER(c_uint8)

class UVCFrame():
    def __init__(self, frame: p_uvc_frame):
        self.frame = frame
    
    @property
    def struct(self) -> uvc_frame: return self.frame.contents
    @property
    def data(self) -> int: return self.struct.data
    @property
    def width(self) -> int: return self.struct.width
    @property
    def height(self) -> int: return self.struct.height
    @property
    def data_bytes(self) -> int: return self.struct.data_bytes
    
    def getByteArray(self):
        return ctypeslib.as_array(cast(self.data, c_uint8_p), (self.data_bytes,))

    def __repr__(self): return f"<UVCFrame {self.frame=!r} {self.width}x{self.height} ({self.data_bytes}B) {self.data=!r}>"

    #we dont own the frames from the callback
    #add a self.owned and free if its true if we make our own uvc_frames
    #def __del__(self): free_frame(self.frame)

"""
/** A callback function to handle incoming assembled UVC frames
 * @ingroup streaming
 */
typedef void(uvc_frame_callback_t)(struct uvc_frame *frame, void *user_ptr);
"""
uvc_frame_callback_t = CFUNCTYPE(None, p_uvc_frame, c_void_p) #p_uvc_frame_callback_t = POINTER(uvc_frame_callback_t)
"""
uvc_error_t uvc_start_streaming(
    uvc_device_handle_t *devh,
    uvc_stream_ctrl_t *ctrl,
    uvc_frame_callback_t *cb,
    void *user_ptr,
    uint8_t flags);
"""
uvc_start_streaming = libuvc.uvc_start_streaming
uvc_start_streaming.argtypes = [p_uvc_device_handle_t, p_uvc_stream_ctrl_t, uvc_frame_callback_t, c_void_p, c_uint8]
uvc_start_streaming.restype = c_int
def start_streaming(devh: p_uvc_device_handle_t, ctrl: p_uvc_stream_ctrl_t, cb: uvc_frame_callback_t, user_ptr: c_void_p = c_void_p(), flags: int = 0):
    ret = uvc_start_streaming(devh, ctrl, cb, user_ptr, flags)
    if ret < 0: raise_error(ret)
uvc_stop_streaming = libuvc.uvc_stop_streaming
uvc_stop_streaming.argtypes = [p_uvc_device_handle_t]
uvc_stop_streaming.restype = None
def stop_streaming(devh: p_uvc_device_handle_t): uvc_stop_streaming(devh)

_stdout = None
def _getstdout():
    global _libc, _stdout
    if _stdout is None:
        _libc = cdll.LoadLibrary("libc.so.6")
        _libc.fdopen.argtypes = [c_int, c_char_p]
        _libc.fdopen.restype = c_void_p
        _stdout = _libc.fdopen(sys.stdout.fileno(), b"w")
    assert _stdout
    return _stdout
uvc_print_diag = libuvc.uvc_print_diag
uvc_print_diag.argtypes = [c_void_p, c_void_p]
uvc_print_diag.restype = None
def print_diag(devh: uvc_device_handle_t): uvc_print_diag(devh, _getstdout())

class UVCDeviceHandle():
    def __init__(self, dev: "UVCDevice", devh: p_uvc_device_handle_t):
        self.dev = dev
        self.devh = devh
        self.ctrl: UVCStreamControl | None = None
        self.isOpen: bool = True
        self.isStreaming: bool = False
    
    def assertOpen(self):
        if not self.isOpen:
            raise ConnectionResetError("Device not open")
        if not self.dev.ctx.isOpen:
            raise SystemError("Context is no longer open")
    
    def printDiag(self): print_diag(self.devh)
    
    def setSharpness(self, val: int): set_sharpness(self.devh, val)
    def getSaturation(self) -> int: return get_saturation(self.devh)
    def getControl(self, ctrl: UVCControls) -> int:
        self.assertOpen()
        return CTRLS[ctrl]["getter"](self.devh)
    def setControl(self, ctrl: UVCControls, val: int):
        self.assertOpen()
        return CTRLS[ctrl]["setter"](self.devh, val)

    def getStreamControl(self, format: uvc_frame_format = uvc_frame_format.UVC_FRAME_FORMAT_YUYV, width: int = 640, height: int = 480, fps: int = 57):
        self.assertOpen()
        return UVCStreamControl(self, get_stream_ctrl_format_size(self.devh, format, width, height, fps))
    
    def startStreaming(self, ctrl: UVCStreamControl, cb: Callable[[UVCFrame], None]):
        self.assertOpen()
        self.ctrl = ctrl
        @uvc_frame_callback_t
        def streamingcallback(frame: p_uvc_frame, user_ptr: c_void_p):
            #print("Frame callback")
            cb(UVCFrame(frame))
        self.cb = streamingcallback
        start_streaming(self.devh, byref(ctrl.ctrl), streamingcallback)
        self.isStreaming = True
    
    def stopStreaming(self):
        stop_streaming(self.devh)
        self.isStreaming = False
    
    def close(self):
        if not self.dev.ctx.isOpen:
            log.debug("UVCDeviceHandle.close: Context is already dead, not proceeding to avoid a crash")
            return
        self.assertOpen()
        if self.isStreaming: self.stopStreaming()
        close(self.devh)
    
    def __repr__(self): return f"<UVCDeviceHandle of device {self.dev!r}>"
    
    def __del__(self):
        if self.isOpen: self.close()
    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.close()

class UVCDevice():
    def __init__(self, ctx: "UVCContext", dev: p_uvc_device_t, lst: UVCDeviceList | None = None):
        self.ctx = ctx
        self.dev = dev
        self.lst = lst
    
    def getDescriptor(self) -> UVCDeviceDescriptor:
        return UVCDeviceDescriptor(get_device_descriptor(self.dev))
    
    def open(self) -> UVCDeviceHandle:
        return UVCDeviceHandle(self, wrapped_open(self.dev))
    
    def getBusNumber(self) -> int: return get_bus_number(self.dev)
    def getAddress(self) -> int: return get_device_address(self.dev)
    def getLocationString(self) -> str: return f"{self.getBusNumber()}.{self.getAddress()}"
    
    def __repr__(self):
        desc = self.getDescriptor()
        product = desc.product
        if product is None: product = desc.manufacturer
        if product is None: product = b"Unknown"
        product = repr(product).lstrip("b")
        return f"<UVCDevice {product} at {self.getLocationString()}>"

    def __del__(self): pass # i'm just going to assume these are cleaned up when the context is free'd?
        #log.warning(f"TODO: implement UVCDevice cleanup")

class UVCContext():
    def __init__(self):
        self.ctx = init()
        self.isOpen: bool = True
    
    def findDevice(self, vid: int = 0, pid: int = 0, serial: bytes | None = None) -> UVCDevice: return UVCDevice(self, find_device(self.ctx, vid, pid, serial))
    def findDevices(self, vid: int = 0, pid: int = 0, serial: bytes | None = None) -> UVCDeviceList: return UVCDeviceList(self, find_devices(self.ctx, vid, pid, serial))
    def getDeviceList(self) -> UVCDeviceList: return UVCDeviceList(self, get_device_list(self.ctx))
    
    def close(self):
        assert self.isOpen, "Already closed"
        wrapped_exit(self.ctx)
        self.isOpen = False

    def __del__(self):
        if self.isOpen:
            log.warning("UVCContext: not closed before __del__")
            self.close()
    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.close()

if __name__ == "__main__":
    import argparse, time
    parser = argparse.ArgumentParser(description="Test utility for libuvc ctypes bindings")
    parser.add_argument("--faulthandler", action="store_true", help="Enable python faulthandler")
    parser.add_argument("--verbose", "-v", action="store_true", help="Output debug log messages")
    subparsers = parser.add_subparsers(dest="action", required=True)
    parser_test = subparsers.add_parser("test", help="test library functionality")
    parser_test.add_argument("--vid", type=int, default=0xf182)
    parser_test.add_argument("--pid", type=int, default=0x0003)
    parser_jpegview = subparsers.add_parser("view", help="view stream")
    parser_jpegview.add_argument("--vid", type=int, default=0xcce3)
    parser_jpegview.add_argument("--pid", type=int, default=0x3884)
    list_parser = subparsers.add_parser("list", help="list UVC devices")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    if args.faulthandler:
        import faulthandler
        faulthandler.enable()
    if args.action == "test":
        with UVCContext() as c: #c = UVCContext()
            d = c.findDevice(args.vid, args.pid)
            print(c, d)
            devh = d.open()
            devh.printDiag()
            print(f"{devh.getSaturation()}")
            sys.stdout.write("Read leap calibation")
            sys.stdout.flush()
            calbytes = []
            for i in range(100,256):
                devh.setControl(UVCControls.SHARPNESS, i)
                time.sleep(0.01)
                v = devh.getControl(UVCControls.SATURATION)
                calbytes.append(v)
                sys.stdout.write(".")
                sys.stdout.flush()
            sys.stdout.write("\nDone!\n")
            sys.stdout.flush()
            print(f"{bytearray(calbytes)}")
            ctrl = devh.getStreamControl()
            print(f"{ctrl=!r}")
            print("Start streaming...")
            devh.startStreaming(ctrl, lambda frame: print(f"{frame=!r}"))
            print("Streaming started?")
            time.sleep(1)
            devh.stopStreaming()

            print("Find all leaps:")
            l = c.findDevices(0xf182, 0x0003)
            count = len(l)
            print(f"Found {count} leap motion controller{'s' if count != 1 else ''}{':' if count > 0 else ''}")
            for ld in l: print(ld)
    elif args.action == "view":
        import cv2
        with UVCContext() as c:
            d = c.findDevice(args.vid, args.pid)
            devh = d.open()
            devh.printDiag()
            print(devh)
            ctrl = devh.getStreamControl(uvc_frame_format.UVC_FRAME_FORMAT_MJPEG, 1280, 720, 30)
            img = None
            def onFrame(frame: UVCFrame):
                global img
                img = cv2.imdecode(frame.getByteArray(), cv2.IMREAD_COLOR)
            devh.startStreaming(ctrl, onFrame)
            while not cv2.waitKey(10) == ord("q"):
                if img is not None:
                    cv2.imshow("mjpeg", img)
            devh.stopStreaming()
    elif args.action == "list":
        with UVCContext() as c:
            l = c.getDeviceList()
            print("UVC device list:")
            for dev in l:
                print(dev)
    else:
        raise KeyError(args.action)
    print("end")