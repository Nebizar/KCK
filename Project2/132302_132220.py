# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:24:33 2018

@author: Krzysztof Pasiewicz, Mikołaj Frankowski
"""
from pylab import *
from numpy import *
from scipy import *
import scipy.io.wavfile
from scipy import signal
from numpy import argmax
import sys



def genderRecog(data, w):
    #flatten signal for further processing
    if (len(data.shape) > 1):
        data = [s[0] for s in data]
    
    signalVar = []
    if w*3<len(data):
        for i in range(w, w*3):
            signalVar.append(data[i])
    else:
        signalVar=data
    #use fft    
    signalfft = fft(signalVar)
    signalfft = abs(signalfft)
    #only relevant freqs
    signalVar = []
    low=110
    high=3000
    freqs = range(low, high)
    for i in freqs:
        signalVar.append(signalfft[i])
    #decimate and multiply
    decimation = []
    wynik = signalVar.copy()
    decimation.append(signalVar)
    for i in range(1, 8):
        decimation.append(signal.decimate(signalVar, i))
        for j in range(len(decimation[i])):
            wynik[j] = wynik[j] * decimation[i][j]
    #get result
    if freqs[argmax(wynik)] > 320:
        return("K")
    else:
        return("M")
        
def main():
    w, data = scipy.io.wavfile.read(sys.argv[1])
    print(genderRecog(data, w))
    
if __name__ == "__main__":
    main()
