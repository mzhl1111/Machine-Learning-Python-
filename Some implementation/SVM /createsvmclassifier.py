"""
INPUT:	
xTr : dxn input vectors
yTr : 1xn input labels
alphas : dx1 vector of alphas generated from quadratic program solution of svm
bias : bias of classifier generated by recoverBias
ktype : type of kernel
kpar : parameter of kernel
compute

Output:
svmclassify : a classifier (svmclassify(xTe) defined in this function 
that returns the binary predictions on xTe)

Creates an svm classifierthat can make predictions on new test data
"""
import numpy as np
from computeK import computeK

def createsvmclassifier(xTr, yTr, alphas, bias, ktype, kpar):
	# classifier that returns all ones
	alphas = alphas.reshape((yTr.shape[0],1))
	def svmclassify(xTe):
		d,n = xTe.shape
	  
		fx = np.transpose(alphas* yTr) @ computeK(ktype,xTr, xTe, kpar)+bias
		pred = np.sign(fx).reshape(-1,1)

		return(pred)





	
	
	return svmclassify
	