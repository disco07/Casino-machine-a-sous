# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 20:21:45 2020

@author: D Koné
"""

import numpy as np
import pygame

pygame.init()
pygame.display.set_caption('Machine à sous')
screen = pygame.display.set_mode((800, 400))
background = pygame.image.load("images/slot.png")
color_background_white = [255, 255, 255]
image_ananas = pygame.image.load("images/ananas.png")
image_cerise = pygame.image.load("images/cerise.png")
image_orange = pygame.image.load("images/orange.png")
image_pasteque = pygame.image.load("images/pasteque.png")
image_pomme_dore = pygame.image.load("images/pomme_dore.png")


welcome = "Bienvenue sur la machine à sous GravenFruitiiii"
liste_fruit = ["ananas", "cerise", "orange", "pasteque", "pomme_dore"]
fruit_image_dict = {"ananas": image_ananas, "cerise": image_cerise, 
               "orange": image_orange, "pasteque": image_pasteque, 
               "pomme_dore": image_pomme_dore}
coins = 1000
choix_fruit = ["ananas", "cerise", "orange"]
def lancement(liste_fruit):
    global coins
    global choix_fruit
    choix_fruit = np.random.choice(liste_fruit, 3, p=[0.40, 0.25, 0.20, 0.10, 0.05])
    if choix_fruit[0] == choix_fruit[1] == choix_fruit[2] == liste_fruit[0]:
        coins += 5
    elif choix_fruit[0] == choix_fruit[1] == choix_fruit[2] == liste_fruit[1]:
        coins += 15
    elif choix_fruit[0] == choix_fruit[1] == choix_fruit[2] == liste_fruit[2]:
        coins += 50
    elif choix_fruit[0] == choix_fruit[1] == choix_fruit[2] == liste_fruit[3]:
        coins += 150
    elif choix_fruit[0] == choix_fruit[1] == choix_fruit[2] == liste_fruit[4]:
        coins += 10000
    
current_image = 0
image1 = image_ananas
image2 = image_cerise
image3 = image_orange
animate = False
def animation():
    if animate:
        global current_image
        global image1
        global image2
        global image3
        current_image += 0.5
        if current_image >= len(liste_fruit):
            current_image = 0
        image3 = fruit_image_dict[liste_fruit[int(current_image)]]
        image1 = fruit_image_dict[liste_fruit[int(current_image)]]
        image2 = fruit_image_dict[liste_fruit[int(current_image)]]

    

running = True
font = pygame.font.Font('freesansbold.ttf', 25)
color_font_black = [0, 0, 0, 0]
count = 0

while running:
    text_surface = font.render(str(coins) + " Jeton(s)", True, color_font_black)
    animation()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and coins >= 10:
                animate = True
                lancement(liste_fruit)
                coins -= 10

    if animate:
        if count <= 20:
            count += 1
            if count == 20:
                count = 0
        if count == 0:
            animate = False
            image1 = fruit_image_dict[choix_fruit[0]]
            image2 = fruit_image_dict[choix_fruit[1]]
            image3 = fruit_image_dict[choix_fruit[2]]
               
    screen.fill(color_background_white)
    screen.blit(background, (0, 0))
    screen.blit(text_surface, (0, 0))
    screen.blit(image1, (226, 250))
    screen.blit(image2, (327, 250))
    screen.blit(image3, (428, 250))

    pygame.display.flip()