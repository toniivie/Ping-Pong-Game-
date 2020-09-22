import turtle #insert drawing feature for computer graphics
import winsound #sound for windows application

win = turtle.Screen() #creating window for game
win.title = ("Ping Pong Game")#title for window
win.bgcolor("pink") #colour of window set to black
win.setup(width=800, height=600) #dimensions of window for Ping Pong game. Note origin is at centre of screen, so (0,0) is 1/2 the width at 400 and 1/2 the height 400. x axis lims are -400 --> 400, y axis lims are -300 --> 300 
win.tracer(0) #speeds game up, without game too slow

"""Main game structure (essentially includes loop for game to operate)"""

#Creating the side paddles for player1 and player2
#For player 1
pad1 = turtle.Turtle()
pad1.shape("square")
pad1.color("white")
pad1.speed(0)
pad1.shapesize(stretch_wid=5, stretch_len=1)
pad1.penup() #removes drawing lines in game caused by turtle module
pad1.goto(-350,0) #starting coord. for player1 paddle in form (x,y).

#For player 2
pad2 = turtle.Turtle()
pad2.shape("square")
pad2.color("white")
pad2.speed(0)
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.penup() 
pad2.goto(350,0)

#Moving paddles
def pad1_up():
    y = pad1.ycor()
    y +=20 
    pad1.sety(y)

def pad1_down():
    y = pad1.ycor()
    y -=20  
    pad1.sety(y)

def pad2_up():
    y = pad2.ycor()
    y +=20 
    pad2.sety(y)

def pad2_down():
    y = pad2.ycor()
    y -=20  
    pad2.sety(y)

win.listen()
win.onkeypress(pad1_up, "q")
win.onkeypress(pad1_down, "a") 
win.onkeypress(pad2_up, "Up")
win.onkeypress(pad2_down, "Down")

#For ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0) #starting coord. for player1 paddle in form (x,y).

ball.dx = 2
ball.dy = 2 #split ball movement into vertical and horizonatal components (dx,dy) --> small deviation in x and y as ball moves
#For score board need pen
pen = turtle.Turtle() #use turtle object to create pen for score board
pen.penup()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.goto(0,250)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "bold"))
score1 = 0 #intial score for player 1 and 2
score2 = 0


while True:
    win.update() #updates screen continuosly after loop run
    ball.setx(ball.xcor() + ball.dx) #using loop to iterate step of adding small deviation (horizantally) from starting point ar origin (0,0)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290: #setting boundaries for border
        ball.sety(290)
        ball.dy *=-1 #direction of ball
        winsound.PlaySound("wallHitSound.wav", winsound.SND_ASYNC) 
    if ball.ycor() < -290: #boundaries for boarders and ball
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("wallHitSound.wav", winsound.SND_ASYNC) 
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score1 +=1
        pen.undo()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("scoreSound.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score2 +=1
        pen.undo()
        pen.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("scoreSound.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() + -40):#collisons with paddles - for player one(to left of screen)
        ball.dx *=-1
        winsound.PlaySound("hitSound.wav", winsound.SND_ASYNC)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() + -40): #taking into consideration the diameter of ball, deduct radius from region the ball could possibly collide with paddle.
        ball.dx *=-1
        winsound.PlaySound("hitSound.wav", winsound.SND_ASYNC)
