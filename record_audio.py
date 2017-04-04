import pyaudio
import wave


input_second = input("Enter the recording time : ")



RECORDING_LENGTH_SECONDS = input_second
FORMAT = pyaudio.paInt16
CHUNK = 1024
CHANNELS = 2
RATE = 44100  


WAVE_OUTPUT_FILENAME = "record.wav"

obj = pyaudio.PyAudio()

stream = obj.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("--> recording")

array_frames = []

for i in range(0, int(RATE / CHUNK * RECORDING_LENGTH_SECONDS)):
    data = stream.read(CHUNK)
    array_frames.append(data)

print("--> done")

stream.stop_stream()
stream.close()
obj.terminate()

wfile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wfile.setnchannels(CHANNELS)
wfile.setsampwidth(obj.get_sample_size(FORMAT))
wfile.setframerate(RATE)
wfile.writeframes(b''.join(array_frames))
wfile.close()

#A new wave file will be created named record.wav in your python folder 
