import pygame
import sys
import random
pygame.init()

WIDTH,HEIGHT = 350,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DEBARGHYA GAME")
FPS = 60
vel = 4
bullet_vel = 1
score = 0
level = 1
missed = 0
wavelenght = 5
main_font = pygame.font.SysFont("comicsans",30)
leveladd = 0
bullet_hit = pygame.USEREVENT + 1
#loading the sprites
BIRD = pygame.image.load('bird1.png').convert_alpha()
BULLET = pygame.image.load('bulletlarge.png').convert_alpha()
BG = pygame.image.load('space0.jpg').convert_alpha()

bullets = []


def movement(bird):
    keypress = pygame.key.get_pressed()
    if keypress[pygame.K_s] and bird.y + vel>0 and bird.y + vel<580-30:
            bird.y += vel
    if keypress[pygame.K_a] and bird.x - vel>0 and bird.x - vel<350-21:
            bird.x -= vel
    if keypress[pygame.K_w] and bird.y - vel>25 and bird.y - vel<600-26:
            bird.y -= vel
    if keypress[pygame.K_d] and bird.x + vel>0 and bird.x + vel<350-37:
            bird.x += vel
  
def bullet_movement(bullet,bullets,bird):
    global missed
    global score
    global level
    global wavelenght
    global bullet_vel
    global vel
    global leveladd
    for bullet in bullets:
        bullet.y += bullet_vel
        if bird.colliderect(bullet):
            pygame.event.post(pygame.event.Event(bullet_hit))
            bullets.remove(bullet)
            score += 1
            if len(bullets) == 0:
                level += 1
                wavelenght += 1
                bullet_vel += leveladd
                vel += leveladd
                for i in range(wavelenght):
        
                    BULLETX = random.randrange(10, 330,random.randrange(10,100))
                    BULLETY = random.randrange(-300,200,random.randrange(10,80))
                    bullet = pygame.Rect(BULLETX,BULLETY,20,30)
                    bullets.append(bullet)
            

        elif bullet.y + bullet_vel > 550:
            missed += 1
            bullets.remove(bullet)
            if len(bullets) == 0:
                level += 1
                wavelenght += 1
                bullet_vel+= leveladd
                vel += leveladd
                for i in range(wavelenght):
        
                    BULLETX = random.randrange(10, 350,100)
                    BULLETY = random.randrange(-300,200,50)
                    bullet = pygame.Rect(BULLETX,BULLETY,20,30)
                    bullets.append(bullet)
            

            
def draw_window(bird,bullet,bullets,BULLET):

    global score 
    global missed
    global main_font
    global level
    score_label = main_font.render(f"SCORE: {score}",1,(255,255,255))
    missed_label = main_font.render(f"MISSED: {missed}",1,(255,255,255))
    level_label = main_font.render(f"LEVEL: {level}",1,(255,255,255))
    WIN.blit(BG,(0,0))
    WIN.blit(BIRD,(bird.x,bird.y))
    for bullet in bullets:
        WIN.blit(BULLET,(bullet.x,bullet.y))
    
    WIN.blit(score_label,(5,10))
    WIN.blit(missed_label,(125,10))
    WIN.blit(level_label,(250,10))

    pygame.display.update()

def main(bullets):
    
    global wavelenght
   
    for i in range(wavelenght):
        
        BULLETX = random.randrange(10, 350,50)
        BULLETY = random.randrange(-400,100,70)
        bullet = pygame.Rect(BULLETX,BULLETY,20,30)
        bullets.append(bullet)
        
    bird = pygame.Rect((350-40)/2,(600-30)/2,40,30)
    
    clock = pygame.time.Clock()
    run = True
    while run :
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        movement(bird)
        draw_window(bird,bullet,bullets,BULLET)
        bullet_movement(bullet,bullets,bird)
        
        
if __name__ == '__main__':
    main(bullets)
    