# importing the built in module statistics
import statistics
# creating a list of numbers to use in the examples below
example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
# calculating and printing the mean of the numbers in the above list
x = statistics.mean(example_list)
print('The mean is: ', x)
# calculating and printing the median of the numbers in the above list
y = statistics.median(example_list)
print('The median is: ', y)
# calculating and printing the mode of the numbers in the above list
z = statistics.mode(example_list)
print('The mode is: ', z)
# calculating and printing the standard deviation of the numbers in the above list
a = statistics.stdev(example_list)
print('The standard deviation is: ', a)
# calculating and printing the variance of the numbers in the above list
b = statistics.variance(example_list)
print('The variance is: ', b)