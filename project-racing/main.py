from pygame import*
from sprites import*

display.set_caption('ARCADE SUNRIDER')
clock = time.Clock()

#lap counter
lap_count = 0

#cooldowns
start_cooldown = 3000
frame_cooldown = 100
lap_cooldown = 10000

#update timers
start_update = time.get_ticks()
go_update = time.get_ticks()
last_lap = time.get_ticks()
last_trophy = time.get_ticks()
last_bomb = time.get_ticks()

#press key to start
k = key.get_pressed()

#MAIN GAME LOOP
running = True
while running:
    #frames per second
    clock.tick(30)
    current_time = time.get_ticks()

    for e in event.get():
        if e.type == QUIT:
            running = False

    if k[K_RETURN] or k[K_SPACE]:
        window.fill((0,0,0))
        window.blit(background,(0,0))

        #go indicator animation
        if lap_count == 0:
            go.animate(go_animation, current_time, go_update, frame_cooldown, 100, 100)

        #bombs sprite update & collision
        for b in bombs:
            b.animate(bomb_animation,current_time,last_bomb,frame_cooldown)

            #gameover: explosion
            if sprite.collide_rect(b, car):
                window.blit(gameover_explosion,(0,0))
                display.update()
                time.delay(3000)
                running = False
        
        #trophy sprite animation
        if lap_count == 3:
            #last lap indicator
            final_lap.reset()
            
            #last lap trophy sprite
            trophy.animate(trophy_animation,current_time,last_trophy,frame_cooldown)

        #trophy collision & lap increment
        if sprite.collide_rect(trophy, car):
            if current_time - last_lap >= lap_cooldown:
                lap_count += 1
                last_lap = current_time
            
            #gameover: winner
            if lap_count > 4:
                window.blit(gameover_winner, (0, 0))
                display.update()
                time.delay(3000)
                running = False

        if lap_count != 0 and lap_count < 5:
            #lap counter
            lap = image.load(laps[lap_count-1])
            window.blit(lap, (50, 20))

        '''if lap_count == 1:
            #screen timer
            start_time = time.get_ticks()
            timer = Timer(start_time, win_width - 100, 25)'''

        #gameover: out of bounds
        if car.rect.x < 0 or car.rect.x > win_width or car.rect.y < 0 or car.rect.y > win_height:
            window.blit(gameover_outbounds,(0,0))
            display.update()
            time.delay(3000)
            running = False
        
        #mantiene dibujados los sprites en pantalla
        car.update()
        car.reset()
        trophy.reset()
        '''if timer
            timer.reset()'''

    else:
        #load screen
        window.fill((0,0,0))
        window.blit(load_screen,(0,0))

        if current_time >= start_cooldown:
            #press to start button animation
            press_start.animate(press_start_animation,current_time,start_update,start_cooldown)
            
            k = key.get_pressed()

    display.update()



    #walls collision
    '''v = 0
    for w in walls:
        if sprite.collide_rect(w, car):
            v += 1
        if v % 2 == 0:
            car.set_speed(self.speed)
        else:
            car.set_speed(self.speed//2)'''