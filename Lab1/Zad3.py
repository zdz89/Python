import numpy

temp = [100, 80, 20, 35, 90, 101, 99]
temp2 = [0] + temp[0:len(temp)-1]

array = numpy.array(temp)
array2 = numpy.array(temp2)

result = array - array2

print(result)

