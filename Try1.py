import numpy as numpy
a=[0,1,4,2,3,5,2,4,3,5,5,3,5,5,4,1,2,5,5,3,4,4,4,4,5,5]
print('Mean= ',numpy.mean(a))
print('\nStandard Deviation= ',numpy.std(a))
print('\nVriance= ',numpy.var(a))
numpy.histogram(a)
print('\nCoefficient of Variance= ',numpy.std(a)/numpy.mean(a))
