from assets import *

#Player character
car = PlayerSprite('res/car/car-up.png',75,300,5)

#single sprites
trophy = Sprite('res/trophy/1st-position.png',75,225,0)
press_start = Sprite('res/start/press-start1.png',75,600,0)
map_continue = Sprite('res/start/map-continue1.png',75,850,0)
go = Sprite('res/start/go1.png',win_width//2-50,win_height//2-50,0)
final_lap = Sprite('res/lap/finallap.png',win_width//2-100, win_height//2,0)

#sprites multiples map 1
bombs1 = [
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
checkpoints1 = [
    Sprite('res/chkp/checkpoint1.png',200,50,0), #1
    Sprite('res/chkp/checkpoint1.png',450,250,0), #2
    Sprite('res/chkp/checkpoint1.png',725,50,0), #3
    Sprite('res/chkp/checkpoint1.png',825,win_height-150,0), #4
    Sprite('res/chkp/checkpoint1.png',100,win_height-150,0), #5
]
chkp_indicator1 = [
    'res/chkp/checkpoint-indicator0.png',
    'res/chkp/checkpoint-indicator1.png',
    'res/chkp/checkpoint-indicator2.png',
    'res/chkp/checkpoint-indicator3.png',
    'res/chkp/checkpoint-indicator4.png',
    'res/chkp/checkpoint-indicator5.png',
]
#sprites map 2
bombs2 = [
    Sprite('res/bomb/bomb1.png',50,50,0), #1
    Sprite('res/bomb/bomb1.png',350,25,0), #2
    Sprite('res/bomb/bomb1.png',675,25,0), #3
    Sprite('res/bomb/bomb1.png',win_width-75,50,0), #4
    Sprite('res/bomb/bomb1.png',200,125,0), #5
    Sprite('res/bomb/bomb1.png',500,100,0), #6
    Sprite('res/bomb/bomb1.png',825,100,0), #7
    Sprite('res/bomb/bomb1.png',400,225,0), #8
    Sprite('res/bomb/bomb1.png',250,400,0), #9
    Sprite('res/bomb/bomb1.png',400,350,0), #10
    Sprite('res/bomb/bomb1.png',625,350,0), #11
    Sprite('res/bomb/bomb1.png',760,275,0), #12
    Sprite('res/bomb/bomb1.png',175,500,0), #13
    Sprite('res/bomb/bomb1.png',460,475,0), #14
    Sprite('res/bomb/bomb1.png',775,500,0), #15
    Sprite('res/bomb/bomb1.png',300,675,0), #16
    Sprite('res/bomb/bomb1.png',win_width-50,600,0), #17
    Sprite('res/bomb/bomb1.png',225,775,0), #18
    Sprite('res/bomb/bomb1.png',460,700,0), #19
    Sprite('res/bomb/bomb1.png',750,700,0), #20
    Sprite('res/bomb/bomb1.png',75,win_height-75,0), #21
    Sprite('res/bomb/bomb1.png',715,win_height-125,0), #22
    Sprite('res/bomb/bomb1.png',815,win_height-100,0) #23
]
checkpoints2 = [
    Sprite('res/chkp/checkpoint1.png',200,50,0), #1
    Sprite('res/chkp/checkpoint1.png',425,575,0), #2
    Sprite('res/chkp/checkpoint1.png',700,175,0), #3
    Sprite('res/chkp/checkpoint1.png',win_width-125,550,0), #4
    Sprite('res/chkp/checkpoint1.png',575,win_height-150,0), #5
    Sprite('res/chkp/checkpoint1.png',125,win_height-150,0) #6
]
chkp_indicator2 = [
    'res/chkp/map2-ci0.png',
    'res/chkp/map2-ci1.png',
    'res/chkp/map2-ci2.png',
    'res/chkp/map2-ci3.png',
    'res/chkp/map2-ci4.png',
    'res/chkp/map2-ci5.png',
    'res/chkp/map2-ci6.png'
]
#sprites map 3
bombs3 = [
    Sprite('res/bomb/bomb1.png',375,50,0), #1
    Sprite('res/bomb/bomb1.png',win_width-50,50,0), #2
    Sprite('res/bomb/bomb1.png',200,125,0), #3
    Sprite('res/bomb/bomb1.png',475,125,0), #4
    Sprite('res/bomb/bomb1.png',750,150,0), #5
    Sprite('res/bomb/bomb1.png',180,275,0), #6
    Sprite('res/bomb/bomb1.png',560,300,0), #7
    Sprite('res/bomb/bomb1.png',win_width-75,325,0), #8
    Sprite('res/bomb/bomb1.png',75,450,0), #9
    Sprite('res/bomb/bomb1.png',375,375,0), #10
    Sprite('res/bomb/bomb1.png',725,400,0), #11
    Sprite('res/bomb/bomb1.png',175,550,0), #12
    Sprite('res/bomb/bomb1.png',550,475,0), #13
    Sprite('res/bomb/bomb1.png',win_width-75,500,0), #14
    Sprite('res/bomb/bomb1.png',375,625,0), #15
    Sprite('res/bomb/bomb1.png',460,650,0), #16
    Sprite('res/bomb/bomb1.png',575,625,0), #17
    Sprite('res/bomb/bomb1.png',750,650,0), #18
    Sprite('res/bomb/bomb1.png',200,win_height-200,0), #19
    Sprite('res/bomb/bomb1.png',460,725,0), #20
    Sprite('res/bomb/bomb1.png',640,700,0), #21
    Sprite('res/bomb/bomb1.png',win_width-50,win_height-200,0), #22
    Sprite('res/bomb/bomb1.png',725,win_height-100,0) #23
]
checkpoints3 = [
    Sprite('res/chkp/checkpoint1.png',200,50,0), #1
    Sprite('res/chkp/checkpoint1.png',450,250,0), #2
    Sprite('res/chkp/checkpoint1.png',725,50,0), #3
    Sprite('res/chkp/checkpoint1.png',625,425,0), #4
    Sprite('res/chkp/checkpoint1.png',825,win_height-250,0), #5
    Sprite('res/chkp/checkpoint1.png',100,win_height-150,0), #6
    Sprite('res/chkp/checkpoint1.png',300,475,0) #7
]
chkp_indicator3 = [
    'res/chkp/map3-ci0.png',
    'res/chkp/map3-ci1.png',
    'res/chkp/map3-ci2.png',
    'res/chkp/map3-ci3.png',
    'res/chkp/map3-ci4.png',
    'res/chkp/map3-ci5.png',
    'res/chkp/map3-ci6.png',
    'res/chkp/map3-ci7.png'
]

#animations
press_start_animation = [
    'res/start/press-start1.png',
    'res/start/press-start2.png',
    'res/start/press-start3.png',
    'res/start/press-start4.png',
    'res/start/press-start5.png',
    'res/start/press-start6.png',
    'res/start/press-start7.png',
    'res/start/press-start8.png',
    'res/start/press-start9.png',
    'res/start/press-start10.png'
]
map_continue_animation = [
    'res/start/map-continue1.png',
    'res/start/map-continue2.png',
    'res/start/map-continue3.png',
    'res/start/map-continue4.png',
    'res/start/map-continue5.png',
    'res/start/map-continue6.png',
    'res/start/map-continue7.png',
    'res/start/map-continue8.png',
    'res/start/map-continue9.png',
    'res/start/map-continue10.png',
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
checkpoint_animation = [
    'res/chkp/checkpoint1.png',
    'res/chkp/checkpoint2.png',
    'res/chkp/checkpoint3.png',
    'res/chkp/checkpoint4.png',
    'res/chkp/checkpoint5.png',
    'res/chkp/checkpoint6.png',
    'res/chkp/checkpoint7.png'
]
checkpointidle_animation = [
    'res/chkp/checkpoint-idle1.png',
    'res/chkp/checkpoint-idle2.png',
    'res/chkp/checkpoint-idle3.png',
    'res/chkp/checkpoint-idle4.png',
    'res/chkp/checkpoint-idle5.png',
    'res/chkp/checkpoint-idle6.png',
    'res/chkp/checkpoint-idle7.png'
]