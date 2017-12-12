def example():
    return 15, 12

x, y = example()
print(x,y)

# in the above case, we have used a tuple and cannot modify it... and
# we definitely do not want to!

x = [1,3,5,6,2,1,6]

'''
You can then reference the whole list like:
'''
print(x)

# or a single element by giving its index value.
# index values start at 0 and go up by 1 each time

print(x[0],x[1])