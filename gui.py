import tkinter, main, time

window = tkinter.Tk()
window.title('Evolutionary Computation Simulation')

canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

def drawCow(cow):
    '''draws cows on canvas'''
    drawnCow = canvas.create_rectangle(cow.location[0]*10, cow.location[1]*10, (cow.location[0]*10)-10, (cow.location[1]*10)+10, fill='red')

    return drawnCow

#draw grid
for i in range(100):
    canvas.create_line(0, 10*i, 500, 10*i)
    canvas.create_line(10*i, 0, 10*i, 500)

#generate cows from main.py script
cows = main.startup()
#draw cows and create list of locations
drawnCows = []
for cow in cows:
    drawnCow = drawCow(cow)
    drawnCows.append(drawnCow)

#animate cows
for x in range(500):
    cowLocations = []
    #move cows
    for i in range(len(cows)):
        cows[i].move()
        #draw new location
        canvas.move(drawnCows[i], cows[i].offset[0], cows[i].offset[1])
        cowLocations.append(tuple(cows[i].location))
    
    #build dict of location occurances
    locationDict = {}
    for location in cowLocations:
        if location in locationDict:
            locationDict[location] += 1
        else:
            locationDict[location] = 1
            
    #check if there are two cows in same location and breed + draw if so
    for key, value in locationDict.items():
        if value > 1:
            cowsToBreed = [index for index, location in enumerate(cowLocations) if location == key]
            newCow = main.breed(cows, cows[cowsToBreed[0]], cows[cowsToBreed[1]])
            cows.append(newCow)
            newDrawnCow = drawCow(newCow)
            drawnCows.append(newDrawnCow)

    canvas.update()
    time.sleep(0.1)

window.mainloop()