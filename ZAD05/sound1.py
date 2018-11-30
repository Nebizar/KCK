#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 100           # częstotliwość próbkowania [Hz]
T = 1  
f0 = 1          # rozważany okres [s]

n = T * w        # liczba próbek
t = linspace(0, T, n, endpoint=False) # punkty na osi OX [s]

"""f1 = lambda t : sin(2*pi*f0*t)    # def. funkcji
f2 = lambda t : 2 * sin(2*pi*f0*t)
f3 = lambda t : 3 * sin(2*pi*f0*t)
f4 = lambda t : 3 * sin(2*pi*f0*t)"""
f1 = lambda t : sin(40*2*pi*f0*t)    # def. funkcji
f2 = lambda t : sin(45*2*pi*f0*t)
f3 = lambda t : sin(55*2*pi*f0*t)
f4 = lambda t : sin(80*2*pi*f0*t)
signal1 = f1(t)
signal2 = f2(t)
signal3 = f3(t)
signal4 = f4(t)                 # funkcja spróbkowana

subplot(241)
plot(t, signal1, '*')
xlabel("test points")
ylabel("signal")

subplot(242)
plot(t, signal2, '*')
xlabel("test points")
#ylabel("signal")

subplot(243)
plot(t, signal3, '*')
xlabel("test points")
#ylabel("signal")

subplot(244)
plot(t, signal4, '*')
xlabel("test points")
#ylabel("signal")

signal01 = fft(signal1)      
signal01 = abs(signal01)        # moduł 

signal02 = fft(signal2)      
signal02 = abs(signal02)        # moduł 

signal03 = fft(signal3)      
signal03 = abs(signal03)        # moduł 

signal04 = fft(signal4)      
signal04 = abs(signal04) 

subplot(245)
freqs = linspace(0, w, n, endpoint=False)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal01/n*2, '-*')
xlabel("frequency [Hz]")
ylabel("amplitune")

subplot(246)
freqs = linspace(0, w, n, endpoint=False)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal02/n*2, '-*')
xlabel("frequency [Hz]")
#ylabel("amplitune")

subplot(247)
freqs = linspace(0, w, n, endpoint=False)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal03/n*2, '-*')
xlabel("frequency [Hz]")
#ylabel("amplitune")

subplot(248)
freqs = linspace(0, w, n, endpoint=False)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal04/n*2, '-*')
xlabel("frequency [Hz]")
#ylabel("amplitune")

show()


#SINGLE TEST
f = lambda t : sin(50*2*pi*f0*t)    # def. funkcji
signal = f(t)                 # funkcja spróbkowana

subplot(211)
plot(t, signal, '*')

signal1 = fft(signal)      
signal1 = abs(signal1)        # moduł 

subplot(212)
freqs = linspace(0, w, n, endpoint=False)              # <-- ZACZNIJ TUTAJ. Użyj linspace
stem(freqs, signal1, '-*')

show()