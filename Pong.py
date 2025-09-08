import turtle

# --- 1. Screen Setup ---
wn = turtle.Screen()
wn.title("Meu Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Turns off screen updates, we'll update manually

# --- 2. Paddle A ---
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Max speed for animation, not movement
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# --- 3. Paddle B ---
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# --- 4. Ball ---
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# --- 5. Scoreboard ---
score_a = 0
score_b = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jogador A: 0  Jogador B: 0", align="center", font=("Courier", 24, "normal"))


# --- 6. Paddle Movement Functions ---
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30 # Aumentado para 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30 # Aumentado para 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30 # Aumentado para 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30 # Aumentado para 30
    paddle_b.sety(y)

# --- 7. Keyboard Bindings ---
wn.listen()  # Listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")  # Up arrow key
wn.onkeypress(paddle_b_down, "Down")  # Down arrow key

# --- 8. Main Game Loop ---
while True:
    wn.update()  # Manually update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right border (scoring)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Jogador A: {score_a}  Jogador B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Jogador A: {score_a}  Jogador B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    # Paddle B collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
            (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # Paddle A collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
            (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1