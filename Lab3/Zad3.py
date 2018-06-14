from pyx import *
import os
os.system("taskkill /f /im AcroRd32.exe")

unit.set(wscale=3)
c = canvas.canvas()
circle = path.circle(0,0,2)
c.stroke(circle, [style.linewidth.THICK, color.rgb.blue])

rect = path.rect(0.25,-2,2,1.75)
c.fill(rect,[color.rgb.white])
c.stroke(rect, [style.linewidth.THICK, color.rgb.white])

wave = path.curve(-1,-0.2,0,1.6,0.8,-1.6,1.7,0)
c.stroke(wave, [style.linewidth.THIck, color.cmyk.Orange])

line1 = path.line(-2.5,-3.8,-2.5,-2.8)
c.stroke(line1,[style.linewidth.THick, color.rgb.blue])

curve1 = path.curve(-2.5,-3.725,-2.2,-3.7,-2,-3.4,-2,-2.8)
c.stroke(curve1,[style.linewidth.THick, color.rgb.blue])

line2 = path.line(-2,-3.8,-2,-2.8)
c.stroke(line2,[style.linewidth.THick, color.rgb.blue])

curve2 = path.curve(-2,-3.725,-1.7,-3.7,-1.5,-3.4,-1.5,-2.8)
c.stroke(curve2,[style.linewidth.THick, color.rgb.blue])

circle2 = path.circle(0.5,-3.25,0.45)
c.stroke(circle2,[style.linewidth.THick, color.rgb.blue])

rect2 = path.rect(0.75,-3.55,0.05,0.05)
c.fill(rect2,[color.rgb.white])
c.stroke(rect2, [style.linewidth.THICK, color.rgb.white])

line3 = path.line(0.4,-3.25,1.027,-3.25)
c.stroke(line3,[style.linewidth.THick, color.rgb.blue])

line4 = path.line(1.25,-2.8,1.25,-3.75)
c.stroke(line4,[style.linewidth.THick, color.rgb.blue])

circle3 = path.circle(2,-3.25,0.45)
c.stroke(circle3,[style.linewidth.THick, color.rgb.blue])

rect3 = path.rect(2.25,-3.55,0.05,0.05)
c.fill(rect3,[color.rgb.white])
c.stroke(rect3, [style.linewidth.THICK, color.rgb.white])

line5 = path.line(2.45,-3.25,2.45,-3.7)
c.stroke(line5,[style.linewidth.THick, color.rgb.blue])

c.stroke(circle, [style.linewidth.THick, color.rgb.blue,trafo.scale(0.25),trafo.translate(-0.7,-3.2)])
c.fill(rect,[color.rgb.white,trafo.scale(0.25),trafo.translate(-0.7,-3.2)])
c.stroke(rect, [style.linewidth.THick, color.rgb.white, trafo.scale(0.25),trafo.translate(-0.7,-3.2)])
c.stroke(wave, [style.linewidth.Thick, color.cmyk.Orange, trafo.scale(0.25),trafo.translate(-0.7,-3.2)])

c.writePDFfile()
os.startfile("Zad3.pdf")
