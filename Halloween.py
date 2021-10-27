import turtle
tr = turtle.Turtle()
wn = turtle.Screen()
wn.bgpic("https://i.gifer.com/hDt.gif")
wn.mainloop()

import turtle as t

def run():
  t.penup()
  t.forward(20)
  t.left(50)
  t.backward(60)

def click(x,y):
  run()

if t.onclick(click):
  run()
 