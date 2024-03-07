import pygame
import sys
import random

pantalla_x = 500
pantalla_y = 350
size = (pantalla_x,pantalla_y)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mi primer juego')
color_rojo = (255,0,0)
color_verde = (0,255,0)
color_azul = (0,0,255)
color_blanco = (255,255,255)
color_negro = (0,0,0)
cordenadas = []
cordenadas1 = []
cordenadas2 = []
fps = 15
clock = pygame.time.Clock()
puntos = 0
vidas = 3
done = True
nivel = 1
font = pygame.font.Font(None,30)
for x in range(10):
    x = random.randint(0,pantalla_x - 20)
    y = random.randint(0,100)
    cordenadas.append([x,y,20,20])
for x in range(10):
    x = random.randint(0,pantalla_x - 20)
    y = random.randint(0,100)
    cordenadas1.append([x,y,20,20])
for x in range(10):
    x = random.randint(0,pantalla_x - 20)
    y = random.randint(0,100)
    cordenadas2.append([x,y,20,20])

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = event.pos
            #x , y = (256,500)
            #x = 256
            #y = 500
            if nivel == 1:
                for cor in cordenadas:
                    if pygame.draw.rect(screen,color_rojo,cor).collidepoint(x,y):
                        cordenadas.remove(cor)
                        puntos += 5
            if nivel == 2:
                for cor in cordenadas1:
                    if pygame.draw.rect(screen,color_rojo,cor).collidepoint(x,y):
                        cordenadas1.remove(cor)
                        puntos += 5
            if nivel == 3:
                for cor in cordenadas2:
                    if pygame.draw.rect(screen,color_rojo,cor).collidepoint(x,y):
                        cordenadas2.remove(cor)
                        puntos += 5

    if (len(cordenadas) == 0 and nivel == 1):
        nivel +=1
        fps += 15
    if len(cordenadas1) == 0 and nivel == 2:
        nivel += 1
        fps += 15

    screen.fill(color_blanco)
    screen_rect = screen.get_rect()
    texto = font.render('Vidas: '+str(vidas)+' Puntos: '+str(puntos),True,color_negro)
    texto_rect = texto.get_rect()
    texto_rect.center = screen_rect.center
    texto_x = texto_rect[0]
    screen.blit(texto,[texto_x,0,176,21])

    if vidas > 0:
        if nivel == 1:
            for cor in cordenadas:
                pygame.draw.rect(screen,color_rojo,cor)
                #a.0 - esta x , 1.- y y en 2 y 3 esta ancho y alto
                cor[1] += 1
                if cor[1] > pantalla_y:
                    cor[1] = 0
                    vidas -= 1
                    puntos -= 5
        if nivel == 2:
            for cor in cordenadas1:
                pygame.draw.rect(screen,color_verde,cor)
                #a.0 - esta x , 1.- y y en 2 y 3 esta ancho y alto
                cor[1] += 1
                if cor[1] > pantalla_y:
                    cor[1] = 0
                    vidas -= 1
                    puntos -= 5
        if nivel == 3:
            for cor in cordenadas2:
                pygame.draw.rect(screen,color_azul,cor)
                #a.0 - esta x , 1.- y y en 2 y 3 esta ancho y alto
                cor[1] += 1
                if cor[1] > pantalla_y:
                    cor[1] = 0
                    vidas -= 1
                    puntos -= 5
    else:
        texto_final = font.render("GAME OVER", True, color_negro)
        texto_final_rect = texto_final.get_rect()
        texto_final_rect.center = screen_rect.center
        screen.blit(texto_final,texto_final_rect)

    pygame.display.flip()
    clock.tick(fps)
sys.exit()
