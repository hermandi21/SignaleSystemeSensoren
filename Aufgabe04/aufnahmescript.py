import pyaudio
import numpy
import matplotlib.pyplot as plt
import time

FORMAT = pyaudio.paInt16
SAMPLEFREQ = 44100
FRAMESIZE = 1024
NOFFRAMES = 220
p = pyaudio.PyAudio()
for i in range(4,5):
    print("running " + str(i))
    stream = p.open(format=FORMAT,channels=1,rate=SAMPLEFREQ,
    input=True,frames_per_buffer=FRAMESIZE)
    data = stream.read(NOFFRAMES*FRAMESIZE)
    decoded = numpy.fromstring(data, dtype=int);
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("done")
    numpy.save("Z:/SSS/aufgabe4/andy/tief/" + str(i), decoded)
    plt.plot(decoded)
    plt.show()
