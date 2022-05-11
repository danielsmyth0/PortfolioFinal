import random


class Agent():


    def __init__(self, environment, agents, x, y):
        self.environment = environment
        self.agents = agents
        self.store = 0
        if (x == None):
            self._x = random.randint(0,self.width)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,self.height)
        else:
            self._y = y



    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100

        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100

        if self.store > 40:
            if random.random() < 0.5:
                self._x = (self._x + 3) % 100
            else:
                self._x = (self._x - 3) % 100

            if random.random() < 0.5:
                self._y = (self._y + 3) % 100
            else:
                self._y = (self._y - 3) % 100


    def eat(self):
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

    def eat_hunger(self):
        if self.environment[self._y][self._x] > 10:
            if self.store <= 10:
                self.environment[self._y][self._x] -= 20
                self.store += 20


    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            if(self!=agent):
                dist = self.distance_between(agent)
                if dist <= neighbourhood:
                    Sum = self.store + agent.store
                    average = Sum /2
                    self.store = average
                    agent.store = average



    def distance_between(self, agent):
        return (((self._x - agent._x)**2) +
                ((self._y - agent._y)**2))**0.5
