# Install a library
# pip install turtles

import turtle
window = turtle.Screen()

jarvis = turtle.Turtle()
jarvis.shape('turtle')
jarvis.color('green')

friday = turtle.Turtle()
friday.shape('turtle')
friday.color('red')

for x in range(50):
    jarvis.forward(100)
    jarvis.left(90+x)
    jarvis.forward(200)
    jarvis.left(90+x)
    friday.forward(100)
    friday.right(90+x)
    friday.forward(200)
    friday.right(90+x)


window.exitonclick()

#creating myfriend green turtle
# myfriend = turtle.Turtle()
# myfriend.shape("turtle")
# myfriend.color("green")
# #*********************
# #creating mycutie turtle blue
# mycutie = turtle.Turtle()
# mycutie.shape("turtle")
# mycutie.color("blue")


# tinyurl.com/mytestaj

# # myfriend.forward(200)
# # myfriend.left(90)
# # myfriend.penup()
# # myfriend.forward(200)
# # myfriend.left(90)

# # myfriend.pendown()
# # myfriend.forward(200)

# # c = 0
# # for c in range(0,50): 
# #     if c % 2 == 0:
# #         value = random.randrange(10,200)
# #         myfriend.forward(value)
# #         myfriend.left(90)
# #         myfriend.forward(value)
# #         # myfriend.color(c)
# #         myfriend.left(45)
# #         myfriend.color("red")
# #         myfriend.forward(value)
# #     if c % 2 != 0:
# #         value = random.randrange(10,200)
# #         mycutie.forward(value)
# #         mycutie.right(90)
# #         mycutie.forward(value)
# #         # mycutie.color(c)
# #         mycutie.right(45)
# #         mycutie.color("red")
# #         mycutie.forward(value)
        

# # myfriend.speed(1)
# # myfriend.forward(200)
# # myfriend.left(90)
# # myfriend.forward(200)
# # myfriend.left(90)
# # myfriend.forward(200)
# # myfriend.left(90)
# # myfriend.forward(200)
# # myfriend.left(45)
# # myfriend.forward(150)



# # mycutie.speed(2)
# # mycutie.backward(200)
# # mycutie.right(90)
# # mycutie.forward(100)
# # mycutie.left(90)
# # mycutie.forward(200)
# # mycutie.left(90)
# # mycutie.forward(100)
# # mycutie.left(45)
# # mycutie.forward(250)




