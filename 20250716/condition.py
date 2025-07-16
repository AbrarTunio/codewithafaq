import turtle

scr = turtle.Screen()

pet = turtle.Turtle()
pet.shape('turtle')
pet.color('blue')

for x in range(5):
    pet.forward(100)
    
    print("The value in x:" , x)
    if x % 2 == 0:
        pet.left(90)
    else:
        pet.right(90)    



scr.exitonclick()