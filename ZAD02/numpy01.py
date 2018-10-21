# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:36:09 2018

@author: student
"""

import numpy as np
from matplotlib import pyplot as plt

matrix = np.array([[1, 3, 1, 2],[1, 2, 5, 8],[3, 1, 2, 9],[5, 4, 2, 1]])
matrix = matrix[1:3,0:3]
matrix2 = np.array([[2, 3, 1],[5, 1, 3]])
matrix2 = matrix2.T
res = matrix.dot(matrix2)

pi_grid = np.arange(-np.pi, np.pi+0.1, np.pi)
grid10 = np.linspace(-np.pi, np.pi, 10)
grid100 = np.linspace(-np.pi, np.pi, 100)


plt.subplot(1,3,1)
plt.plot(pi_grid, np.sin(pi_grid))
plt.title("krok PI")
#plt.show
plt.subplot(1,3,2)
plt.plot(grid10, np.sin(grid10))
plt.title("krok 10")
#plt.show
plt.subplot(1,3,3)
plt.plot(grid100, np.sin(grid100))
plt.title("krok 100")
plt.show