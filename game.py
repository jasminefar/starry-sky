import turtle
import random
import threading
import time

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Starry Night with Turtle Graphics")

# Function to draw the moon
def draw_moon(x, y, radius):
    moon = turtle.Turtle()
    moon.hideturtle()
    moon.speed(0)
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    moon.color("light yellow")
    moon.begin_fill()
    moon.circle(radius)
    moon.end_fill()

# Function to draw a star
def draw_star(x, y, size, color):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Function to create stars at random positions
def create_stars(num_stars):
    colors = ["white", "light gray", "light yellow"]
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(10, 20)
        color = random.choice(colors)
        draw_star(x, y, size, color)

# Function to make stars twinkle
twinkling = True
def twinkle_stars():
    while twinkling:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        size = random.randint(10, 20)
        color = random.choice(["white", "light gray", "light yellow", "black"])
        draw_star(x, y, size, color)

# Function to draw a shooting star
def draw_shooting_star():
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color("white")
    star.penup()
    start_x = random.randint(-300, 300)
    start_y = random.randint(-300, 300)
    star.goto(start_x, start_y)
    star.pendown()
    for _ in range(20):
        star.forward(10)
        star.right(15)
        if not twinkling:
            break
    star.hideturtle()

# Function to toggle twinkling
def toggle_twinkling():
    global twinkling
    twinkling = not twinkling
    if twinkling:
        threading.Thread(target=twinkle_stars).start()

# Draw the moon
draw_moon(100, 150, 50)

# Create initial stars
create_stars(50)

# Start twinkling stars in a separate thread
twinkle_thread = threading.Thread(target=twinkle_stars)
twinkle_thread.start()

# Bind the space key to toggle twinkling
screen.listen()
screen.onkey(toggle_twinkling, "space")

# Draw a shooting star every 5 seconds
def shooting_star():
    while True:
        if twinkling:
            draw_shooting_star()
        time.sleep(5)

shooting_star_thread = threading.Thread(target=shooting_star)
shooting_star_thread.start()

# Keep the window open
turtle.done()
