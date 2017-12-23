from matplotlib import pyplot as plt 
from matplotlib import style
style.use('ggplot')
# defining the x and y lists 
x = [5, 6, 7, 8]
y = [7, 3, 8, 3]
x2 = [5, 6, 7, 8]
y2 = [6, 7, 2, 6]
# plotting x and y lists
plt.plot(x, y, 'g', linewidth=5, label='line 1') # adding label
plt.plot(x2, y2, 'c', linewidth=10, label='line 2') # adding label
# adding title
plt.title('Example 3')
# adding labels 
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend() # showing the legend
plt.grid(True, color='g') # adding green grid lines
# showing the graph
plt.show()
