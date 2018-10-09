# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:24:36 2018

@author: Krzysztof Pasiewicz
"""

#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read files as Data Frames
data1 = pd.read_csv('2cel-rs.csv')
data2 = pd.read_csv('2cel.csv')
data3 = pd.read_csv('cel-rs.csv')
data4 = pd.read_csv('cel.csv')
data5 = pd.read_csv('rsel.csv')

#Parse Data
generation =  data1.iloc[:,0].values

effort1 = data1.iloc[:,1].values
run1 = data1.iloc[:,2:34].values

effort2 = data2.iloc[:,1].values
run2 = data2.iloc[:,2:34].values

effort3 = data3.iloc[:,1].values
run3 = data3.iloc[:,2:34].values

effort4 = data4.iloc[:,1].values
run4 = data4.iloc[:,2:34].values

effort5 = data5.iloc[:,1].values
run5 = data5.iloc[:,2:34].values

#Delete Data Frames
del(data1)
del(data2)
del(data3)
del(data4)
del(data5)

#Create arrays for plotting
out1 = []
out2 = []
out3 = []
out4 = []
out5 = []

#Calculate mean for each effort
for i in generation:
    out1.append(np.mean(run1[i,:]))

for i in generation:
    out2.append(np.mean(run2[i,:]))

for i in generation:
    out3.append(np.mean(run3[i,:]))

for i in generation:
    out4.append(np.mean(run4[i,:]))

for i in generation:
    out5.append(np.mean(run5[i,:]))
    
#plot for 3.0
plt.plot(effort1, out1, color = 'blue', label = '2-Coev-RS')
plt.plot(effort2, out2, color = 'red', label = '2-Coev')
plt.plot(effort3, out3, color = 'green', label = '1-Coev-RS')
plt.plot(effort4, out4, color = 'black', label = '1-Coev')
plt.plot(effort5, out5, color = 'orange', label = '1-Evol-RS')
plt.xlabel('Rozegranych gier')
plt.ylabel('Odsetek wygranych gier')
plt.legend()
plt.show()

#plot for 5.0
plt.plot(effort1/1000, out1, color = 'blue', label = '2-Coev-RS')
plt.plot(effort2/1000, out2, color = 'red', label = '2-Coev')
plt.plot(effort3/1000, out3, color = 'green', label = '1-Coev-RS')
plt.plot(effort4/1000, out4, color = 'black', label = '1-Coev')
plt.plot(effort5/1000, out5, color = 'orange', label = '1-Evol-RS')
plt.xlabel('Rozegranych gier (x1000)')
plt.ylabel('Odsetek wygranych gier')
plt.legend()
plt.show()



