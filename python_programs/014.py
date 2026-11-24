#Hackerrank : Transpose and Flatten
#Difficulty : easy
Transpose = The transpose of a matrix is a new matrix formed by swapping its rows and columns. 
The element at position [i][j] in the original moves to position [j][i] in the result.
Flatten = Flattening converts a multi-dimensional array into a one-dimensional array by reading its elements row by row.

#Code
import numpy

n, m = map(int, input().split())

arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(arr))
print(arr.flatten())
