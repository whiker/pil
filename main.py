#! /usr/bin/python

from numpy import *
import matplotlib.pyplot as plt
import Image


def PCA(X):
	(nRow,nCol) = X.shape;

	meanX = X.mean(axis=0);  # each column's mean
	X = X - meanX;

	if nCol > nRow:
		M = dot(X, X.T);
		e,E = linalg.eigh(M);
		tmp = dot(X.T, E).T;
		V = tmp[::-1];
		S = sqrt(e)[::-1];
		for i in xrange(V.shape[1]):
			V[:,i] /= S;
	else:
		U,S,V = linalg.svd(X);
		V = V[:nRow];

	return V,S,meanX;


if __name__ == '__main__':
	x = [[0,1],[1,0],[1,2],[2,1],[2,3],[3,2],[3,4],[4,3]];
	x = array(x);
	V,S,meanX = PCA(x);
	print V;
	print S;
	print meanX;