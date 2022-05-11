import matplotlib.pyplot as mpl
import agentframework
import csv
import os
import random
import matplotlib.animation


'''Set up directories for correct input + output file locations'''
main = os.getcwd()
print (main)
inputs = os.path.join('.', 'input')
print ("Input files are located " + inputs)
outputs = os.path.join('.', 'output')
print ("Output files are located " + outputs)


'''Set up parameters'''
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []
carry_on = True
fig = mpl.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

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


'''Make agents act'''
def update(frame_number):
    global carry_on
    fig.clear()
    if (carry_on):
        random.shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        '''Stop processs if agents gain more than 50 in store'''
        half_full_agent_count = 0
        for i in range(num_of_agents):
            if (agents[i].store > 50):
                half_full_agent_count += 1
            if (half_full_agent_count == num_of_agents):
                carry_on = False


    '''plot environment'''
    mpl.xlim(0, 99)
    mpl.ylim(0, 99)
    mpl.imshow(environment)

    '''plot agents'''
    for i in range(num_of_agents):
        mpl.scatter(agents[i]._x,agents[i]._y, color = "black")


'''Define generator function + print reason for process ending'''
def gen_function(b = [0]):
    a = 0
    global carry_on
    while  (a < num_of_iterations) & (carry_on):
        yield a                     #: Returns control and waits next call.
        a = a + 1
    if not carry_on:
        print("Stopping..." + " storage capacity reached.")
    else:
        print("Max iterations met.")
    print("Number of iterations: ", a)




'''Animate agents'''
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
matplotlib.pyplot.show()

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
print("total ", total)
file = os.path.join(outputs, 'total_stored.txt')
with open(file, 'a') as q2:
    q2.write(str(total) + "\n")
    q2.flush
q2.close
print("Stored data is located in " + file)
