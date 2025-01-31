#Radhe Radhe 
import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv

freq=44100
duration=7

record=sd.rec(int(duration*freq), samplerate=freq,channels=2)
sd.wait()

write("recording0",freq,record) #scipy.io.wavfile

wv.write("recording1",record,freq,sampwidth=2)


