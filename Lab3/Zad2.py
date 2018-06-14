from pyx import *
import os
import numpy as np
os.system("taskkill /f /im AcroRd32.exe")

c = canvas.canvas()
startRED = (-1.5,0)
startBLUE = (-1.75,1)
startGREEN = (-2, 0)

for x in np.arange(5):
    if(x%2==0):
        redUP = path.path(path.moveto(startRED[0],startRED[1]), path.curveto(startRED[0]+0.5, 0, startRED[0]+0.5, 1, startRED[0]+1, startRED[1]+1))
        c.stroke(redUP, [color.rgb.red])
        startRED = (startRED[0]+1,startRED[1]+1)
        blueDOWN = path.path(path.moveto(startBLUE[0],startBLUE[1]), path.curveto(startBLUE[0]+0.5, 1, startBLUE[0]+0.5, 0, startBLUE[0]+1, startBLUE[1]-1))
        c.stroke(blueDOWN,[color.rgb.blue])
        startBLUE = (startBLUE[0]+1, startBLUE[1]-1)
        greenUP = path.path(path.moveto(startGREEN[0],startGREEN[1]), path.curveto(startGREEN[0]+0.5, 0, startGREEN[0]+0.5, 1, startGREEN[0]+1, startGREEN[1]+1))
        c.stroke(greenUP, [color.rgb.green])
        startGREEN = (startGREEN[0]+1,startGREEN[1]+1)
    else:
        greenDOWN = path.path(path.moveto(startGREEN[0],startGREEN[1]), path.curveto(startGREEN[0]+0.5, 1, startGREEN[0]+0.5, 0, startGREEN[0]+1, startGREEN[1]-1))
        c.stroke(greenDOWN, [color.rgb.green])
        startGREEN = (startGREEN[0]+1,startGREEN[1]-1)
        blueUP = path.path(path.moveto(startBLUE[0],startBLUE[1]), path.curveto(startBLUE[0]+0.5, 0, startBLUE[0]+0.5, 1, startBLUE[0]+1, startBLUE[1]+1))
        c.stroke(blueUP,[color.rgb.blue])
        startBLUE = (startBLUE[0]+1,startBLUE[1]+1)
        redDOWN = path.path(path.moveto(startRED[0],startRED[1]), path.curveto(startRED[0]+0.5, 1, startRED[0]+0.5, 0, startRED[0]+1, startRED[1]-1))
        c.stroke(redDOWN, [color.rgb.red])
        startRED = (startRED[0]+1,startRED[1]-1)
        
c.writePDFfile()
os.startfile("Zad2.pdf")
