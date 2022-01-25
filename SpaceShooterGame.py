import pygame
import sys
import random
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)
# display function
def text_display(score):
     font=pygame.font.SysFont("Times New Roman",35)
     if score >20:
          text=font.render("Game Over",True,(255,255,255))
          text1=font.render("Congratulations You Won!! :)",True,(255,255,255))
     if score<20:
          text=font.render("Game Over",True,(255,255,255))
          text1=font.render("You loose!! Better Luck next time:(",True,(255,255,255))
     screen.blit(text,(500,300))
     screen.blit(text1,(500,400))
def score_display(score):
     font=pygame.font.SysFont("Times New Roman",20)
     text=font.render("Score:"+str(score),True,(255,255,255))
     screen.blit(text,(800,50))

#group
sprite_group=pygame.sprite.Group()
spaceship_group = pygame.sprite.GroupSingle()
meteor_group = pygame.sprite.Group()

#meteor lists
meteor_names = ["Meteor1.png","Meteor2.png","Meteor3.png"]

clock = pygame.time.Clock()
#spaceship class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect(center =(x_pos,y_pos))
        
        
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        if self.rect.centery>600:
             self.rect.centery=600
    def remove(self):
        self.kill()
    

        
score=0

shield_group=pygame.sprite.Group()
h=10
        
#meteor class        
class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, meteor_x, meteor_y, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.meteor_x = random.randint(4,10)
        self.meteor_y = random.randint(5,15)
        self.rect = self.image.get_rect(center = (meteor_x, meteor_y))
    def update(self):
        self.rect.x += self.meteor_x
        self.rect.y += self.meteor_y
    def remove(self):
        self.kill()
#laser class
class Laser(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("Laser.png")
        x,y=pos
        self.rect=self.image.get_rect(center = (pos))
        self.speed = 4
        self.remove()
        
    def update(self):
        self.rect.y -= self.speed
    def remove(self):
        if self.rect.y<=0:
            self.kill()
            
        
        
    
    
        
    
#add spaceship to group        
spaceship=Spaceship("spaceship.png",650,500,10)
sprite_group.add(spaceship)
spaceship_group.add(spaceship)
#add meteor to group
meteor=Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
sprite_group.add(meteor)
meteor_group.add(meteor)
#laser group
laser_group=pygame.sprite.Group()



meteorClone = pygame.USEREVENT
pygame.time.set_timer(meteorClone,1000)

meteorClone_1=pygame.USEREVENT+1
pygame.time.set_timer(meteorClone_1,1500)

        
play=True        
    

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == meteorClone:
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
        if event.type == meteorClone_1:
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
            meteor = Meteor(random.choice(meteor_names),random.randint(0,1280),10,random.randint(1,5))
            
            meteor_group.add(meteor)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
             laser=Laser(spaceship.rect.center)
             sprite_group.add(laser)
             laser_group.add(laser)
        if pygame.sprite.groupcollide(laser_group,meteor_group,False,True):
            meteor_group.remove()
            score+=1
        if pygame.sprite.groupcollide(spaceship_group,meteor_group,False,True):
            h-=1
            meteor_group.remove()
        if h<=0:
            spaceship.remove()
            play=False
            
            
       
        
             
    laser_group.update()
    meteor_group.update()
   
    
    screen.fill((42,45,51))
    spaceship_group.update()
   
    sprite_group.draw(screen)
    meteor_group.draw(screen)
    shield_group.draw(screen)
    pygame.draw.rect(screen,(255,255,255),(100,50,(10*h),10))
    score_display(score)
    pygame.display.update()
    clock.tick(120)

def restart(score):
     while True:
          screen.fill((42,48,51))
          for event in pygame.event.get():
               if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
          text_display(score)
          pygame.display.update()

restart(score)
    
