# импортируем классы Screen и Turtle
from turtle import Screen, Turtle

def create_field(img_path: str):
    """
    Создаём поле для ровера
    """
    screen = Screen()
    screen.setup(420, 420)
    screen.bgpic(img_path)
    return screen

class Rover(Turtle):
    """
    Марсоход
    """
    def __init__(self, startX: int, startY: int):
        super().__init__()
        self.speed(2)
        self.shapesize(2, 2, 3)
        self.pensize(4)
        self.penup()
        self.goto(startX, startY)
        self.pendown()
