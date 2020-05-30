import speech_recognition as sr
import pyaudio
import _portaudio
import wave

## to use: input name of audio file in .wav format
def convert_audio():

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 15
    WAVE_OUTPUT_FILENAME = "groceries.wav"
    INPUT_DEVICE_INDEX = 0
 
    audio = pyaudio.PyAudio()
 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index= INPUT_DEVICE_INDEX,
                frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")
 
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
 
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    r = sr.Recognizer()

    with sr.AudioFile("groceries.wav") as source:
        r.adjust_for_ambient_noise(source)

        print("Converting Audio File... ")

        audio = r.listen(source)

        try:
            #print("Converted Audio is: " + r.recognize_google(audio))
            queryText = r.recognize_google(audio)
        except Exception as e:
            queryText = ""
            print(e)
    
    return queryText

