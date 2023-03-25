import shape
shape.speed(0)

#корпус
shape.beginfill("Light gray")
shape.coords(-40, -70)
shape.rect(100, 200)
shape.endfill()
#модуль
shape.beginfill("Gray")
shape.coords(-45,-80)
shape.rect(110, 40)
shape.endfill()
#окно
shape.beginfill("yellow")
shape.coords(10,15)
shape.circle(30)
shape.endfill()
#крыша
shape.coords(-60, 130)
shape.forward(145)
shape.left(150)
shape.forward(90)
shape.left(64)
shape.forward(85)
#огонь
shape.left(86)
shape.beginfill("yellow")
shape.coords(-25,-80)
shape.triangle(70)
shape.endfill()

shape.done()
