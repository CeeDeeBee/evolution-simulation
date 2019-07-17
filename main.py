#A basic natural selection(?) simulation
import numpy as np
import random
directions = ['N', 'E', 'S', 'W']
class Entity:
    '''Basic entity class'''
    def __init__(self, health, location, direction):
        self.health = health
        self.location = location
        self.direction = direction
        self.offset = [0, 0]

    def move(self):
        #Roll to keep current direction or pick new one
        if random.uniform(0, 1) < 0.15:
            possDirections = list(directions)
            possDirections.remove(self.direction)
            newDirectionIndex = random.randint(0, 2)
            self.direction = possDirections[newDirectionIndex]
        #Change location
        if self.direction == 'N':
            if self.location[1] < 49:
                self.location[1] += 1
                self.offset = [0, 10]
            else:
                self.location[1] -= 1
                self.offset = [0, -10]
                self.direction = 'S'
        elif self.direction == 'E':
            if self.location[0] < 49:
                self.location[0] += 1
                self.offset = [10, 0]
            else:
                self.location[0] -=1
                self.offset = [-10, 0]
                self.direction = 'W'
        elif self.direction == 'S':
            if self.location[1] > 0:
                self.location[1] -= 1
                self.offset = [0, -10]
            else:
                self.location[1] += 1
                self.offset = [0, 10]
                self.direction = 'N'
        else:
            if self.location[0] > 0:
                self.location[0] -= 1
                self.offset = [-10, 0]
            else:
                self.location[0] += 1
                self.offset = [10, 0]
                self.direction = 'E'


def startup():
    '''Startup Function'''
    cows = []
    #Generate entities
    for n in range(10):
        randHealth = random.randint(1, 100)
        randLocation = []
        for n in range(2):
            randLocation.append(random.randint(1, 50))
        randDirection = directions[random.randint(0, 3)]
        cows.append(Entity(randHealth, randLocation, randDirection))

    return cows

if __name__ == '__main__':
    cows = startup()

    for cow in cows:
        print(cow.health, cow.location)

    cows[0].move()
    print(cows[0].location)