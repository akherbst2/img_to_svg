import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import skimage
from matplotlib import transforms

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


def main():
    plt.interactive(False)
    plt.figure(figsize=(12, 2))
    print('running')
    img = mpimg.imread('huhcat.jpg')
    img = skimage.filters.gaussian(img, 10)
    gray = rgb2gray(img)
    plt.imshow(gray, cmap=plt.get_cmap('gray'))
    plt.show()

    print('done')

if __name__ == '__main__':
    main()

