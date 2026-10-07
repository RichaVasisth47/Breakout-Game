from turtle import Turtle, Screen
import time

# --- Screen Setup ---
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# --- Paddle Setup ---
paddle = Turtle()
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# --- Ball Setup ---
ball = Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -230)
ball.x_move = 3
ball.y_move = 3

# --- Bricks Setup ---
bricks = []
colors = ["red", "orange", "yellow", "green"]
row_y = [250, 220, 190, 160]

for i in range(len(row_y)):
    y = row_y[i]
    color = colors[i]
    for x in range(-350, 380, 75):
        brick = Turtle()
        brick.shape("square")
        brick.color(color)
        brick.shapesize(stretch_wid=1, stretch_len=3.2)
        brick.penup()
        brick.goto(x, y)
        bricks.append(brick)

# --- Scoreboard Setup ---
score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
def update_scoreboard():
    scoreboard.clear()
    scoreboard.goto(0, 260)
    scoreboard.write(f"Score: {score}", align="center", font=("Courier", 20, "normal"))

update_scoreboard()

# --- Paddle Movement Controls ---
def go_left():
    if paddle.xcor() > -350:
        paddle.setx(paddle.xcor() - 30)

def go_right():
    if paddle.xcor() < 350:
        paddle.setx(paddle.xcor() + 30)

screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    time.sleep(0.016)
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.x_move)
    ball.sety(ball.ycor() + ball.y_move)

    # Detect collision with left/right walls
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.x_move *= -1

    # Detect collision with top wall
    if ball.ycor() > 280:
        ball.y_move *= -1

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() > -240:
        ball.y_move *= -1

    # Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 35:
            brick.goto(1000, 1000)  # Screen se bahar bhej do
            bricks.remove(brick)
            ball.y_move *= -1
            score += 10
            update_scoreboard()
            break

    # Detect when ball misses the paddle (Game Over)
    if ball.ycor() < -280:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Courier", 30, "bold"))

screen.exitonclick()