#! /usr/bin/python

from numpy import *
import matplotlib.pyplot as plt
import Image
import pca


if __name__ == '__main__':
	x = [[0,1],[1,0],[1,2],[2,1],[2,3],[3,2],[3,4],[4,3]];
	x = array(x);
	V,S,meanX = pca.PCA(x);
	print V;
	print S;
	print meanX;