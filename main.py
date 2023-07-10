from pygame import*
from sprites import*

display.set_caption('ARCADE SUNRIDER')
display.set_icon(image.load('res/chkp/checkpoint1.png'))
clock = time.Clock()

#counts
lap_count = 0
checkpoint_count = 0

#cooldowns
start_cooldown = 3000
frame_cooldown = 100
checkpoint_cooldown = 1000

#press key to start
k = key.get_pressed()

#MAIN GAME LOOP
running = True
load_screen_done = False
map_selected = False

while running:
    #frames per second
    clock.tick(30)
    current_time = time.get_ticks()

    for e in event.get():
        if e.type == QUIT:
            running = False
        
        if e.type == KEYUP:
            car.speed = 5

    if not load_screen_done:
        # Load screen
        window.fill((0, 0, 0))
        window.blit(load_screen, (0, 0))

        if current_time >= start_cooldown:
            # Press to start button animation
            press_start.animate(press_start_animation, frame_cooldown)

            k = key.get_pressed()

            if k[K_RETURN] or k[K_SPACE]:
                load_screen_done = True

    elif not map_selected:
        # Maps selection screen
        window.fill((0, 0, 0))
        window.blit(selection_screen, (0, 0))

        if current_time >= start_cooldown:
            # Select map to continue button animation
            map_continue.animate(map_continue_animation, frame_cooldown)

        k = key.get_pressed()

        if k[K_1]:
            background,bombs,checkpoints,checkpoint_indicator = maps[0],bombs[0],checkpoints[0],checkpoint_indicator[0]
            map_selected = True
        elif k[K_2]:
            background,bombs,checkpoints,checkpoint_indicator = maps[1],bombs[1],checkpoints[1],checkpoint_indicator[1]
            map_selected = True
        elif k[K_3]:
            background,bombs,checkpoints,checkpoint_indicator = maps[2],bombs[2],checkpoints[2],checkpoint_indicator[2]
            map_selected = True

    else:
        window.fill((0, 0, 0))
        window.blit(background, (0, 0))

        #go sprite animation
        if lap_count == 0:
            go.animate(go_animation, frame_cooldown, 100, 100)
        
        #trophy sprite animation
        if lap_count == 3:
            #last lap indicator
            final_lap.reset()
            #last lap trophy sprite
            trophy.animate(trophy_animation, frame_cooldown, 29,51)

        if lap_count != 0 and lap_count < 5:
            #lap counter
            lap = image.load(laps[lap_count-1])
            window.blit(lap, (50, 20))

            #checkpoint indicator
            chkp = image.load(checkpoint_indicator[checkpoint_count])
            window.blit(chkp, (390, 20))

            '''#screen timer
            start_time = time.get_ticks()
            timer = Timer(start_time, win_width - 100, 25)
            timer.reset()'''

            #bombs sprite update & collision
            for b in bombs:
                b.animate(bomb_animation, frame_cooldown)

                #gameover: explosion
                if sprite.collide_rect(b, car):
                    window.blit(gameover_explosion,(0,0))
                    display.update()
                    time.delay(3000)
                    running = False
            
            #checkpoint sprite update & collision
            for c in checkpoints:
                if checkpoint_count == 0:
                    c.collision = False

                if not c.collision:
                    c.animate(checkpoint_animation, frame_cooldown)
                    if sprite.collide_rect(c, car):
                        if checkpoint_count != len(checkpoints):
                            checkpoint_count += 1
                            c.collision = True
                else:
                    c.animate(checkpointidle_animation, frame_cooldown)

        #trophy collision & lap increment
        if sprite.collide_rect(trophy, car):
            if lap_count == 0:
                lap_count += 1
            else:
                if checkpoint_count >= len(checkpoints):
                    lap_count += 1
                    checkpoint_count = 0
            
            #gameover: winner
            if lap_count > 3:
                window.blit(gameover_winner, (0, 0))
                display.update()
                time.delay(3000)
                running = False     

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