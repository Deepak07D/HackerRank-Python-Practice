#Hackerrank : Shape and Reshape
#Difficulty : easy
import numpy

arr = list(map(int, input().split()))

a = numpy.array(arr)
a.shape = (3, 3)

print(a)
