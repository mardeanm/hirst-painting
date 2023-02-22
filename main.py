import colorgram
import turtle as turtle_module
from random import choice

# colors=colorgram.extract('imgc.jpg',10)
rgb = [(29, 20, 16), (218, 150, 87), (19, 33, 64), (32, 105, 165), (49, 18, 31), (138, 82, 60), (18, 47, 39), (169, 50, 79), (131, 30, 57), (49, 124, 67)]
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb.append(new_color)
#
# print(rgb)

tom = turtle_module.Turtle()
turtle_module.colormode(255)
tom.hideturtle()
tom.penup()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.speed(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots):
    tom.dot(20, choice(rgb))
    tom.forward((50))
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
