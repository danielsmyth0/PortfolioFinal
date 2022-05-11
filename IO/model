import matplotlib.pyplot as mpl
import agentframework
import csv
import os

'''Set up directories for correct input + output file locations'''
main = os.getcwd()
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)

'''Define function to calculate distance between two agents'''
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
    ((agents_row_a._y - agents_row_b._y)**2))**0.5

'''Set up parameters'''
num_of_agents = 10
num_of_iterations = 100
environment = []
agents = []

'''Set up environment'''
file = os.path.join(inputs, 'in.txt')
with open (file, newline='') as f:
    dataset = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)

'''Make the agents'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

'''Move the agents'''
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()

'''plot the agents + environment'''
mpl.xlim(0, 99)
mpl.ylim(0, 99)
mpl.imshow(environment)
for i in range(num_of_agents):
    mpl.scatter(agents[i]._x,agents[i]._y)
mpl.show()

'''Write to output output_env.csv file for environment data'''
file = os.path.join(outputs, 'output_env.csv')
with open(file, 'w', newline='') as f2:
    writer = csv.writer(f2, delimiter=' ')
    for row in environment:
        writer.writerow(row)
print("Environment data is located in " + file)

'''Append data for total stored to total_stored.txt'''
total = 0
for a in agents:
    total += a.store
file = os.path.join(outputs, 'total_stored.txt')
with open(file, "a") as f3:
    f3.write(str(total) + "\n")
    f3.flush
f3.close
print("Stored data is located in " + file)


'''call function to calculate distance between agents'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
