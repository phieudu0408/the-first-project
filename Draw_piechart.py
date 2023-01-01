import matplotlib.pyplot as pyplot
labels = ('Python', 'Java', 'Scala', 'C#')
sizes = [45, 30, 10, 15]
pyplot.pie(sizes,labels=labels,autopct='%1.f%%',counterclock=False,startangle=105) # Display the figure
pyplot.show()
