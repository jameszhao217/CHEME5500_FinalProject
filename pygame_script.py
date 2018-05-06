# -*- coding: utf-8 -*-

import pygame

# PyGame Tutorial Reference: 
# https://pythonprogramming.net/pygame-buttons-part-1-button-rectangle/

def pygame_plot():
    
    pygame.init()
    
    # Size of Display
    display_width = 800
    display_height = 600
    
    # Color rgb
    black = (0,0,0)
    white = (255,255,255)
    red = (200,0,0)
    green = (0,200,0)
    
    bright_red = (255,0,0)
    bright_green = (0,255,0)
    
    # Set display
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    clock = pygame.time.Clock()
    
    # Name program
    pygame.display.set_caption('Beam Deflection')
    
    # load Deflection Curve
    defl_shape = pygame.image.load('deflection.png')
    
    # Define the location where the curve is plotted
    def defl_location(x,y):
        gameDisplay.blit(defl_shape,(x,y))
    
    # Define the font of text displayed
    def text_objects(text,font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
        
    # def message_display(text):
    #    largeText = pygame.font.Font('freesansbold.ttf',115)
    #    TextSurf, TextRect = text_objects(text, largeText)    
    #    TextRect.center = ((display_width/2),(display_height/2))
    #    gameDisplay.blit(TextSurf, TextRect)
    #    pygame.display.update
    #    time.sleep(2)
    #    game_loop()
    
    # Game Start Menu    
    def game_intro():
        
        intro = True
        
        while intro:
    
            event = pygame.event.poll()
            if event.type == pygame.QUIT:            
                pygame.quit()
                break

#            for event in pygame.event.get():
#                
#                if event.type == pygame.QUIT:
#                    intro = False
#                    pygame.quit()                
#                    break
        
            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',55)
            TextSurf, TextRect = text_objects('Beam Deflection Curve Fun', largeText)    
            TextRect.center = ((display_width/2),(display_height/3))
            gameDisplay.blit(TextSurf, TextRect)

            mouse = pygame.mouse.get_pos()
            print(mouse)

            if (display_width/2)+100 > mouse[0] > (display_width/2)-100 and (3*display_height/5) + 50 > mouse[1] > (3*display_height/5):
                pygame.draw.rect(gameDisplay, bright_green, ((display_width/2)-100,(3*display_height/5),200,50))
            else:
                pygame.draw.rect(gameDisplay, green, ((display_width/2)-100,(3*display_height/5),200,50))
            
            if (display_width/2)+100 > mouse[0] > (display_width/2)-100 and (3*display_height/5) + 150 > mouse[1] > (3*display_height/5)+100:
                pygame.draw.rect(gameDisplay, bright_red, ((display_width/2)-100,(3*display_height/5)+100,200,50))
            else:
                pygame.draw.rect(gameDisplay, red, ((display_width/2)-100,(3*display_height/5)+100,200,50))


            pygame.display.update()
            clock.tick(15)        
#            game_loop()    

    def game_loop():
            
        x = (display_width * 0.25)
        y = (display_height * 0.5)
          
        game_exit = False
        
        while not game_exit:
    
            event2 = pygame.event.poll()
            if event2.type == pygame.QUIT:
                pygame.quit()
                game_exit = True
                break
            
    #        for event in pygame.event.get():
    #            if event.type == pygame.QUIT:
    ##                game_exit = True
    #                pygame.quit()
    #                break
            
            gameDisplay.fill(white)
            defl_location(x,y)
            pygame.display.update()
            clock.tick(60)
        
        
    
    # Run game
    game_intro()
    #game_loop()
    #
    #pygame.quit()
    #break
