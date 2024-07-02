import time
import turtle
import random
from threading import Thread

type ScreenType = turtle._Screen

class StarryNight:
    def __init__(self) -> None:
        self.screen = turtle.Screen()
        self.screen.bgcolor("black")
        self.screen.title("Starry Night with Turtle Graphics")
        self.twinkling = True
        
        self.draw_moon(100, 150, 50)
        self.create_stars(50)
        
        self.twinkle_manager = TwinkleManager(self.screen)
        self.twinkle_manager.start_twinkling()

        self.screen.listen()
        self.screen.onkey(self.toggle_twinkling, "space")

        self.shooting_star_manager = ShootingStarManager(self.screen, self)
        self.shooting_star_manager.start_shooting()

        turtle.done()
        
    def draw_moon(self, x: int, y: int, radius: int):
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
        
    def create_stars(self, num_stars: int):
        for _ in range(num_stars):
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            size = random.randint(10, 20)
            color = random.choice(["white", "light gray", "light yellow"])
            star = Star(x, y, size, color)
            star.draw()
            
    def toggle_twinkling(self):
        self.twinkling = not self.twinkling
        if self.twinkling:
            self.twinkle_manager.start_twinkling()
        else:
            self.twinkle_manager.stop_twinkling()
            
class Star:
    def __init__(self, x: int, y: int, size: int, color: str):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.color(color)
        self.size = size
        
    def draw(self):
        self.turtle.begin_fill()
        for _ in range(5):
            self.turtle.forward(self.size)
            self.turtle.right(144)
        self.turtle.end_fill()

class TwinkleManager:
    def __init__(self, screen: turtle._Screen) -> None:
        self.screen = screen
        self.twinkle_thread: Thread | None = None
        
    def start_twinkling(self):
        if not self.twinkle_thread or not self.twinkle_thread.is_alive():
            self.twinkle_thread = Thread(target=self.twinkle_stars)
            self.twinkle_thread.start()
    
    def stop_twinkling(self):
        self.twinkle_thread = None
        
    def twinkle_stars(self):
        while self.twinkle_thread:
            x = random.randint(-300, 300)
            y = random.randint(-300, 300)
            size = random.randint(10, 20)
            color = random.choice(["white", "light gray", "light yellow", "black"])
            star = Star(x, y, size, color)
            star.draw()
            time.sleep(0.1)

class ShootingStarManager:
    def __init__(self, screen: ScreenType, starry_night: StarryNight):
        self.screen = screen
        self.starry_night = starry_night
        self.shooting_star_thread = Thread(target=self.shooting_star)
            
    def start_shooting(self):
        self.shooting_star_thread.start()
        
    def shooting_star(self):
        while True:
            if self.starry_night.twinkling:
                self.draw_shooting_star()
            time.sleep(5)

    def draw_shooting_star(self):
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
            if not self.starry_night.twinkling:
                break
            
        star.hideturtle()
        
if __name__ == "__main__":
    StarryNight()