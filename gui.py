import tkinter, main, time

window = tkinter.Tk()
window.title('Evolutionary Computation Simulation')

canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()
cowsNum = tkinter.StringVar()
tkinter.Label(window, text='Number of Cows:').pack()
tkinter.Label(window, textvariable=cowsNum).pack()
def getColor(health):
    if health < 41:
        return 'red'
    elif health < 81:
        return 'orange'
    elif health < 121:
        return 'yellow'
    elif health < 161:
        return 'green'
    else: 
        return 'blue'

def drawCow(cow):
    '''draws cows on canvas'''
    drawnCow = canvas.create_rectangle(cow.location[0]*10, cow.location[1]*10, (cow.location[0]*10)-10, (cow.location[1]*10)+10, fill=getColor(cow.initialHealth))

    return drawnCow

#draw grid
for i in range(50):
    canvas.create_line(0, 10*i, 500, 10*i)
    canvas.create_line(10*i, 0, 10*i, 500)

#generate cows from main.py script
cows = main.startup()
#draw cows and create list of locations
drawnCows = {}
for cow in cows:
    drawnCow = drawCow(cow)
    drawnCows[cow.cowId] = drawnCow

#animate cows
for x in range(500):
    cowLocations = []
    cowsToRemove = []
    print('----')
    for i in range(len(cows)):
        print(cows[i].health)
        #move cows
        if cows[i].health > 0:
            cows[i].move()
        else:
            cowsToRemove.append(cows[i].cowId)
        #draw new location
        canvas.move(drawnCows[cows[i].cowId], cows[i].offset[0], cows[i].offset[1])
        canvas.itemconfig(drawnCows[cows[i].cowId], fill=getColor(cows[i].initialHealth))
        cowLocations.append(tuple(cows[i].location))
    
    #remove dead cows
    for cowId in cowsToRemove:
        for cow in cows:
            if cow.cowId == cowId:
                cows.remove(cow)

        del drawnCows[cowId]
            
            
    
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
            print(cowsToBreed)
            newCow = main.breed(cows, cows[cowsToBreed[0]], cows[cowsToBreed[1]])
            if newCow:
                cows.append(newCow)
                newDrawnCow = drawCow(newCow)
                drawnCows[newCow.cowId] = newDrawnCow

    #update number of cows
    cowsNum.set(len(cows))

    canvas.update()
    time.sleep(0.1)

window.mainloop()