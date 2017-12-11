# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readMe = open('litanyAginstFear.txt','r').read()
print('Reading all text:\n', readMe)
# this will instead read the file into a python list. 
readMe = open('litanyAginstFear.txt','r').readlines()
print('Reading into a list: ', readMe)