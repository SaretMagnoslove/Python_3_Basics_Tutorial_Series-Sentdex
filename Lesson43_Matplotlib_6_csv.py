from matplotlib import pyplot as plt 
from matplotlib import style
import numpy as np

style.use('ggplot')

# unpacking values from csv file into x and y
x,y = np.loadtxt('exampleFile.csv',
                  unpack = True,
                  delimiter = ',') # unpacking into numpy array

plt.plot(x,y) # same as before

plt.title('Example 4')
# adding labels 
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()