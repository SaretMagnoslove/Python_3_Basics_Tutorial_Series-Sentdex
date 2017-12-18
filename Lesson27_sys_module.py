import sys
# stderr and stdout
sys.stderr.write('this is a stderr text\n') # text will show in red error colour
sys.stderr.flush() # flushing the buffer
sys.stdout.write('this is a stdout text\n') # text will show in regular font (blue)
# # Mainly used to comunicte between Python and other language
print(sys.argv) # in the terminal prints a list of all the python arguments that were passed
if len(sys.argv) > 1: # checking if more than one agument was passed
    print(sys.arg[1]) # print the second argument on the argumants list
if len(sys.argv) > 1: # checking if more than one agument was passed
    print(float(sys.arg[1])/5) # manipulating arguments in the arguments list