# Object Attributes
# SYNTAX -> object.attribute

from turtle import Screen,Turtle

# creating a Turtle object
timmy = Turtle()
print(timmy)

timmy.shape("turtle")
timmy.color("coral")
# shape and color are methods

# creating a Screen object
my_screen = Screen()

timmy.forward(100)
print(my_screen.canvheight)  # canvheight -> attribute inside class Screen

my_screen.exitonclick() # exitonclick -> method inside class Screen

