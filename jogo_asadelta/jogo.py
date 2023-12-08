#MENU
'''
import pygame
width = 1900 #Largura Janela
height = 1000 #Altura Janela
BLACK = 0,0,0

def load():
    global background
    global background_largura #tamanho das imagens
    global px_fundo,fonte
    global som, mudo, musica, logo

    background = pygame.image.load("background.png") #carrega o fundo
    background_largura = background.get_width()
    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)


    pygame.mixer.music.load("musica.fundo.mp3")
    pygame.mixer.music.play()
    px_fundo=-1500
    musica = True
    som = (pygame.image.load("Sound.png"))
    logo = (pygame.image.load("logo.png"))

    mudo = (pygame.image.load("mute.png"))
def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica

    if mouse_buttons[0]:
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

def draw_screen(screen):
    screen.blit(background,(px_fundo,0)) #printa o fundo

    comeco = fonte.render("INICIAR", False,(255, 212, 89))
    screen.blit(comeco,(855,480))

    rank = fonte.render("TOP 5", False,(255, 212, 89))
    screen.blit(rank,(870,560))

    sair = fonte.render("SAIR", False,(255, 212, 89))
    screen.blit(sair,(880,640))

    screen.blit(logo,(560,250))

    if musica:
        som2= pygame.transform.scale(som, (som.get_width()/4,som.get_height()/4))

        screen.blit(som2, (1450, 110))
    else:
        mudo2= pygame.transform.scale(mudo, (mudo.get_width()/4,mudo.get_height()/4))

        screen.blit(mudo2, (1450, 110))

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):

    if mouse_buttons[0]:
        if check_click(855,480, 200, 80, px_mouse, py_mouse):
            pygame.quit()

        if check_click(870, 560, 150, 80, px_mouse, py_mouse):
            pygame.quit()

        if check_click(880,640, 100, 80, px_mouse, py_mouse):
            pygame.quit()

def update():
    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

        
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
        update()

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()

'''
#TOP 5
'''
import pygame
width = 1900 #Largura Janela
height = 1000 #Altura Janela
BLACK = 0,0,0

def load():
    global background
    global background_largura #tamanho das imagens
    global px_fundo,fonte
    global som, mudo, musica, top, seta

    background = pygame.image.load("background.png") #carrega o fundo
    background_largura = background.get_width()
    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)


    pygame.mixer.music.load("musica.fundo.mp3")
    pygame.mixer.music.play()
    px_fundo=-1500
    musica = True
    som = (pygame.image.load("Sound.png"))
    top = (pygame.image.load("top5.png"))
    seta = (pygame.image.load("seta.png"))
    mudo = (pygame.image.load("mute.png"))
    
def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica

    if mouse_buttons[0]:
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

def draw_screen(screen):
    screen.blit(background,(px_fundo,0)) #printa o fundo

    primeiro = fonte.render("1º) Strogonoff", False,(255, 212, 89))
    screen.blit(primeiro,(500,400))

    p1 = fonte.render("Pontuação:10000000", False,(255, 212, 89))
    screen.blit(p1,(950,400))
    
    segundo =  fonte.render("2º) Yakisoba", False,(255, 212, 89))
    screen.blit(segundo,(500,480))

    p2 =  fonte.render("Pontuação:9000000", False,(255, 212, 89))
    screen.blit(p2,(950,480))
    
    terceiro = fonte.render("3º) Cookie", False,(255, 212, 89))
    screen.blit(terceiro,(500,560))

    p3 = fonte.render("Pontuação:800000", False,(255, 212, 89))
    screen.blit(p3,(950,560))
    
    quarto = fonte.render("4º) Poke", False,(255, 212, 89))
    screen.blit(quarto,(500,640))
    
    p4 = fonte.render("Pontuação:700000", False,(255, 212, 89))
    screen.blit(p4,(950,640))
    
    quinto = fonte.render("5º) Bolo de copo", False,(255, 212, 89))
    screen.blit(quinto,(500,720))

    p5 = fonte.render("Pontuação:50000", False,(255, 212, 89))
    screen.blit(p5,(950,720))

    top2 = pygame.transform.scale(top, (top.get_width()/1.2,top.get_height()/1.2))
    screen.blit(top2,(670,150))
    
    seta2= pygame.transform.scale(seta, (seta.get_width()/4,seta.get_height()/4))
    screen.blit(seta2,(300,125))
    
    if musica:
        som2= pygame.transform.scale(som, (som.get_width()/4,som.get_height()/4))

        screen.blit(som2, (1450, 110))
    else:
        mudo2= pygame.transform.scale(mudo, (mudo.get_width()/4,mudo.get_height()/4))

        screen.blit(mudo2, (1450, 110))

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica
    if mouse_buttons[0]:
        if check_click(300,125, 80, 80, px_mouse, py_mouse): #BOTÃO DE VOLTAR, mas agr tá pra sair da tela
            pygame.quit()
            
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

def update():
    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

        
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
        update()

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
'''
#JOGO
''' 
import pygame, random, math

width = 1900 #Largura Janela
height = 1000 #Altura Janela

def load():
    global background, montanha, skins_asadelta, objetos, obj_img, obj_pos #imgs
    global background_largura #tamanho das imagens
    global px_fundo, px_montanha, anda #anda com o cenario
    global vel_fundo, vel_montanha, vel_obj, n_obj
    global x_pers, y_pers, x_obj, y_obj, colisao
    global clock, tempo, cons
    global som, pausa, play, mudo, musica, continuacao, fonte, pontuacao

    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)
    pontuacao = 0

    n_obj = 10

    tempo = 0
    
    anda = False
    colisao = False
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

    som = (pygame.image.load("Sound.png"))

    mudo = (pygame.image.load("mute.png"))

    pausa = (pygame.image.load("Pause.png"))

    play = (pygame.image.load("Play.png"))


    musica = True
    continuacao = True

def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def check_circular_collision(ax, ay, ar, bx, by, br):
   dx = bx - ax
   dy = by - ay
   dist = math.sqrt(dx * dx + dy * dy)
   return dist < ar + br

def spawn_obj():
    global objetos, x_obj,y_obj, tempo, obj_img, obj_pos, cons, skin, colisao, x_pers, y_pers
    
    for k in range(len(obj_img)):
        if (obj_pos[k][0] < 0):
            i = random.randint(0,len(objetos)-1)
            obj_img[k] = objetos[i]
            obj_pos[k] = (x_obj + (850*k) + cons[k],random.randint(100,height-250))
            cons[k] += width + 150
        obj_pos[k] = (x_obj + (800*k) + cons[k],obj_pos[k][1])
        screen.blit(obj_img[k],obj_pos[k])
        if check_circular_collision(x_pers+28, y_pers, 80, obj_pos[k][0], obj_pos[k][1], 40):
            colisao = True
    
def draw_screen(screen):
    global pontuacao, skin

    k = pygame.key.get_pressed()

    screen.blit(background,(px_fundo,0)) #printa o fundo
    screen.blit(montanha,(px_montanha,400))

    pont = fonte.render("PONTUAÇÃO: %s, colisao = %s, y = %f" % (str(pontuacao),colisao,y_pers), False, 	(0, 0, 0))
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

    if colisao:
        anda = False
             
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

'''

#GAME OVER
'''
import pygame
width = 1900 #Largura Janela
height = 1000 #Altura Janela
BLACK = 0,0,0

def load():
    global background
    global background_largura #tamanho das imagens
    global px_fundo,fonte
    global som, mudo, musica, over

    background = pygame.image.load("background.png") #carrega o fundo
    background_largura = background.get_width()
    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)


    pygame.mixer.music.load("musica.fundo.mp3")
    pygame.mixer.music.play()
    px_fundo=-1500
    musica = True
    som = (pygame.image.load("Sound.png"))
    over = (pygame.image.load("game over.png"))

    mudo = (pygame.image.load("mute.png"))
def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica

    if mouse_buttons[0]:
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

def draw_screen(screen):
    screen.blit(background,(px_fundo,0)) #printa o fundo

    #pont = fonte.render("PONTUAÇÃO: %s" % (str(pontuacao)), False,(255, 212, 89))
    #USAR O QUE ESTÁ COMENTADO. Coloquei o pont de baixo só pra testar a pontuação
    pont = fonte.render("PONTUAÇÃO: 1000000", False,(255, 212, 89))
    screen.blit(pont,(655,450))

    nov = fonte.render("JOGAR NOVAMENTE", False,(255, 212, 89))
    screen.blit(nov,(680,550))

    saida = fonte.render("SAIR", False,(255, 212, 89))
    screen.blit(saida,(860,650))


    screen.blit(over,(600,250))

    if musica:
        som2= pygame.transform.scale(som, (som.get_width()/4,som.get_height()/4))

        screen.blit(som2, (1450, 110))
    else:
        mudo2= pygame.transform.scale(mudo, (mudo.get_width()/4,mudo.get_height()/4))

        screen.blit(mudo2, (1450, 110))

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica
    if mouse_buttons[0]:
        if check_click(650,550, 600, 80, px_mouse, py_mouse): #BOTÃO DE JOGAR NOVAMENTE
            #pygame.quit()

        if check_click(860,650, 200, 80, px_mouse, py_mouse):
            pygame.quit()

        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

def update():
    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

        
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
        update()

        pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((width, height))
load()
main_loop(screen)
pygame.quit()
'''
