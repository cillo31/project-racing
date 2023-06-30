from pygame import*

# Program window
win_width = 960
win_height = 960
window = display.set_mode((win_width, win_height))

# load screen & gameover
load_screen = transform.scale(image.load('res/bkg/load-screen.jpg'),(win_width, win_height))
selection_screen = transform.scale(image.load('res/bkg/selection-screen.jpg'),(win_width, win_height))
gameover_explosion = transform.scale(image.load('res/bkg/gameover-explosion.jpg'),(win_width, win_height))
gameover_outbounds = transform.scale(image.load('res/bkg/gameover-outbounds.jpg'), (win_width, win_height))
gameover_winner = transform.scale(image.load('res/bkg/gameover-winner.jpg'), (win_width, win_height))

# map background
maps = [
    transform.scale(image.load('res/bkg/1racing-background.png'),(win_width, win_height)),
    transform.scale(image.load('res/bkg/2racing-background.png'),(win_width, win_height)),
    transform.scale(image.load('res/bkg/3racing-background.png'),(win_width, win_height)),
]