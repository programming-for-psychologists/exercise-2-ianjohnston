import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
lastNames = [s.replace('\n', '') for s in lastNames]
bothNames = firstNames+lastNames

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
crossStim = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    crossStim.draw()
    win.flip()
    core.wait(.500)
    win.flip()
    nameShown = random.choice(bothNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    
    while True:
        response = event.waitKeys()
        if "f" in response and nameShown in firstNames:
            pass
        elif "l" in response and nameShown in lastNames:
            pass
        else:
            continue
        core.wait(.75)
        win.flip()
        core.wait(.15)
        break

    if event.getKeys(['q']):
        break

win.close()
