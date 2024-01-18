import numpy

# my__1D_array = numpy.array([1, 2, 3, 4, 5])
# print(my__1D_array.shape)     #(5,) -> 1 row and 5 columns
#
# my__2D_array = numpy.array([[1, 2], [3, 4], [6, 5]])
# print(my__2D_array.shape)     #(3, 2) -> 3 rows and 2 columns
#
# print('hello world')
#
# change_array = numpy.array([1, 2, 3, 4, 5, 6])
# change_array.shape = (3, 2)
# print(change_array)
# print(numpy.reshape(numpy.array([1, 2, 3, 4, 5, 6]), (2, 3)))

str1 = "1 2 3 4 5 6 7 8 9"
arr = [int(i) for i in str1.split()]

print(arr)

result = numpy.array(arr)

print(numpy.reshape(result, (3, 3)))
