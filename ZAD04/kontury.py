# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:28:34 2018

@author: apasi
"""
from matplotlib import pyplot as plt
import numpy as np
from skimage import data, color, filters, io, feature, morphology 


def perform_image_computations(filteredImage,index):

    filteredImage = filters.sobel(filteredImage)
    filteredImage = filteredImage > filters.threshold_otsu(filteredImage)
    
    filteredImage = morphology.dilation(filteredImage)
    filteredImage = morphology.erosion(filteredImage)
    #filteredImage = morphology.erosion(filteredImage)
    
    subplot = plt.subplot(2, 3, index + 1)

    return filteredImage


if __name__ == "__main__":
    plt.figure(figsize=(20, 12))
    plt.subplots_adjust(left=0, bottom=0, top=1, right=1, hspace=0.25, wspace=0.10)

    for index, imageFilePath in enumerate(['samolot1.jpg','samolot2.jpg','samolot3.jpg','samolot4.jpg','samolot5.jpg','samolot6.jpg']):
        image = data.imread(imageFilePath,as_grey=True)
        image = perform_image_computations(image, index)
        plt.imshow(image, cmap="Greys_r")
        plt.axis("off")

    plt.savefig("samoloty.pdf", bbox_inches="tight")
