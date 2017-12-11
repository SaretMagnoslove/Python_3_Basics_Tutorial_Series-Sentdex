# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline(file_name.write(\n))
# then append what you want. 

# text to append
appendMe = '\nFear is the little-death that brings total obliteration.'

# opening for appending then writing and closing the file
appendFile = open('litanyAginstFear.txt','a')
appendFile.write(appendMe)
appendFile.close()