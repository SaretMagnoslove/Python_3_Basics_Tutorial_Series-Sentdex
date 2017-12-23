from matplotlib import pyplot as plt 
from matplotlib import style
style.use('ggplot')
# defining the x and y lists 
x = [5, 6, 7, 8]
y = [7, 3, 8, 3]
x2 = [5, 6, 7, 8]
y2 = [6, 7, 2, 6]
# plotting x and y lists
plt.plot(x, y, 'g', linewidth=5) # changing graph manualy (green thick line)
plt.plot(x2, y2, 'c', linewidth=10) # very thick line in cyan
# adding title
plt.title('Example 2')
# adding labels 
plt.ylabel('Y axis')
plt.xlabel('X axis')
# showing the graph
plt.show()
