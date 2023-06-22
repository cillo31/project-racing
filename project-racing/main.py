from pygame import*
from sprites import*

display.set_caption('SUNRIDE')
clock = time.Clock()

#contador de vueltas
lap_count = 0

#Bucle principal del juego
running = True
while running:
    #frames per second
    clock.tick(30)
    for e in event.get():
        if e.type == QUIT:
            running = False
        
    window.fill((0,0,0))
    window.blit(background,(0,0))
    
    #bombs sprite update & collision
    index = 0
    for b in bombs:
        
        b.update_img()
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
    if sprite.collide_rect(trophy, car):
        lap_count += 1
        if lap_count == 3:
            trophy.update_img('res/trophy.png')
            trophy.reset()
            final_lap = image.load('res/finallap.png')
            window.blit(final_lap, (win_width // 2, win_height // 2))
        if lap_count > 3:
            winner = transform.scale(image.load('res/gameover-winner.jpg'), (win_width, win_height))
            window.blit(winner, (0, 0))
            display.update()
            time.delay(3000)
            running = False
        laps = image.load('res/lap' + str(lap_count) + '.png')
        window.blit(laps, (100, 50))


    #gameover out of bounds
    if car.rect.x < 0 or car.rect.x > win_width or car.rect.y < 0 or car.rect.y > win_height:
        gameover = transform.scale(image.load('res/gameover-outbounds.jpg'), (win_width, win_height))
        window.blit(gameover,(0,0))
        display.update()
        time.delay(3000)
        running = False

    car.update()
    car.reset()
    trophy.reset()

    display.update()