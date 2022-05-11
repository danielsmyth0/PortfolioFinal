import random


class Agent():

    '''definine __init__ function to create agents'''
    def __init__(self, environment, agents):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        print("x", self._x, "y", self._y)


    '''define move function to move agents'''
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10


    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if(self!=agent):
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    Sum = self.store + agent.store
                    average = Sum /2
                    self.store = average
                    agent.store = average



    '''Define function to calculate distance between two agents'''
    def distance_between(self, agent):
        return (((self._x - agent._x)**2) +
                ((self._y - agent._y)**2))**0.5
