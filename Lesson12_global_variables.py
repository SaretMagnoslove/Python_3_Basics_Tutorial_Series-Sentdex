# this variable has no parent function, but is actually NOT a global variable.
# it just so happens that it is committed to memory before the function is called
# so we are able to iterate, or call it out, but we cannot do much else.

x = 6

def example():
    print(x)
    # z, however, is a local variable.  
    z = 5
    # this works
    print(z)
    
example()
# this does not, which often confuses people, because z has been defined
# and successfully even was called... the problem is that it is a local
# variable only, and you are attempting to access it globally.

print(z)

x = 6

def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    x+=6

    # so there we attempted to take the x var and add 6 to it... but now
    # we are told that we cannot, as we're referencing the variable before
    # its assignment.

# Here, again, we are able to reference x, we are even able to print x+6... 
# but we are not allowed to modify x.

# What if we'd like to modify x? Well, then we need to use global!
x = 6

def example3():
    # what we do here is defined x as a global variable. 
    global x
    # now we can:
    print(x)
    x+=5
    print(x)
# Now we're cooking! The problem here is that some people do not like the idea at all of 
# using global variables. How do we get around using them and referencing them locally?
x = 6

def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)
# We are able to do the above, by assigning the value that we can reference to a local
# variable, then doing what we want with it from there.

# Another choice you might have, as suggested by one of my viewers is the following:
x = 6
def example(x):
 
    print(x)
    x+=5
    print(x)
    return x
 
x = example(x)
print(x)
# In the above example, we have the function modifying x. 

# It may appear somewhat confusing since x is being used in multiple locations, 
# so maybe a more clear example is something like:
x = 6
def example(modify):
 
    print(modify)
    modify+=5
    print(modify)
    return modify
 
x = example(x)
print(x)