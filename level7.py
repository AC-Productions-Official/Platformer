import pygame
import sys
pygame.init()
dis = pygame.display.Info()
screen_width = dis.current_w
screen_height = dis.current_h
GRAV = screen_height/2160
jump = screen_height/67#im a fucking genus
Yspeed = 0
Xspeed = 0
jumpTF = False
leftright = screen_height/180#im too smart
canjump = False
canright = True
canleft = True
ontop = False
finish = False
death = False

TouchingPlace = []

clock = pygame.time.Clock()
rownum = 32
collumnum = 18
size = screen_height//collumnum#this is accually genius
sizeX = screen_width//rownum
#1=block 2=lava 3=spawn 4=goal
level = [
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,
1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,1,0,0,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,2,0,1,
1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,0,1,0,1,0,0,2,0,1,
1,0,0,0,0,1,0,0,0,0,0,0,1,0,2,0,0,0,0,0,0,2,0,0,0,0,1,0,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,1,0,2,0,1,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,0,0,4,0,0,0,1,0,2,0,1,
1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1,0,0,0,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1


]
boxes = []
lava = []
win = []
#convert to boxes
for a in range(576):
    if level[a] == 1:
        rowNumber1 = (a//rownum)
        relX = (a-(rowNumber1*rownum))*size
        relY = rowNumber1*size
        boxes.append(pygame.Rect(relX,relY,sizeX,size))
        # plat = pygame.draw.rect(screen,"black",(relX,relY,sizeX,size))
    elif level[a] == 4:#goal
        rowNumber1 = (a//rownum)
        relX = (a-(rowNumber1*rownum))*size
        relY = rowNumber1*size
        win.append(pygame.Rect(relX,relY,sizeX,size))
    elif level[a]==2:#spikes
        rowNumber1 = (a//rownum)
        relX = (a-(rowNumber1*rownum))*size
        relY = rowNumber1*size
        lava.append(pygame.Rect(relX,relY,sizeX,size))





####################


for i in range(576):
    if level[i] == 3:
        rowNumber = (i//rownum)#0=first row
        ia = i-(rowNumber*rownum)
        PlayerY = rowNumber*size
        PlayerX = ia*size
# PlayerX = 100
# PlayerY = screen_height-300
try:
    OGY = PlayerY
    OGX = PlayerX
except:
    print("you forgot the dang spawn dumbass")
    input()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Platformer")
player = pygame.Rect(PlayerX, PlayerY, sizeX, size)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_r:
                Yspeed=0
                player.x = OGX
                player.y = OGY
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if canjump:
                    Yspeed = -jump
                    canjump = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        Xspeed = leftright
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        Xspeed = -leftright
    else:
        Xspeed = 0
    ########################################################
    #calc left/right
    player.x += Xspeed
    #grav
    Yspeed += GRAV

    #test for right/left
    for box in boxes:
        if player.colliderect(box):
            if Xspeed > 0:  # Moving right, collided with left side of box
                player.x = box.x - player.width
            elif Xspeed < 0:  # Moving left, collided with right side of box
                player.x = box.x + box.width
    
###########################


    player.y += Yspeed
    for box in boxes:
        if player.colliderect(box):
            if Yspeed > 0:  # Moving down, landed on top of box
                player.y = box.y - player.height
                Yspeed = 0
                canjump = True
            elif Yspeed < 0:  # Moving up, hit bottom of box
                player.y = box.y + box.height
                Yspeed = 0
    if finish:
        break
    if death:
        Yspeed=0
        player.x = OGX
        player.y = OGY
        death = False

    ############################## start rendering shit
    screen.fill((255, 255, 255))

    ################################### stupid death shit and win shit I want to kms
    for lava1 in lava:
        pygame.draw.rect(screen, "red", lava1)
        if player.colliderect(lava1):
            death = True
    for win1 in win:
        pygame.draw.rect(screen, "green", win1)
        if player.colliderect(win1):
            print("Level 7 completed!!!!")
            run = False
            
    #########################
    #render the actual boxes
    for box in boxes:
        pygame.draw.rect(screen, "black", box)
    #########################
    
    
    pygame.draw.rect(screen, "blue", player)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
import level8.py
