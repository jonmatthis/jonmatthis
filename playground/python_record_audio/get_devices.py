import platform
import subprocess

def list_usb_devices_windows():
    command = 'powershell "Get-WmiObject Win32_PnPEntity | Where-Object { $_.DeviceID -like \'USB*\' } | Select-Object Name, DeviceID"'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def list_usb_devices_macos():
    command = 'system_profiler SPUSBDataType'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

def list_usb_devices_linux():
    command = 'lsusb'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    os_type = platform.system()
    if os_type == "Windows":
        list_usb_devices_windows()
    elif os_type == "Darwin":
        list_usb_devices_macos()
    elif os_type == "Linux":
        list_usb_devices_linux()
    else:
        print(f"Unsupported OS: {os_type}")
