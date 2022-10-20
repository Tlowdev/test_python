import matplotlib.pyplot as plt
x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, cmap = plt.cm.Blues, s = 10)
#set charge title and label axes.
ax.set_title('Scatter', size = 24)
ax.set_xlabel('Value', size = 14)
ax.set_ylabel('Square values', size = 14)
#size of tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize = 14)
#set axis range for each axis
ax.axis([0, 1100, 0, 1_100_000])
plt.savefig('squares_plot.png', bbox_inches='tight')
