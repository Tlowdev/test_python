from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#create a D6 and D10
die1 = Die()
die2 = Die(10)

#make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_results = die1.num_sides + die2.num_sides
for value in range(2, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results
x_value = list(range(2, max_results+1))
data = [Bar(x = x_value, y = frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title = 'Results of rolling a D6 and D10 50_000 times',
    xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename= 'd6_d10.html')

print(frequencies)