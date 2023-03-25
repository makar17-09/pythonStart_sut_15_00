import shape
shape.speed(0)


shape.beginfill("black")
shape.coords(-400, -300)
shape.square(800)
shape.endfill()


shape.coords(0,0)
shape.beginfill("red")
shape.right(60)
shape.forward(60)
shape.left(60)
shape.forward(60)
shape.right(140)
shape.forward(60)
shape.left(60)
shape.forward(60)
shape.right(140)
shape.forward(60)
shape.left(80)
shape.forward(60)
shape.right(140)
shape.forward(60)
shape.left(63)
shape.forward(60)
shape.right(143)
shape.forward(60)
shape.left(70)
shape.forward(60)
shape.left(20)
shape.endfill()

shape.beginfill("yellow")

shape.coords(0, 45)
shape.forward(90)

shape.endfill()

shape.beginfill("yellow")

shape.right(45)
shape.coords(60, 30)
shape.forward(90)

shape.endfill()

shape.beginfill("yellow")

shape.right(45)
shape.coords(60, -30)
shape.forward(90)

shape.endfill()

shape.beginfill("yellow")

shape.left(135)
shape.coords(-60, 30)
shape.forward(90)

shape.endfill()

shape.beginfill("yellow")

shape.left(45)
shape.coords(-60, -30)
shape.forward(90)

shape.endfill()


shape.done()
