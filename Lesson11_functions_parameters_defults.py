# When using defaults, any parameters with defaults should be the last ones listed in the
# function's parameters.

# Something like:
def simple(num1, num2=5):
    pass
# This is just a simple definition of a function, 
# with num1 not being pre-defined (not given a default), 
# and num2 being given a default.
def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)
# Here, we can see that, if there is a function parameter default, 
# then, when we call that function, we do not need to define or even mention that 
# parameter at all!
basic_window(350,500,font='courier')