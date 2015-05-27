#! /usr/bin/python

from numpy import *
import matplotlib.pyplot as plt
import Image
import pca
from scipy.ndimage import filters


if __name__ == '__main__':
	img = array(Image.open('img/lion_2.jpg').convert('L'));
	dst = zeros(img.shape);
	filters.gaussian_filter(img, (3,3), (0,1), dst);
	dstMin = dst.min();
	dstMax = dst.max();
	dst = (dst - dstMin) * 255 / (dstMax - dstMin);
	Image.fromarray(uint8(dst)).save('img/lion_2_1.jpg');