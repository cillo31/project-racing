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

    def update_img(self, img):
        self.img = image.load(img)

class PlayerSprite(Sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
            if keys[K_LEFT]:
                self.rect.x -= self.speed
                self.update_img('res/car-left1.png')
            elif keys[K_RIGHT]:
                self.rect.x += self.speed
                self.update_img('res/car-right1.png')
            else:
                self.update_img('res/car-up.png')

        if keys[K_DOWN]:
            self.rect.y += self.speed
            if keys[K_LEFT]:
                self.rect.x -= self.speed
                self.update_img('res/car-left3.png')
            elif keys[K_RIGHT]:
                self.rect.x += self.speed
                self.update_img('res/car-right3.png')
            else:
                self.update_img('res/car-down.png')
        
        if keys[K_LEFT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x -= self.speed
            self.update_img('res/car-left2.png')
        
        if keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
            self.rect.x += self.speed
            self.update_img('res/car-right2.png')

class Wall():
    def __init__(self, width, height, x, y):
        self.rect = Rect(x, y, width, height)
        self.width = width
        self.height = height
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        draw.rect(window,(255,255,255),(self.rect.x,self.rect.y,self.width,self.height))