import pygame, random

width = 1900 #Largura Janela
height = 1000 #Altura Janela

#ESC FECHA O JOGO
#SETA PRA CIMA ANDA COM O CENÁRIO E COMEÇA O JOGO (alterar no uptade)



def load():
    global background, montanha, skins_asadelta, objetos, obj_img #imgs
    global background_largura #tamanho das imagens
    global px_fundo, px_montanha, anda #anda com o cenario
    global vel_fundo, vel_montanha
    global x_pers, y_pers, x_obj, y_obj
    global clock, tempo


    tempo = 0
    
    anda = False
    px_fundo = -1500
    px_montanha = 100
    x_pers = 400
    y_pers = 400

    x_obj = -1
    y_obj = random.randint(0,height)


    vel_fundo = 0.05
    vel_montanha = 0.1

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

    obj_img = [objetos[random.randint(0,len(objetos))]]
    clock = pygame.time.Clock()

    

def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def spawn_obj():
    global objetos, x_obj,y_obj, tempo, obj_img
    obj_pos = [(x_obj,y_obj)]
    if (x_obj < 0):
        i = random.randint(0,len(objetos)-1)
        obj_img[0] = objetos[i]
        x_obj = width + 100
        y_obj = random.randint(100,height-250)
        obj_pos[0] =(x_obj,y_obj)
        
    screen.blit(obj_img[0],obj_pos[0])
    

def draw_screen(screen):
    screen.blit(background,(px_fundo,0)) #printa o fundo
    screen.blit(montanha,(px_montanha,400))
    screen.blit(skins_asadelta[1],(x_pers,y_pers))
    spawn_obj()
    

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    a=0

def update(dt):
    global px_fundo, px_montanha, y_pers, tempo, x_obj
    global anda
    global audio
    k = pygame.key.get_pressed()

    if k[pygame.K_SPACE]:
        anda = True
        pygame.mixer.music.load("musica.fundo.mp3")
        pygame.mixer.music.play()

    if k[pygame.K_m]:
        pygame.mixer.music.pause()

    if k[pygame.K_c]:
        pygame.mixer.music.unpause()

           
    if anda:
        if px_fundo > (background_largura * -1) + width:
            px_fundo -= (vel_fundo * dt)
            px_montanha -=  (vel_montanha * dt)
            x_obj -= (0.9 * dt)
        else:
            px_fundo = -8

        if k[pygame.K_UP]:
            y_pers = y_pers - (0.2 * dt)
            

        if k[pygame.K_DOWN]:
            y_pers = y_pers + (0.2 * dt)

    
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
pygame.quit()
