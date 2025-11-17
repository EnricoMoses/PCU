import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]

plt.plot(x,y,marker='o')
plt.title('Line Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()