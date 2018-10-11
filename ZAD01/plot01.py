# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 12:48:43 2018

@author: apasi
"""
#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
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
        out1.append(np.mean(run1[i,:])*100)

    for i in generation:
        out2.append(np.mean(run2[i,:])*100)

    for i in generation:
        out3.append(np.mean(run3[i,:])*100)

    for i in generation:
        out4.append(np.mean(run4[i,:])*100)

    for i in generation:
        out5.append(np.mean(run5[i,:])*100)
    
    # Fr bxpl daa
    data = [100*run1[199,:],100*run2[199,:],100*run3[199,:],100*run4[199,:],100*run5[199,:]]
    
    #plot for 3.0
    plt.plot(effort1, out1, color = 'blue', label = '2-Coev-RS')
    plt.plot(effort2, out2, color = 'red', label = '2-Coev')
    plt.plot(effort3, out3, color = 'green', label = '1-Coev-RS')
    plt.plot(effort4, out4, color = 'black', label = '1-Coev')
    plt.plot(effort5, out5, color = 'orange', label = '1-Evol-RS')
    plt.xlabel('Rozegranych gier')
    plt.ylabel('Odsetek wygranych gier')
    plt.legend()
    plt.savefig('132302_plot3.0.pdf')
    plt.show()

    #plot for 5.0
    boxprops = dict(color='blue')
    meanpointprops = dict(marker='o', markeredgecolor='black',
                          markerfacecolor='blue')
    whiskerprops = dict(color='blue')
    
    
    fig = plt.figure()
    ax1 = fig.add_subplot(121)


    ax1.plot(effort1/1000, out1, marker = '8', markevery = 20, color = 'blue', label = '2-Coev-RS', linewidth = 0.9)
    ax1.plot(effort2/1000, out2, marker = 'h', markevery = 20, color = 'red', label = '2-Coev', linewidth = 0.9)
    ax1.plot(effort3/1000, out3, marker = '^', markevery = 20, color = 'green', label = '1-Coev-RS', linewidth = 0.9)
    ax1.plot(effort4/1000, out4, marker = 'P', markevery = 20, color = 'black', label = '1-Coev', linewidth = 0.9)
    ax1.plot(effort5/1000, out5, marker = '*', markevery = 20, color = 'orange', label = '1-Evol-RS', linewidth = 0.9)
    ax1.set_xlim(0,500)
    ax1.set_xlabel('Rozegranych gier (x1000)')
    ax1.set_ylim(60,100)
    ax1.set_ylabel('Odsetek wygranych gier [%]')
    ax1.legend()
    ax1.grid()

    ax2 = ax1.twiny()
    ax2.set_xlabel('Pokolenie')
    ax2.set_xlim(0,500)
    ax2.set_xticks([0, 100, 200, 300, 400, 500])
    ax2.set_xticklabels(['0','40','80', '120', '160', '200'])
    
    ax3 = fig.add_subplot(122)
    ax3.boxplot(data, 1, labels = ['2-Coev-RS','2-Coev','1-Coev-RS','1-Coev','1-Evol-RS'],
                sym = 'b+', showmeans = 1, meanprops=meanpointprops, boxprops=boxprops, whiskerprops = whiskerprops)
    ax3.set_ylim(60,100)
    ax3.yaxis.tick_right()
    for tick in ax3.get_xticklabels():
        tick.set_rotation(35)
    ax3.grid()
    
    plt.savefig('132302_plot5.0.pdf')
    plt.show()
    
    
if __name__ == '__main__':
    main()