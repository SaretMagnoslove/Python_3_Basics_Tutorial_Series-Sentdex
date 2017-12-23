from matplotlib import pyplot as plt 
from matplotlib import style
style.use('ggplot')

x = [2, 4, 6, 8]
y = [7, 3, 8, 3]
x2 = [1, 3, 5, 7]
y2 = [6, 7, 2, 6]

# plotting scatter
plt.scatter(x,y, color='c')
plt.scatter(x2,y2, color='g')
# plotting bar chart
plt.bar(x,y, color='c', align='center')
plt.bar(x2,y2, color='g', align='center')
# adding title
plt.title('Example 3')
# adding labels 
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()