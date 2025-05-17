def menuscreen(hardc, hardc1, dead):
    import pygame
    import sys
    import random
    import math
    pygame.init()

    dis = pygame.display.Info()
    var1, var2 = dis.current_w, dis.current_h
    scw = 1920
    sch = 1080
    screen = pygame.display.set_mode((var1, var2))
    scrSC = pygame.Surface((1920, 1080))
    clock = pygame.time.Clock()

    run = True
    Yellow = (200, 200, 50)
    red = (255, 0, 0)
    green = (0, 255, 0)

    superstart = False

    sizew = 500
    sizeh = 80

    toggle = hardc1

    box1 = pygame.Rect(scw//2 - sizew//2, 450 , sizew, sizeh)
    box2 = pygame.Rect(scw//2 - sizew//2, 575, sizew, sizeh)

    box3 = pygame.Rect(scw//2 - sizew//2, 700, sizew//2 - 20, sizeh)
    box4 = pygame.Rect(scw//2 + 20, 700, sizew//2 - 20, sizeh)



    bg = pygame.image.load(r"textures\menubackground.png")
    background = pygame.transform.scale(bg, (scw, sch))



    start = pygame.image.load(r"textures\start.png")
    start = pygame.transform.scale(start, (sizew, sizeh))
    start2 = pygame.image.load(r"textures\start2.png")
    start2 = pygame.transform.scale(start2, (sizew, sizeh))

    hardon1 = pygame.image.load(r"textures\hardon.png")
    hardon1 = pygame.transform.scale(hardon1, (sizew, sizeh))
    hardon2 = pygame.image.load(r"textures\hardon2.png")
    hardon2 = pygame.transform.scale(hardon2, (sizew, sizeh))
    hardoff1 = pygame.image.load(r"textures\hardoff.png")
    hardoff1 = pygame.transform.scale(hardoff1, (sizew, sizeh))
    hardoff2 = pygame.image.load(r"textures\hardoff2.png")
    hardoff2 = pygame.transform.scale(hardoff2, (sizew, sizeh))

    Q1 = pygame.image.load(r"textures\Q1.png")
    Q1 = pygame.transform.scale(Q1, (sizew//2 - 20, sizeh))
    Q2 = pygame.image.load(r"textures\Q2.png")
    Q2 = pygame.transform.scale(Q2, (sizew//2 - 20, sizeh))


    Q12 = pygame.image.load(r"textures\Con1.png")
    Q12 = pygame.transform.scale(Q12, (sizew//2 - 20, sizeh))
    Q22 = pygame.image.load(r"textures\Con2.png")
    Q22 = pygame.transform.scale(Q22, (sizew//2 - 20, sizeh))







    while run:
        scrSC.fill((0,0,0))
        mx, my = pygame.mouse.get_pos()
        virtual_mx = mx * 1920 / var1
        virtual_my = my * 1080 / var2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if box2.collidepoint(virtual_mx, virtual_my):
                    toggle = not toggle
                if box1.collidepoint(virtual_mx, virtual_my):
                    superstart = True



                    run = False
                if box3.collidepoint(virtual_mx, virtual_my):




                    run = False
                if box4.collidepoint(virtual_mx, virtual_my):
                    import controls as con
                    con.controlss()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        elif keys[pygame.K_RETURN]:
            superstart = True
            run = False
        font = pygame.font.SysFont("Arial", 70)
        text_surface = font.render("You lose and Your Final Score is ", True, red)
        scrSC.blit(text_surface, (scw // 2 - 500, sch // 2 - 70))


        scrSC.blit(background, (0, 0))






        if box1.collidepoint((virtual_mx, virtual_my)):
            startv = start2
        else:
            startv = start

        if box3.collidepoint((virtual_mx, virtual_my)):
            quits = Q2
        else:
            quits = Q1


        if toggle:
            if box2.collidepoint((virtual_mx, virtual_my)):
                hardcore = hardon2
            else:
                hardcore = hardon1
        elif box2.collidepoint((virtual_mx, virtual_my)):
            hardcore = hardoff2
        else:
            hardcore = hardoff1


        if box4.collidepoint((virtual_mx, virtual_my)):
            cons = Q22
        else:
            cons = Q12



        t = pygame.time.get_ticks() / 1000 
        alpha = int((math.sin(t * 2) + 1) / 2 * 255)  



        font = pygame.font.Font(r"textures\Minecraft.ttf", 40)
        text_surface = font.render("ONLY in 1080p :)", True, Yellow)


        text_surface = pygame.transform.rotate(text_surface, 30)
        text_surface = text_surface.convert_alpha()



        text_surface.set_alpha(alpha)


        text_rect = text_surface.get_rect(center=(scw // 2 + 400, 150))




        scrSC.blit(text_surface, text_rect)


        scrSC.blit(quits, (scw//2 - sizew//2, 700))

        
        scrSC.blit(cons, (scw//2 + 20, 700))


        scrSC.blit(hardcore, (scw//2 - sizew//2, 575))


        scrSC.blit(startv, (scw//2 - sizew//2, 450))


        clock.tick(60)
        scalesurface = pygame.transform.smoothscale(scrSC, (var1, var2))
        screen.blit(scalesurface, (0,0))
        pygame.display.update()
    if not dead and hardc1:
        toggle = True






    if superstart and toggle and (dead or hardc1 == False):
        level1s = True
        
    else:
        level1s = False





    return superstart, toggle, level1s