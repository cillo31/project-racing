from pygame import*

#Ventana, dimensiones y background
win_width = 960
win_height = 960
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load('res/1racing-background.png'),(win_width, win_height))
