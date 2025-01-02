import matplotlib.pyplot as plt
import numpy as np

#prepairing the string
string = "Data Science is Amazing"
string = string.replace(" ", "")
string = string.lower()

#count the number of each letter
dictLetters = {}
for l in string:
    if l in dictLetters:
        dictLetters[l] += 1
    else:
        dictLetters[l] = 1

#prepare data for plotting
letters = list(dictLetters.keys())
counts = list(dictLetters.values())

#plotting the data
fig, ax = plt.subplots()
ax.bar(letters, counts, width=0.9)

#adding title and labels
ax.set_title('Number of letters in string "Data Science is Amazing"')
ax.set_xlabel('Letters')
ax.set_ylabel('Counts')

#show the plot
plt.show()

xAxis = [1, 2, 3, 4, 5]
yAxis = [2, 4, 6, 8, 10]

#plotting the data
plt.plot(xAxis,yAxis)

#set title and labels
plt.title("Line chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#showing
plt.show()
