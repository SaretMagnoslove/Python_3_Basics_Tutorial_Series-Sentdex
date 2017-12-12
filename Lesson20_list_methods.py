# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)
# insterting in a specific place
x.insert(2,33)
print(x)
# removing by item value
x.remove(6)
print(x)
# refferencing by index from list begining
print(x[5])
# refferencing by index from list end
print(x.[-1])
# serching for an index of a specific value in the list
print(x.index(1))
# counting the number of occurances of a specific value in the list
print(x.count(1))
# sorting the list in acending order
x.sort()
print(x)
# sorting string values in list
y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort()
print(y)
# reversing the order of the sorted list
y.reverse()
print(y)

