#Author: MD AL MAMUN
#Date: 10/ 03/ 2022
#Purpose: Pong game

# In this project, I am making a game where a ball will move left to right to left until it hit
# the boundary right_y of the vertical border. If the ball touch the paddle bar the ball game will be running, if
# the ball touches the vertical borders game will be ended.

from cs1lib import *
from random import uniform

#setting window size
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

#variables

right_x = 380 #right paddle initial x point
left_x = 0   #LEFT paddle initial x point
right_y = 320 #right paddle initial y point
left_y = 0 #left paddle initial x point
HEIGHT = 80 # paddle height
WIDTH = 20 #paddle width
PADDLE_MOVEMENT = 5 # paddle velocity
BALL_RADIUS = 10 # ball radius
bx = 200 # ball initial x point
by = 200 # ball initial y point
LEFT_UP = 'a' #key for left paddle moving up
LEFT_DOWN = 'z' #key for left paddle moving down
RIGHT_UP = 'k' #key for right paddle moving up
RIGHT_DOWN = 'm' #key for right paddle moving down

#velocity of the ball vertically and horizontally
vx = 2
vy = 1

#keypress initializing
kpress = False

#initializing paddle movement
left_paddle_up = False
left_paddle_down = False
right_paddle_up = False
right_paddle_down = False

# if the game is in play mode
playing = True


#function for reseting the game into their initial state
def gameReset():
    global bx, by, right_y, right_x, left_y, left_x
    bx = 200
    by = 200
    right_x = 380
    left_x = 0
    right_y = 320
    left_y = 0

#function for setting the boundary and collision state
#here function work for bounceback from the paddle and make the game reset if touches the verical wall
def collision(cx, cy):
    global playing, vx, vy
    if cx >= WINDOW_WIDTH - BALL_RADIUS:
        playing = False
    if cx <= WINDOW_WIDTH - WINDOW_WIDTH + BALL_RADIUS:
        playing = False
    if cy <= WINDOW_HEIGHT - WINDOW_HEIGHT + BALL_RADIUS:
        vy = - vy
    if cy >= WINDOW_HEIGHT - BALL_RADIUS:
        vy = -vy
    if (cx < WIDTH + BALL_RADIUS) and ((left_y - BALL_RADIUS) < cy < (left_y + HEIGHT + BALL_RADIUS)):
        vx = - vx
    if (cx > WINDOW_WIDTH - WIDTH - BALL_RADIUS) and (right_y - BALL_RADIUS) < cy < (right_y + HEIGHT + BALL_RADIUS
    ):
        vx = - vx

    #here my game will restart if touches the vertical wall. So that you won't need to
    # rerun the code to play again.
    if playing == False:
        gameReset()
        playing = True

#this function make ball movement vertically and horizontally
def ball_move():
    global bx, by
    bx = bx + vx
    by = by + vy


#function for creating the ball
def ball():
    global bx,by
    set_fill_color(1,0,0)
    #set_fill_color(uniform(0,1),uniform(0,1),uniform(0,1))
    draw_circle(bx,by,BALL_RADIUS)


#function for drawing the paddles
def drawBars():
    global left_x,right_x,left_y,right_y
    set_fill_color(0,0,0)
    draw_rectangle(left_x,left_y,WIDTH,HEIGHT)
    draw_rectangle(right_x,right_y,WIDTH,HEIGHT)

#function for the key works
def my_kpress(key):
    global kpress,left_paddle_up,left_paddle_down,right_paddle_up,right_paddle_down
    global bx,by, right_y,right_x,left_y,left_x
    kpress = True
    if key == LEFT_DOWN:
        left_paddle_down = True
    if key == LEFT_UP:
        left_paddle_up = True
    if key == RIGHT_UP:
        right_paddle_up = True
    if key == RIGHT_DOWN:
        right_paddle_down = True

    if key == 'q':
        cs1_quit()
    if key == ' ':
        gameReset()


#function for disabling the keys
def my_krelease(key):
    global kpress,left_paddle_up,left_paddle_down,right_paddle_up,right_paddle_down
    kpress = False
    if key == LEFT_DOWN:
        left_paddle_down = False
    if key == LEFT_UP:
        left_paddle_up = False
    if key == RIGHT_UP:
        right_paddle_up = False
    if key == RIGHT_DOWN:
        right_paddle_down = False

# function that moves the paddle up and down in a certain boundary
def paddleMove():
    global left_paddle_up, left_paddle_down, right_paddle_up, right_paddle_down
    global left_y, right_y, left_x, right_x,bx,by

    if left_paddle_down and left_y < WINDOW_HEIGHT - HEIGHT:
        left_y = left_y + PADDLE_MOVEMENT
    elif left_paddle_up and left_y > 0:
        left_y = left_y - PADDLE_MOVEMENT
    elif right_paddle_down and right_y < WINDOW_HEIGHT - HEIGHT:
        right_y = right_y + PADDLE_MOVEMENT
    elif right_paddle_up and right_y > 0:
        right_y = right_y - PADDLE_MOVEMENT


#main function
def myDraw():
    set_clear_color(0,1,1)
    clear()


    drawBars()
    ball()
    paddleMove()
    ball_move()
    collision(bx,by)

start_graphics(myDraw, key_press = my_kpress, key_release= my_krelease)
