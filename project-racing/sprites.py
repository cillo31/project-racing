from assets import *

#Player character
car = PlayerSprite('res/car/car-up.png',75,300,7)

#single sprites
trophy = Sprite('res/trophy/1st-position.png',75,225,0)
press_start = Sprite('res/start/press-start1.png',75,600,0)
go = Sprite('res/start/go1.png',win_width//2-50,win_height//2-50,0)
final_lap = Sprite('res/lap/finallap.png',win_width//2-100, win_height//2,0)

#sprite 16 bombas para mapa 1
bombs = [
    Sprite('res/bomb/bomb1.png',25,50,0), #1
    Sprite('res/bomb/bomb1.png',175,150,0), #2
    Sprite('res/bomb/bomb1.png',450,150,0), #3
    Sprite('res/bomb/bomb1.png',725,125,0), #4
    Sprite('res/bomb/bomb1.png',185,400,0), #5
    Sprite('res/bomb/bomb1.png',430,375,0), #6
    Sprite('res/bomb/bomb1.png',580,280,0), #7
    Sprite('res/bomb/bomb1.png',780,430,0), #8
    Sprite('res/bomb/bomb1.png',370,530,0), #9
    Sprite('res/bomb/bomb1.png',570,580,0), #10
    Sprite('res/bomb/bomb1.png',180,720,0), #11
    Sprite('res/bomb/bomb1.png',450,770,0), #12
    Sprite('res/bomb/bomb1.png',640,win_height-200,0), #13
    Sprite('res/bomb/bomb1.png',780,win_height-300,0), #14
    Sprite('res/bomb/bomb1.png',50,win_height-75,0), #15
    Sprite('res/bomb/bomb1.png',win_width-50,win_height-50,0) #16
]

#animations
press_start_animation = [
    'res/start/press-start1.png',
    'res/start/press-start2.png',
    'res/start/press-start3.png',
    'res/start/press-start4.png',
    'res/start/press-start5.png',
    'res/start/press-start6.png',
    'res/start/press-start7.png'
]
go_animation = [
    'res/start/go1.png',
    'res/start/go2.png',
    'res/start/go3.png',
    'res/start/go4.png',
    'res/start/go5.png',
    'res/start/go6.png',
    'res/start/go7.png',
    'res/start/go8.png',
    'res/start/go9.png',
    'res/start/go10.png',
    'res/start/go11.png',
    'res/start/go12.png'
]
bomb_animation = [
    'res/bomb/bomb1.png',
    'res/bomb/bomb2.png',
    'res/bomb/bomb3.png',
    'res/bomb/bomb4.png',
    'res/bomb/bomb5.png',
    'res/bomb/bomb6.png'
]
trophy_animation = [
    'res/trophy/trophy1.png',
    'res/trophy/trophy2.png',
    'res/trophy/trophy3.png',
    'res/trophy/trophy4.png',
    'res/trophy/trophy5.png',
    'res/trophy/trophy6.png',
    'res/trophy/trophy7.png',
    'res/trophy/trophy8.png',
    'res/trophy/trophy9.png',
    'res/trophy/trophy10.png',
    'res/trophy/trophy11.png'
]
laps = [
    'res/lap/lap1.png',
    'res/lap/lap2.png',
    'res/lap/lap3.png'
]