import matplotlib.pyplot as mpl
import agentframework
import csv
import os
import random

'''Set up directories for correct input + output file locations'''
main = os.getcwd()
print (main)
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)


'''Set up parameters'''
num_of_agents = 10
num_of_iterations = 1000
neighbourhood = 20
environment = []
agents = []


'''Set up environment'''
file = os.path.join(inputs, 'in.txt')
with open (file, newline='') as q0:
    dataset = csv.reader(q0, quoting=csv.QUOTE_NONNUMERIC)
    for row in dataset:
        rowlist = []
        for value in row:
            rowlist.append(float(value))
        environment.append(rowlist)

'''Make the agents'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))
#print("Test getting another agent from an agent.")
#print("agents[0].agents[1]", agents[0].agents[0]._x, agents[0].agents[0]._y)



'''Agent Actions'''
for j in range(num_of_iterations):
    print("iteration number: ", j)
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)



'''plot the agents + environment'''
mpl.xlim(0, 99)
mpl.ylim(0, 99)
mpl.imshow(environment)
for i in range(num_of_agents):
    mpl.scatter(agents[i]._x,agents[i]._y)
mpl.show()

'''Write to output output_env.csv file for environment data'''
file = os.path.join(outputs, 'output_env.csv')
with open(file, 'w', newline='') as q1:
    writer = csv.writer(q1, delimiter=' ')
    for row in environment:
        writer.writerow(row)
print("Environment data is located in " + file)

'''Append data for total stored to total_stored.txt'''
total = 0
for a in agents:
    total += a.store
file = os.path.join(outputs, 'total_stored.txt')
with open(file, "a") as q2:
    q2.write(str(total) + "\n")
    q2.flush
q2.close
print("Stored data is located in " + file)
