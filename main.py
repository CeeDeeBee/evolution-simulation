#A basic natural selection(?) simulation
import numpy as np
import random, uuid
directions = ['N', 'E', 'S', 'W']
class Entity:
    '''Basic entity class'''
    def __init__(self, health, location, direction, cowId):
        self.cowId = cowId
        self.health = health
        self.initialHealth = health
        self.location = location
        self.direction = direction
        self.canBreed = True
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
        #reduce health
        self.health -= 1


def startup():
    '''Startup Function'''
    cows = []
    #Generate entities
    for n in range(20):
        randHealth = random.randint(50, 200)
        randLocation = []
        for i in range(2):
            randLocation.append(random.randint(1, 50))
        randDirection = directions[random.randint(0, 3)]
        cows.append(Entity(randHealth, randLocation, randDirection, uuid.uuid1()))

    return cows

def breed(cows, cow1, cow2):
    '''Create new cow from two existing cows'''
    if cow1.canBreed and cow2.canBreed:
        health = round((cow1.initialHealth + cow2.initialHealth) / 2)
        location = [cow1.location[0] + 1, cow1.location[1]]
        randDirection = directions[random.randint(0, 3)]
        newCow = Entity(health, location, randDirection, uuid.uuid1())
        cow1.canBreed, cow2.canBreed = False, False

        return newCow
    else:
        cow1.canBreed, cow2.canBreed = True, True

        return False

if __name__ == '__main__':
    cows = startup()

    for cow in cows:
        print(cow.health, cow.location)

    cows[0].move()
    print(cows[0].location)