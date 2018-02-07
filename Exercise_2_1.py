import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
# r means open for reading (so we wont write to it)
#length of names will mathc number of names int he file
# the firstnames thing: initializes list, iterates over names, 
#and appends something to the list
split: will split things that are separated by the indicated separator,
here it's ' '.  This space character is known as a delimiter

need random module to get things to randomize
random.choice will expect a list as an argument

"""

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
crossStim = visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

while True:
    crossStim.draw()
    win.flip()
    core.wait(.500)
    win.flip()
    nameShown = random.choice(firstNames)
    firstNameStim.setText(nameShown)
    firstNameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)

    if event.getKeys(['q']):
        break

win.close()
    
"""
Create a fixation cross using a TextStim object visual.TextStim set text to"+" 
and color to "white". Make the fixation cross appear for 500 ms before each name and 
disappears right before the name comes up.
"""