import matplotlib.pyplot
import agentframework

'''Define function to calculate distance between two agents'''
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._x - agents_row_b._x)**2) +
    ((agents_row_a._y - agents_row_b._y)**2))**0.5


'''Set up parameters'''
num_of_agents = 10
num_of_iterations = 100
agents = []

'''Make the agents'''
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

'''Move the agents'''
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

'''plot the agents'''
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()

'''call function to calculate distance between agents'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
