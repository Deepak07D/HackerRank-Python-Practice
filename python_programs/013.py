#Hackerrank : Shape and Reshape
#Difficulty : easy

Shape = The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
ReShape = The reshape tool gives a new shape to an array without changing its data. It creates a new array and does not modify the original array itself.

#code
import numpy

arr = list(map(int, input().split()))

#Shape
a = numpy.array(arr)
a.shape = (3, 3)
print(a)

#Reshape
b=numpy.array(arr)
print (numpy.reshape(b,(3,3)))

