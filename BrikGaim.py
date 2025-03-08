import turtle
import random
import time


# Set up the screen
screen = turtle.Screen()
screen.title("Brick Breaker")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)


# Score display
score = 0
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))


# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, -200)
ball.dx = 5
ball.dy = 5


# Bricks
bricks = []
rows = 5
cols = 7
brick_colors = ["red", "orange", "yellow", "green", "blue"]


for row in range(rows):
   for col in range(cols):
       brick = turtle.Turtle()
       brick.shape("square")
       brick.color(brick_colors[row])
       brick.shapesize(stretch_wid=1, stretch_len=2)
       brick.penup()
       x = -200 + (col * 60)
       y = 200 - (row * 30)
       brick.goto(x, y)
       bricks.append(brick)


# Paddle movement
def move_left():
   x = paddle.xcor()
   if x > -250:
       paddle.setx(x - 50)


def move_right():
   x = paddle.xcor()
   if x < 250:
       paddle.setx(x + 50)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")


# Update score
def update_score():
   global score
   score += 10
   score_display.clear()
   score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))


# Reset game
def reset_game():
   global score, game_over, bricks
   score = 0
   score_display.clear()
   score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))
  
   # Reset ball and paddle
   paddle.goto(0, -250)
   ball.goto(0, -200)
   ball.dx = 3
   ball.dy = 3
  
   # Reset bricks
   for brick in bricks:
       brick.goto(1000, 1000)  # Move old bricks off-screen
   bricks.clear()


   for row in range(rows):
       for col in range(cols):
           brick = turtle.Turtle()
           brick.shape("square")
           brick.color(brick_colors[row])
           brick.shapesize(stretch_wid=1, stretch_len=2)
           brick.penup()
           x = -200 + (col * 60)
           y = 200 - (row * 30)
           brick.goto(x, y)
           bricks.append(brick)
  
   game_over = False
   game_loop()


# Quit game
def quit_game():
   screen.bye()


# Listen for replay and quit commands
screen.onkeypress(reset_game, "r")
screen.onkeypress(quit_game, "q")


# Game loop
def game_loop():
   global game_over
   game_over = False
   while not game_over:
       screen.update()
       ball.setx(ball.xcor() + ball.dx)
       ball.sety(ball.ycor() + ball.dy)


       # Ball collision with walls
       if ball.xcor() > 280 or ball.xcor() < -280:
           ball.dx *= -1


       if ball.ycor() > 280:
           ball.dy *= -1


       # Ball collision with paddle
       if (ball.ycor() < -230 and ball.ycor() > -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
           ball.dy *= -1


       # Ball collision with bricks
       for brick in bricks:
           if ball.distance(brick) < 25:
               brick.goto(1000, 1000)  # Move the brick off-screen
               bricks.remove(brick)
               ball.dy *= -1
               update_score()
               break  # Prevent multiple collisions at once


       # Game over conditions
       if ball.ycor() < -290:
           print("Game Over! Press 'R' to Restart or 'Q' to Quit.")
           game_over = True


       if len(bricks) == 0:
           print("You Win! Press 'R' to Restart or 'Q' to Quit.")
           game_over = True


       time.sleep(0.01)  # Slows down the game slightly


# Start the game
game_loop()
screen.mainloop()



