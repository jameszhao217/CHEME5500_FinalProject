# -*- coding: utf-8 -*-

############## M.Z. added pygame plot ##############

import pygame
import sys

# PyGame Tutorial Reference: 
# https://pythonprogramming.net/pygame-buttons-part-1-button-rectangle/

def pygame_plot(max_defleciton,max_location,defl_point,location_point):
    
    # Initialize PyGame
    pygame.init()
    
    # Size of Display
    display_width = 800
    display_height = 450
    
    # Set Color (rgb)
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    blue = (65,105,225)
    bright_red = (255,99,71)
    bright_blue = (30,144,255)
    
    # Set display
    gameDisplay = pygame.display.set_mode((display_width,display_height))
    
    # Name program
    pygame.display.set_caption('Beam Deflection')
    
    # load Deflection Curve
    defl_shape = pygame.image.load('deflection.png')
    
    # Load Background
    bkgroud = pygame.image.load('background.png')
    
    # Define the location where the curve is plotted
    def defl_location(x,y):
        gameDisplay.blit(defl_shape,(x,y))
    
    # Define the font of text displayed
    def text_objects(text,font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
        
    # Define GUI button function
    def button(msg,x,y,w,h,low_color,high_color,action = None):
            
        # Obtain mouse positions and actions
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Define Buttons and Events
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
        
        # Display words on buttons
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( x, y + h/2)
        gameDisplay.blit(textSurf, textRect)

    ####### Game Start Menu #######    
    def game_intro():
        
        intro = True
        
        while intro:
    
            event = pygame.event.poll()
            if event.type == pygame.QUIT:            
                intro = False
                pygame.quit()
                sys.exit()

            # Set up start up page
            gameDisplay.fill(white)
            gameDisplay.blit(bkgroud,(0,0))
            largeText = pygame.font.Font('freesansbold.ttf',50)
            TextSurf, TextRect = text_objects('Beam Deflection Curve Fun', largeText)    
            TextRect.center = ((display_width/2),(display_height/3))
            gameDisplay.blit(TextSurf, TextRect)
            
            # set buttons
            button('Reveal the Deflected Shape?',(display_width/3),3*display_height/5,300,50,bright_blue,blue,'Play')            
            button('Nevermind ...',(display_width/3),3*display_height/5+75,300,50,bright_red,red,'Quit')
            
            pygame.display.update()

    # Display Deflection Curve to Window   
    def game_loop():
        
        # Location of Deflection curve
        x = (display_width * 0.25)
        y = (display_height * 0.30)
          
        game_exit = False
        
        while not game_exit:
    
            event2 = pygame.event.poll()
            if event2.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
                sys.exit()
            
            gameDisplay.fill(white)
            
            # Display Command Window Outputs
            mediumText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects('Max Deflection = %6.2f (in) at x = %6.2f (ft)' % (max_defleciton,max_location), mediumText)    
            TextRect.center = ((display_width/2),(display_height/8))
            gameDisplay.blit(TextSurf, TextRect)
            TextSurf2, TextRect2 = text_objects('Deflection = %6.2f (in) at x = %6.2f (ft)' % (defl_point,location_point), mediumText)    
            TextRect2.center = ((display_width/2),(display_height/8)+30)
            gameDisplay.blit(TextSurf2, TextRect2)

            # Show deflection curve
            defl_location(x,y)
            
            # Set up Quit button
            button('Thank you!',(9*display_width/10),7*display_height/8,150,40,bright_red,red,'Quit')
            pygame.display.update()
            
    # Run game
    game_intro()

    # Terminate Pygame
    pygame.quit()
