from pyx import *
import os

c = canvas.canvas()

circle = path.circle(0, 0, 2)
line = path.line(-1.5, 2, -1.5, -2)
c.stroke(circle, [style.linewidth.Thick])
c.stroke(line, [style.linewidth.thin])

isects_circle, isects_line = circle.intersect(line)
isectx, isecty = circle.at(isects_circle[0])
p=path.line(isectx,isecty,0,0)<<path.line(0,0,isectx,-isecty)

p.append(path.closepath())
c.fill(p,[color.gray(0.5)])
c.stroke(p)

c.writePDFfile()
os.startfile("Zad1.pdf")
