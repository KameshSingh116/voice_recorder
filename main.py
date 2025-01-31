#Radhe Radhe 
import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv

freq=44100
duration=int(input("Enter the duration of audio in seconds:"))

record=sd.rec(int(duration*freq), samplerate=freq,channels=2)

sd.wait()

# file_name1=input("Enter the filename:")
file_name=input("Enter the filename:")


# write(f"C:/Users/lenovo/Desktop/{file_name1}",freq,record) #scipy.io.wavfile

wv.write(f"C:/Users/lenovo/Desktop/{file_name}",record,freq,sampwidth=2) #using wavio


