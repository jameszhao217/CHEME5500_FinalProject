# -*- coding: utf-8 -*-
"""
Created on Sat May 05 10:00:32 2018

@author: MZ
"""

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
