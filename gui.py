import tkinter, main, time

window = tkinter.Tk()
window.title('Evolutionary Computation Simulation')

canvas = tkinter.Canvas(window, width=500, height=500)
canvas.pack()

#draw grid
for i in range(100):
    canvas.create_line(0, 10*i, 500, 10*i)
    canvas.create_line(10*i, 0, 10*i, 500)

canvas.create_rectangle(10, 10, 0, 20, fill='red')
#generate cows from main.py script
cows = main.startup()
#draw cows
drawnCows = []
for cow in cows:
    drawnCow = canvas.create_rectangle(cow.location[0]*10, cow.location[1]*10, (cow.location[0]*10)-10, (cow.location[1]*10)+10, fill='red')
    drawnCows.append(drawnCow)

#animate cows
for x in range(500):
    for i in range(len(cows)):
        cows[i].move()
        canvas.move(drawnCows[i], cows[i].offset[0], cows[i].offset[1])
        
    time.sleep(0.1)
    canvas.update()

window.mainloop()