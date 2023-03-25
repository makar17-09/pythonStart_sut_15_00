import shape
shape.speed(0)

shape.coords(-90,0)
shape.forward(180)
shape.left(45)
shape.forward(80)

shape.right(45)

shape.coords(-90, 0)
shape.left(135)
shape.forward(80)

shape.right(135)
shape.forward(300)

shape.left(90)
shape.coords(0,58)
shape.forward(120)

shape.right(90)

shape.right(135)
shape.forward(70)
shape.left(100)
shape.forward(65)

shape.coords(-80, 15)
shape.beginfill("black")
shape.circle(15)
shape.endfill()

shape.coords(-30, 15)
shape.beginfill("black")
shape.circle(15)
shape.endfill()

shape.coords(20, 15)
shape.beginfill("black")
shape.circle(15)
shape.endfill()

shape.coords(70, 15)
shape.beginfill("black")
shape.circle(15)
shape.endfill()

shape.left(35)
shape.coords(70,57)
shape.rect(80, 30)


shape.done()
