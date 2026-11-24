#Hackerrank : array
#difficulty : easy

Numpy = The NumPy (Numeric Python) package helps us manipulate large arrays and matrices of numeric data.
Arrays = A NumPy array is a grid of values. They are similar to lists, except that every element of an array must be the same type.

#code
import numpy

def arrays(arr):
    a = numpy.array(arr, float)
    return a[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
