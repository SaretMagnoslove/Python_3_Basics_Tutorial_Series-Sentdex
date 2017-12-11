# The idea of function parameters in Python is to allow a programmer who is using
# that function, define variables dynamically within that function. 
# For example:
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(5,3)
# There is no limit to the amount of function parameters you have. 
# If you want to just specify the definitions of these parameters without saying the
#  parameter, like when we just said 5 and 3, instead of putting the parameter=5,
# then you must put them in the exact order. 
# If you have a lot of parameters where it might be difficult to remember their order, 
# you could do something like:
simple_addition(num2=3,num1=5)
# Finally, not only must they be in perfect order, but you must not specify too many
# or two few definitions.

# This will not work:
simple_addition(3,5,6)
# nor will this: 
simple_addition(3)