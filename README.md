# voice_recorder
A mini project to make voice recorder using python
...
import sounddevice as sd: Imports the sounddevice library and gives it the alias sd. This library is used to interact with your microphone and record audio.

from scipy.io.wavfile import write: Imports the write function from the scipy.io.wavfile module. This function is used to save audio data as a .wav file.

import wavio as wv: Imports the wavio library and gives it the alias wv. This library provides another way to save audio data as a .wav file.
...
...
freq: This is the sampling frequency (or sample rate) of the audio recording. It determines how many samples of audio are recorded per second.

44100: A common sampling frequency for audio recordings. It means 44,100 samples are recorded every second. This is the standard for CD-quality audio.
...
...
duration: This is the length of the recording in seconds.

7: The recording will last for 7 seconds.
...
...
sd.rec(): This function from the sounddevice library starts recording audio.

int(duration * freq): Calculates the total number of samples to record. Since duration is in seconds and freq is samples per second, multiplying them gives the total number of samples. The int() function ensures the result is an integer.

samplerate=freq: Specifies the sampling frequency (44,100 Hz in this case).

channels=2: Specifies the number of audio channels. 2 means stereo (left and right channels).

recording: This variable stores the recorded audio data as a NumPy array. Each element in the array represents an audio sample.
...
...
sd.wait(): This function blocks the program until the recording is complete. Since the recording duration is 7 seconds, the program will wait for 7 seconds before proceeding.
...
...
write(): This function from scipy.io.wavfile saves the recorded audio data as a .wav file.

"recording0.wav": The name of the output file.

freq: The sampling frequency (44,100 Hz).

recording: The NumPy array containing the audio data.
...
...
wv.write(): This function from the wavio library also saves the recorded audio data as a .wav file.

"recording1.wav": The name of the output file.

recording: The NumPy array containing the audio data.

freq: The sampling frequency (44,100 Hz).

sampwidth=2: Specifies the sample width (number of bytes per sample). 2 means 16-bit audio, which is standard for CD-quality audio.
...
...
..
..
.
.
