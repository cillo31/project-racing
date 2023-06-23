from maps import*

class Sprite():
    def __init__(self, img, x, y, speed):
        self.img = image.load(img)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

    def update_img(self, img, width=None, height=None):
        if width is None or height is None:
            self.img = image.load(img)
        else:
            self.img = transform.scale(image.load(img), (width, height))
    
    def animate(self, animated_list, current_time, last_update, frame_cooldown, width=None, height=None):
        self.animated_list = animated_list
        self.current_time = current_time
        self.last_update = last_update
        self.frame_cooldown = frame_cooldown
        self.index = 0

        if self.current_time - self.last_update >= self.frame_cooldown:
            self.index += 1
            if self.index >= len(self.animated_list):
                self.index = 0
            self.last_update = self.current_time
        
        self.update_img(self.animated_list[self.index], width, height)
        window.blit(self.img, (self.rect.x, self.rect.y))

class PlayerSprite(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
            if keys[K_LEFT]:
                self.rect.x -= self.speed
                self.update_img('res/car/car-left1.png')
            elif keys[K_RIGHT]:
                self.rect.x += self.speed
                self.update_img('res/car/car-right1.png')
            else:
                self.update_img('res/car/car-up.png')

        if keys[K_DOWN]:
            self.rect.y += self.speed
            if keys[K_LEFT]:
                self.rect.x -= self.speed
                self.update_img('res/car/car-left3.png')
            elif keys[K_RIGHT]:
                self.rect.x += self.speed
                self.update_img('res/car/car-right3.png')
            else:
                self.update_img('res/car/car-down.png')
        
        if keys[K_LEFT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x -= self.speed
            self.update_img('res/car/car-left2.png')
        
        if keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x += self.speed
            self.update_img('res/car/car-right2.png')

class Timer():
    def __init__(self, start_time, x, y):
        self.counting_time = time.get_ticks() - start_time

        # change milliseconds into minutes, seconds, milliseconds
        self.mins = str(self.counting_time/60000).zfill(2)
        self.secs = str((self.counting_time%60000)/1000).zfill(2)
        self.mills = str(self.counting_time%1000).zfill(3)

        self.font = font.Font(None, 32)
        self.string = "%s:%s:%s" % (self.mins, self.secs, self.mills)
        self.text = self.font.render(str(self.string), True, (255,255,255))
        self.rect = self.text.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.text, (self.rect.x, self.rect.y))

class Wall():
    def __init__(self, width, height, x, y):
        self.rect = Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        draw.rect(window,(255,255,255),(self.rect.x,self.rect.y,self.width,self.height))