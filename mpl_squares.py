import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize= (15,8))
ax.plot(input_values, squares, linewidth = 3)

#Set char title and label axes.
ax.set_title("Suare Numbers", fontsize = 24)
ax.set_xlabel("square of value", fontsize = 14)
ax.set_ylabel("value", fontsize = 14)
ax.tick_params(axis = 'both', labelsize = 12)

plt.show()