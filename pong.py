# pong game
# by Seth Johnston

import turtle
import winsound as ws

# turtles
pen = turtle.Turtle()
wn = turtle.Screen()
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()

# screen
wn.title("Pong by Seth")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# useful variables
ysg = 1.25
xsg = 1.25
score_a = 0
score_b = 0
HA1 = 0
HA2 = 40
HB1 = 0
HB2 = 40
run = True

# Useful definitions


def quit():
    global run
    run = False


def pen1(x, y):
    pen.speed(0)  # what does this do?
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(x, y)
    pen.write(
        "Player One: {}  Player Two: {}".format(score_a, score_b),
        align="center",
        font=("courier", 24, "normal"),
    )


def pen2(x, y):
    pen.goto(x, y)
    pen.write(
        "ball speed up and down: {} left and right: {}".format(
            speedx_display, speedy_display
        ),
        align="center",
        font=("courier", 11, "normal"),
    )


def paddle_a_refresh():
    paddle_a.speed(0)  # what does this do?
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=HA1 + 5, stretch_len=1)
    paddle_a.penup()


def paddle_b_refresh():
    paddle_b.speed(0)  # what does this do?
    paddle_b.shape("square")
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=HB1 + 5, stretch_len=1)
    paddle_b.penup()


def ball_setup(x, y):
    ball.speed(0)  # what does this do?
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(x, y)


# paddle A

paddle_a_refresh()
paddle_a.goto(-350, 0)

# paddle B

paddle_b_refresh()
paddle_b.goto(350, 0)

# ball
ball_setup(0, 0)
ball.dx = 0.25
ball.dy = -0.25
speedx_display = ball.dx * -1
speedy_display = ball.dy * -1

# pen
pen1(0, 260)
pen2(0, 250)


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)


def paddle_a_up_fast():
    y = paddle_a.ycor()
    y += 80
    paddle_a.sety(y)


def paddle_a_down__fast():
    y = paddle_a.ycor()
    y -= 80
    paddle_a.sety(y)


def paddle_b_up_fast():
    y = paddle_b.ycor()
    y += 80
    paddle_b.sety(y)


def paddle_b_down_fast():
    y = paddle_b.ycor()
    y -= 80
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_a_up_fast, "W")
wn.onkeypress(paddle_a_down__fast, "S")
wn.onkeypress(paddle_b_up_fast, "O")
wn.onkeypress(paddle_b_down_fast, "L")
wn.onkeypress(quit, "q")

# main game loop
while run:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 255:
        ball.sety(255)
        ball.dy *= -1
        ws.PlaySound(
            "bounce.wav", ws.SND_ASYNC
        )  # why does the .wav not install in an installer?

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ws.PlaySound("bounce.wav", ws.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx /= xsg
        speedx_display /= xsg
        speedy_display /= ysg
        ball.dx *= -1
        ball.dy /= ysg
        score_a += 1
        pen.clear()
        pen1(0, 260)
        pen2(0, 250)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx /= xsg
        speedx_display /= xsg
        speedy_display /= ysg
        ball.dx *= -1
        ball.dy /= ysg
        score_b += 1
        pen.clear()
        pen1(0, 260)
        pen2(0, 250)

    # paddle and ball collisions
    if (ball.xcor() > 320 and ball.xcor() > 350) and (
        ball.ycor() < paddle_b.ycor() + HB2 and ball.ycor() > paddle_b.ycor() - HB2
    ):
        ball.setx(315)
        speedx_display *= xsg
        speedy_display *= ysg
        ball.dx *= xsg
        ball.dx *= -1
        ball.dy *= ysg
        ws.PlaySound("bounce.wav", ws.SND_ASYNC)
        ball.pendown()
        ball.color("red")
        ball.penup()
        pen.clear()
        pen1(0, 260)
        pen2(0, 250)

    if (ball.xcor() < -320 and ball.xcor() < -350) and (
        ball.ycor() < paddle_a.ycor() + HA2 and ball.ycor() > paddle_a.ycor() - HA2
    ):
        ball.setx(-315)
        ball.dx *= xsg
        speedx_display *= xsg
        speedy_display *= ysg
        ball.dx *= -1
        ball.dy *= ysg
        ws.PlaySound("bounce.wav", ws.SND_ASYNC)
        ball.pendown()
        ball.color("blue")
        ball.penup()
        pen.goto(0, 260)
        pen.clear()
        pen1(0, 260)
        pen2(0, 250)

wn.bye()
