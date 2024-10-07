import pyaudio
import wave

def list_microphones():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    num_devices = info.get('deviceCount')
    
    print("Available microphone devices:")
    for i in range(num_devices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            print(f"Device {i}: {device_info.get('name')}")
    p.terminate()

def record_audio(device_index, duration=30, filename="output.wav"):
    p = pyaudio.PyAudio()
    
    # Set up the stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=1024)
    
    print("Recording...")
    frames = []
    
    for _ in range(0, int(44100 / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    
    print("Recording finished.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    list_microphones()
    
    # Choose the device index you want to use for recording
    device_index = int(input("Enter the device index you want to use for recording: "))
    
    # Record audio for 30 seconds and save it to a file
    record_audio(device_index, duration=30, filename="output.wav")