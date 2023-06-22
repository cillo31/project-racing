from assets import *

#Player character
car = PlayerSprite('res/car-up.png',75,300,7)

#single sprites
trophy = Sprite('res/1st-position.png',75,225,0)

#sprite 16 bombas para mapa 1
bombs = [
    Sprite('res/bomb1.png',25,50,0), #1
    Sprite('res/bomb1.png',175,150,0), #2
    Sprite('res/bomb1.png',450,150,0), #3
    Sprite('res/bomb1.png',725,125,0), #4
    Sprite('res/bomb1.png',185,400,0), #5
    Sprite('res/bomb1.png',430,375,0), #6
    Sprite('res/bomb1.png',580,280,0), #7
    Sprite('res/bomb1.png',780,430,0), #8
    Sprite('res/bomb1.png',370,530,0), #9
    Sprite('res/bomb1.png',570,580,0), #10
    Sprite('res/bomb1.png',180,720,0), #11
    Sprite('res/bomb1.png',450,770,0), #12
    Sprite('res/bomb1.png',640,win_height-200,0), #13
    Sprite('res/bomb1.png',780,win_height-300,0), #14
    Sprite('res/bomb1.png',50,win_height-75,0), #15
    Sprite('res/bomb1.png',win_width-50,win_height-50,0) #16
]

#animation
bomb_animation = [
    'res/bomb1.png',
    'res/bomb2.png',
    'res/bomb3.png',
    'res/bomb4.png',
    'res/bomb5.png',
    'res/bomb6.png'
]