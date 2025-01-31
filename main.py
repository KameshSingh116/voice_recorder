#Radhe Radhe 
import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv

freq=44100
duration=7

record=sd.rec(int(duration*freq), samplerate=freq,channels=2)

sd.wait()

file_name1=input("Enter the filename:")
file_name2=input("Enter the filename:")


write(f"C:/Users/lenovo/Desktop/{file_name1}",freq,record) #scipy.io.wavfile

wv.write(f"C:/Users/lenovo/Desktop/{file_name2}",record,freq,sampwidth=2) #using wavio


