# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello")
import turtle


wn=turtle.Screen()
wn.title("pong game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.goto(-350,0)

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.goto(350,0)

ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
#paddle_b.shapesize(stretch_wid=5,stretch_len=1)
ball.goto(0,0)
ball.dx=0.5
ball.dy=0.5


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,265)
pen.write("player A: 0  player B: 0",align="center",font=("courier",24,"normal"))

#last card
last=turtle.Turtle()
last.speed(0)
last.color("white")
last.penup()
last.hideturtle()
last.goto(0,0)
last.clear
#score
score_a=0
score_b=0
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")



while(True):
    
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        
    if ball.xcor()>360:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("player A: "+str(score_a)+" player B: "+str(score_b),align="center",font=("courier",24,"normal"))
    if ball.xcor()<-360:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("player A: "+str(score_a)+" player B: "+str(score_b),align="center",font=("courier",24,"normal"))
    #collision with paddles
    if ball.xcor()>340 and ball.ycor()<(paddle_b.ycor()+50) and ball.ycor()>(paddle_b.ycor()-50):
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and ball.ycor()<(paddle_a.ycor()+50) and ball.ycor()>(paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx*=-1
        
    if score_a==10:
        pen.clear()
        pen.write("player A wins",align="center",font=("courier",30,"normal"))
        pen.goto(0,0)
        flag=1
        en.exitonclick()
        
        #turtle.bye()
        break
    elif score_b==10:
        pen.clear()
        pen.goto(0,0)
        pen.write("player B wins",align="center",font=("courier",50,"normal"))
        
        flag=2
        wn.exitonclick()
        #turtle.bye()
        break
   
    
    
if flag==1:
    print("player A wins") 
    
else:
    print("player B wins")
    
    

    
   