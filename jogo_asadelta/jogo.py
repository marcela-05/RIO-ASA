'''import pygame
width = 1900 #Largura Janela
height = 1000 #Altura Janela
BLACK = 0,0,0

def draw_screen(screen):'''

import pygame, random

width = 1900 #Largura Janela
height = 1000 #Altura Janela

def load():
    global background, montanha, skins_asadelta, objetos, obj_img, obj_pos #imgs
    global background_largura #tamanho das imagens
    global px_fundo, px_montanha, anda #anda com o cenario
    global vel_fundo, vel_montanha, vel_obj, n_obj
    global x_pers, y_pers, x_obj, y_obj
    global clock, tempo, cons
    global som, pausa, play, mudo, musica, continuacao, fonte, pontuacao

    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)
    pontuacao = 0

    n_obj = 10

    tempo = 0
    
    anda = False
    px_fundo = -1500
    px_montanha = 100
    x_pers = 400
    y_pers = 400

    vel_fundo = 0.05
    vel_montanha = 0.1
    vel_obj = 0.6

    background = pygame.image.load("background.png") #carrega o fundo
    background_largura = background.get_width()
    montanha = pygame.image.load("montanha.png") #carrega a montanha

    skins_asadelta = []
    for i in range(4):
        skins_asadelta.append(pygame.image.load("asadelta_" + str(i) + ".png"))

    objetos = []
    for i in range(9):
        img = (pygame.image.load("obj_" + str(i) + ".png"))
        objetos.append(pygame.transform.scale(img, (img.get_width()/3,img.get_height()/3)))

    obj_pos = []   
    obj_img = [] 
    cons = [] 
    for i in range(n_obj):
        obj_img.append(objetos[random.randint(0,len(objetos)-1)])
        x_obj = width + 100
        y_obj = random.randint(0,height)
        obj_pos.append((x_obj,y_obj))
        cons.append(0)

    clock = pygame.time.Clock()

    som = (pygame.image.load("som laranja.png"))

    mudo = (pygame.image.load("mudo laranja.png"))

    pausa = (pygame.image.load("pausa laranja.png"))

    play = (pygame.image.load("play laranja.png"))


    musica = True
    continuacao = True

def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def spawn_obj():
    global objetos, x_obj,y_obj, tempo, obj_img, obj_pos, cons
    
    for k in range(len(obj_img)):
        if (obj_pos[k][0] < 0):
            i = random.randint(0,len(objetos)-1)
            obj_img[k] = objetos[i]
            obj_pos[k] = (x_obj + (850*k) + cons[k],random.randint(100,height-250))
            cons[k] += width + 150
        obj_pos[k] = (x_obj + (800*k) + cons[k],obj_pos[k][1])
        screen.blit(obj_img[k],obj_pos[k])
    
def draw_screen(screen):
    global pontuacao

    k = pygame.key.get_pressed()

    screen.blit(background,(px_fundo,0)) #printa o fundo
    screen.blit(montanha,(px_montanha,400))

    pont = fonte.render("PONTUAÇÃO: %s" % (str(pontuacao)), False, 	(0, 0, 0))
    screen.blit(pont,(300,150))
    
    if musica:
        som2= pygame.transform.scale(som, (som.get_width()/4,som.get_height()/4))

        screen.blit(som2, (1450, 110))
    else:
        mudo2= pygame.transform.scale(mudo, (mudo.get_width()/4,mudo.get_height()/4))

        screen.blit(mudo2, (1450, 110))

    if continuacao:
        pausa2= pygame.transform.scale(pausa, (pausa.get_width()/6,pausa.get_height()/6))

        screen.blit(pausa2, (1350, 130))
    else:
        play2= pygame.transform.scale(play, (play.get_width()/6,play.get_height()/6))

        screen.blit(play2, (1350, 130))

    skin = skins_asadelta[1]

    if k[pygame.K_UP]:
       skin =  pygame.transform.rotate(skins_asadelta[1], 5)
    if k[pygame.K_DOWN]:
       skin  =  pygame.transform.rotate(skins_asadelta[1], -12)
    
    screen.blit(skin,(x_pers,y_pers))

    spawn_obj()
    

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica, continuacao

    if mouse_buttons[0]:
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

        if check_click(1350, 130, 80, 80, px_mouse, py_mouse):
            continuacao = not continuacao


def update(dt):
    global px_fundo, px_montanha, y_pers, tempo, x_obj, vel_obj, pontuacao
    global anda

    k = pygame.key.get_pressed()

    if k[pygame.K_SPACE]:
        anda = True
        pygame.mixer.music.load("musica.fundo.mp3")
        pygame.mixer.music.play()

    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    if continuacao:
        anda = True
    else:
        anda = False
        pygame.mixer.music.pause()
             
    if anda:
        if px_fundo > (background_largura * -1) + width:
            px_fundo -= (vel_fundo * dt)
            px_montanha -=  (vel_montanha * dt)
            x_obj -= (vel_obj * dt)
        else:
            px_fundo = -8

        if k[pygame.K_UP]:
            y_pers = y_pers - (0.2 * dt)
            
        if k[pygame.K_DOWN]:
            y_pers = y_pers + (0.2 * dt)
        
        pontuacao += round((0.1 * dt)/4)

    

    
def main_loop(screen):
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: #esc fecha o jogo
                    pygame.quit()
                    return
                
        draw_screen(screen)

        clock.tick(120)        
        dt = clock.get_time()

        update(dt)

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()

#exec(start)
'''
def main_loop(screen):
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                break
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_buttons = pygame.mouse.get_pressed()
                px_mouse, py_mouse = pygame.mouse.get_pos()
                mouse_click_down(px_mouse, py_mouse, mouse_buttons)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE: #esc fecha o jogo
                    pygame.quit()
                    return
                
        draw_screen(screen)

        clock.tick(60)        
        dt = clock.get_time()

        update(dt)

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()'''
