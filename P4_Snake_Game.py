from turtle import *
from random import randrange
import turtle
from freegames import vector,square
food=vector(0,0)
snake=[vector(10,0)]
aim=vector(0,-10)
turtle.title("Snake Game")
bgcolor('black')

def change(x,y):
    aim.x=x
    aim.y=y
    
def inside(head):
    bgcolor('white')
    return -300<head.x<290 and -300<head.y<290
     
def move():
    head=snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x,head.y,9,'darkred')
        style=('Courier',30,'italic')
        turtle.write("Game Over!",font=style,align='right')
        turtle.write("Click to Exit",20,align='left')

        update()
        exitonclick()
    snake.append(head)
    if head == food:
        print('snake',len(snake))
        food.x=randrange(-15,15)*10
        food.y=randrange(-15,15)*10
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x,body.y,9,'cyan')
    square(food.x,food.y,9,'red')
    update()
    ontimer(move,100)
hideturtle()
tracer(False)
listen()
onkey(lambda:change(10,0),'Right')
onkey(lambda:change(-10,0),'Left')
onkey(lambda:change(0,10),'Up')
onkey(lambda:change(0,-10),'Down')
move()
done()
     


