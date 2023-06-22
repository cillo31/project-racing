from pygame import*
from sprites import*

display.set_caption('SUNRIDE')
clock = time.Clock()

#contador de vueltas
lap_count = 0

#Bucle principal del juego
running = True
last_update = time.get_ticks()
last_update2 = time.get_ticks() 
cooldown = 100
trophy_cooldown = 10000
frame_index = 0

while running:
    #frames per second
    clock.tick(30)
    current_time = time.get_ticks()

    for e in event.get():
        if e.type == QUIT:
            running = False
        
    window.fill((0,0,0))
    window.blit(background,(0,0))
    
    #bombs sprite update & collision
    if current_time - last_update >= cooldown:
        frame_index += 1
        if frame_index >= len(bomb_animation):
            frame_index = 0
        current_image = bomb_animation[frame_index]
        last_update = current_time

    for b in bombs:
        b.update_img(bomb_animation[frame_index])
        b.reset()

        if sprite.collide_rect(b, car):
            gameover = transform.scale(image.load('res/gameover-explosion.jpg'), (win_width, win_height))
            window.blit(gameover,(0,0))
            display.update()
            time.delay(3000)
            running = False
    
    #colision con paredes
    '''v = 0
    for w in walls:
        if sprite.collide_rect(w, car):
            v += 1
        if v % 2 == 0:
            car.set_speed(self.speed)
        else:
            car.set_speed(self.speed//2)'''
    
    #colision con el trofeo
    current_time2 = time.get_ticks()
    if sprite.collide_rect(trophy, car):
        if lap_count != 0:
            if current_time2 - last_update2 >= trophy_cooldown:
                lap_count += 1
                if lap_count == 3:
                    trophy.update_img('res/trophy.png')
                    trophy.reset()
                if lap_count > 3:
                    winner = transform.scale(image.load('res/gameover-winner.jpg'), (win_width, win_height))
                    window.blit(winner, (0, 0))
                    display.update()
                    time.delay(3000)
                    running = False
                last_update2 = current_time2
        else:
            lap_count+=1

    #gameover out of bounds
    if car.rect.x < 0 or car.rect.x > win_width or car.rect.y < 0 or car.rect.y > win_height:
        gameover = transform.scale(image.load('res/gameover-outbounds.jpg'), (win_width, win_height))
        window.blit(gameover,(0,0))
        display.update()
        time.delay(3000)
        running = False

    if lap_count != 0:
        laps = image.load('res/lap' + str(lap_count) + '.png')
        window.blit(laps, (50, 20))

        '''#contrareloj en pantalla
        start_time = time.get_ticks()
        timer = Timer(start_time, win_width - 100, 25)
        timer.reset()'''

    if lap_count == 3:
        final_lap = image.load('res/finallap.png')
        window.blit(final_lap, (win_width // 2 - 100, win_height // 2))
    
    #mantiene dibujados los sprites en pantalla
    car.update()
    car.reset()
    trophy.reset()
    

    display.update()