# -*- coding: utf-8 -*-

import pygame
import sys

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
#    clock = pygame.time.Clock()
    
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
        
    # Define GUI button function
    def button(msg,x,y,w,h,low_color,high_color,action = None):
            
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w/2 > mouse[0] > x-w/2 and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, low_color, (x-w/2,y,w,h))
            if click[0] == 1 and action != None:
                if action == 'Play':
                    game_loop()
                elif action == 'Quit':
                    pygame.quit()
                    sys.exit()         
        else:
            pygame.draw.rect(gameDisplay, high_color, (x-w/2,y,w,h))
        
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( x, y + h/2)
        gameDisplay.blit(textSurf, textRect)
        
    # Game Start Menu    
    def game_intro():
        
        intro = True
        
        while intro:
    
            event = pygame.event.poll()
            if event.type == pygame.QUIT:            
                intro = False
                pygame.quit()
                sys.exit()

            gameDisplay.fill(white)
            largeText = pygame.font.Font('freesansbold.ttf',40)
            TextSurf, TextRect = text_objects('Beam Deflection Curve Fun', largeText)    
            TextRect.center = ((display_width/2),(display_height/3))
            gameDisplay.blit(TextSurf, TextRect)

            button('YES PLEASE',(display_width/2),3*display_height/5,200,50,bright_green,green,'Play')            
            button('Nevermind',(display_width/2),3*display_height/5+100,200,50,bright_red,red,'Quit')
            
            pygame.display.update()

    # Display Deflection Curve to Window   
    def game_loop():
            
        x = (display_width * 0.25)
        y = (display_height * 0.3)
          
        game_exit = False
        
        while not game_exit:
    
            event2 = pygame.event.poll()
            if event2.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
                sys.exit()
            
            gameDisplay.fill(white)
            defl_location(x,y)
            pygame.display.update()
    
    # Run game
    game_intro()

    # Terminate Pygame
    pygame.quit()
