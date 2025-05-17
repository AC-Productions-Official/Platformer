def controlss():
    import pygame
    import sys
    
    pygame.init()

    dis = pygame.display.Info()
    var1, var2 = dis.current_w, dis.current_h
    scw = 1920
    sch = 1080
    screen = pygame.display.set_mode((var1, var2))
    scrSC = pygame.Surface((1920, 1080))

    clock = pygame.time.Clock()

    run = True

    red = (255, 0, 0)
    green = (0, 255, 0)


    sizew = 500
    sizeh = 80




    box4 = pygame.Rect(scw//2 - sizew//2, 700, sizew//2 - 20, sizeh)



    bg = pygame.image.load(r"textures\menubackground.png")
    background = pygame.transform.scale(bg, (scw, sch))


    Q12 = pygame.image.load(r"textures\back1.png")
    Q12 = pygame.transform.scale(Q12, (sizew//2 - 20, sizeh))
    Q22 = pygame.image.load(r"textures\back2.png")
    Q22 = pygame.transform.scale(Q22, (sizew//2 - 20, sizeh))

    Yellow = (200, 200, 50)
    Black = (0,0,0)
    color = Black



    while run:
        scrSC.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        vx = mx * 1920 / var1
        vy = my * 1080 / var2
        scrSC.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if box4.collidepoint((vx, vy)):
                    run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        scrSC.blit(background, (0, 0))
        font = pygame.font.Font(r"textures\Minecraft.ttf", 35)


        text_surface = font.render("-Dont hit the magma blocks", True, color)
        text_surface2 = font.render("-Hit Nether Portal to progress", True, color)
        text_surface3 = font.render("-Arrow Keys or WASD to Move", True, color)
        text_surface4 = font.render("-Go to Minecraft for EXTRA speed", True, color)
        text_surface5 = font.render("There are 10 Levels + 10 from DLC", True, color)
        scrSC.blit(text_surface, (scw//2 - sizew//2, 250 + 50))
        scrSC.blit(text_surface2, (scw//2 - sizew//2, 300 + 50))
        scrSC.blit(text_surface3, (scw//2 - sizew//2, 350 + 50))
        scrSC.blit(text_surface4, (scw//2 - sizew//2, 400 + 50))
        scrSC.blit(text_surface5, (scw//2 - sizew//2, 450 + 50))






        if box4.collidepoint((vx, vy)):
            cons = Q22
        else:
            cons = Q12








        scrSC.blit(cons, (scw//2 - sizew//2, 700))








        clock.tick(60)
        scalesurface = pygame.transform.smoothscale(scrSC, (var1, var2))
        screen.blit(scalesurface, (0,0))
        pygame.display.update()