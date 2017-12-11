# The next loop is the For loop.
# The idea of the for loop is to "iterate" through something. 
# For each thing in that something, it will do a block of code. 
# Most often, you will see a for loop's structure very much like this:
for eachThing in thisThing:
    do this stuff
    in this block
# This code will print out each item in that list. 
# Usually, people will choose to actually do something with the item in the list,
# more than just printing it out, but this is just a basic example
exampleList = [1,5,6,6,2,1,5,2,1,4]

for x in exampleList:
    print(x)
# This code is actually what is known as a generator function, and is highly efficient.
# The above works very much like the "counter" function we made with a while loop. 
# The only difference is this one is much faster and more efficient in many cases.
for x in range(1,11):
    print(x)