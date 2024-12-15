from turtle import *
from PIL import Image

# Set up the turtle screen
screen = Screen()

# Example usage of Pillow to load an image
image = Image.open("txt.png")
image.show()

# Your turtle code here
turtle = Turtle()
turtle.forward(100)
done()
