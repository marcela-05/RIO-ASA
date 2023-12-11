import pygame, random, math, time

width = 1900 #Largura Janela
height = 1000 #Altura Janela

def load():
    global tela, background, montanha, skin, skin_mask, objetos, obj_img, obj_masks, obj_pos, logo, top, seta, over, setaAlta, setaBaixo,espaco,tutorial#imgs
    global background_largura #tamanho das imagens
    global px_fundo, px_montanha, anda #anda com o cenario
    global vel_fundo, vel_montanha, vel_obj, n_obj
    global x_pers, y_pers, x_obj, y_obj, colisao
    global clock, tempo, cons
    global som, pausa, play, mudo, musica, continuacao, fonte, pontuacao, fonte2
    global arq_rank, ranking

    fonte = pygame.font.Font(pygame.font.get_default_font(), 50)
    fonte2 = pygame.font.Font(pygame.font.get_default_font(), 20)
    pontuacao = 0
    tela = 'menu'

    ranking = []
    arq_rank = open("ranking.txt","r")
    for pont in arq_rank:
        ranking.append(int(pont))
    arq_rank.close()

    tempo = 0
    
    anda = False
    colisao = False
    px_fundo = -1500
    px_montanha = 100
    continuacao = False
    x_pers = 400
    y_pers = 400

    vel_fundo = 0.05
    vel_montanha = 0.1
    vel_obj = 0.2

    background = pygame.image.load("background.png") #carrega o fundo
    logo = pygame.image.load("logo.png")
    tutorial = pygame.image.load("tutorial.png")
    background_largura = background.get_width()
    montanha = pygame.image.load("montanha.png") #carrega a montanha

    
    skin = pygame.image.load("asadelta_1.png")
    skin_mask = pygame.mask.from_surface(skin)

    objetos = []
    obj_masks = []

    for i in range(28):
        img = (pygame.image.load("obj_" + str(i) + ".png"))
        objetos.append(pygame.transform.scale(img, (img.get_width()/3,img.get_height()/3)))

    n_obj = len(objetos)
    obj_pos = []   
    obj_img = [] 
    cons = [] 
    for i in range(n_obj):
        a = random.randint(0,len(objetos)-1)
        obj_img.append(objetos[a])
        obj_masks.append(pygame.mask.from_surface(objetos[a]))
        x_obj = -10
        y_obj = random.randint(0,height)
        obj_pos.append((x_obj,y_obj))
        cons.append(0)

    clock = pygame.time.Clock()

    som = (pygame.image.load("Sound.png"))
    mudo = (pygame.image.load("mute.png"))
    pausa = (pygame.image.load("Pause.png"))
    play = (pygame.image.load("Play.png"))
    top = (pygame.image.load("top5.png"))
    seta = (pygame.image.load("seta.png"))
    over = (pygame.image.load("game over.png"))
    espaco = (pygame.image.load("espaco.png"))
    setaBaixo = (pygame.image.load("setaBaixo.png"))
    setaAlta = (pygame.image.load("setaAlta.png"))
    
    pygame.mixer.music.load("musica.fundo.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
    musica = True

def check_click(x1,y1,w1,h1,x2,y2):
    return x1 < x2+1 and x2 < x1+w1 and y1 < y2+1 and y2 < y1+h1

def spawn_obj():
    global objetos, x_obj,y_obj, tempo, obj_img, obj_pos, cons, skin, colisao, x_pers, y_pers, skin_mask, obj_masks
    
    for k in range(len(obj_img)):
        if (obj_pos[k][0] < 0):
            i = random.randint(0,len(objetos)-1)
            obj_img[k] = objetos[i]
            obj_masks[k] = pygame.mask.from_surface(objetos[i])
            obj_pos[k] = (x_obj + (850*k) + cons[k],random.randint(100,height-250))
            cons[k] += width + 150
        obj_pos[k] = (x_obj + (800*k) + cons[k],obj_pos[k][1])
        screen.blit(obj_img[k],obj_pos[k])


        if skin_mask.overlap(obj_masks[k], (obj_pos[k][0] - x_pers, obj_pos[k][1] - y_pers)):
            colisao = True

def jogo():
    global pontuacao, skin, skin_mask,y_pers
    k = pygame.key.get_pressed()

    screen.blit(background,(px_fundo,0)) #printa o fundo
    screen.blit(montanha,(px_montanha,400))

    pont = fonte.render("PONTUAÇÃO: %s" % (str(pontuacao)), False, (255, 212, 89))
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

    skin = pygame.image.load("asadelta_1.png")
    skin_mask = pygame.mask.from_surface(skin)

    if k[pygame.K_UP]:
       skin =  pygame.transform.rotate(skin, 5)
       skin_mask = pygame.mask.from_surface(skin)

    if k[pygame.K_DOWN]:
       skin  =  pygame.transform.rotate(skin, -12)
       skin_mask = pygame.mask.from_surface(skin)
    
    screen.blit(skin,(x_pers,y_pers))

    spawn_obj()

def resetajogo():
    global px_montanha, continuacao, x_obj,pontuacao, colisao, y_pers, cons, obj_pos, vel_obj
    
    vel_obj = 0.2
    y_pers = 400
    colisao = False
    pontuacao = 0
    px_montanha = 100
    continuacao = False
    for k in range(len(obj_img)):
        obj_pos[k] = (-10,0)

def menu():
    screen.blit(background,(px_fundo,0)) #printa o fundo

    creditos = fonte2.render("Feito por Guilherme Cunha e Marcela Issa", False,(255, 212, 89))
    screen.blit(creditos,(200,100))
    
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

def intro():
    screen.blit(background,(px_fundo,0)) #printa o fundo
    
    setaAlta2= pygame.transform.scale(setaAlta, (setaAlta.get_width()/2,setaAlta.get_height()/2))
    screen.blit(setaAlta2, (400, 400))
    
    alto = fonte.render("Para a asa delta subir", False,(255, 212, 89))
    screen.blit(alto,(570,425))

    setaBaixo2= pygame.transform.scale(setaBaixo, (setaBaixo.get_width()/2,setaBaixo.get_height()/2))
    screen.blit(setaBaixo2, (400, 550))
    
    baixo = fonte.render("Para a asa delta descer", False,(255, 212, 89))
    screen.blit(baixo,(570,575))
    
    espaco2= pygame.transform.scale(espaco, (espaco.get_width()/2,espaco.get_height()/2))
    screen.blit(espaco2, (400, 700))
    
    iniciar = fonte.render("Para iniciar o jogo", False,(255, 212, 89))
    screen.blit(iniciar,(700,710))

    pular = fonte.render("PULAR", False,(255, 212, 89))
    screen.blit(pular,(1400,800))
    
    screen.blit(tutorial,(660,200))

    if musica:
        som2= pygame.transform.scale(som, (som.get_width()/4,som.get_height()/4))

        screen.blit(som2, (1450, 110))
    else:
        mudo2= pygame.transform.scale(mudo, (mudo.get_width()/4,mudo.get_height()/4))

        screen.blit(mudo2, (1450, 110))

def top5():
    global ranking
    screen.blit(background,(px_fundo,0)) #printa o fundo

    primeiro = fonte.render("1º) %s" % (str(ranking[0])), False,(255, 212, 89))
    screen.blit(primeiro,(500,400))
    
    segundo =  fonte.render("2º) %s" % (str(ranking[1])), False,(255, 212, 89))
    screen.blit(segundo,(500,480))

    terceiro = fonte.render("3º) %s" % (str(ranking[2])), False,(255, 212, 89))
    screen.blit(terceiro,(500,560))
    
    quarto = fonte.render("4º) %s" % (str(ranking[3])), False,(255, 212, 89))
    screen.blit(quarto,(500,640))
    
    quinto = fonte.render("5º) %s" % (str(ranking[4])), False,(255, 212, 89))
    screen.blit(quinto,(500,720))

    top2 = pygame.transform.scale(top, (top.get_width()/1.2,top.get_height()/1.2))
    screen.blit(top2,(670,150))
    
    seta2= pygame.transform.scale(seta, (seta.get_width()/4,seta.get_height()/4))
    screen.blit(seta2,(300,125))

def gameover():
    screen.blit(background,(px_fundo,0)) #printa o fundo
    pont = fonte.render("PONTUAÇÃO: %s" % (str(pontuacao)), False,(255, 212, 89))
    screen.blit(pont,(675,450))
    nov = fonte.render("JOGAR NOVAMENTE", False,(255, 212, 89))
    screen.blit(nov,(680,550))
    saida = fonte.render("SAIR", False,(255, 212, 89))
    screen.blit(saida,(860,650))
    screen.blit(over,(600,250))

def atualizaranking():
    ranking.append(pontuacao)
    ranking.sort(reverse=True)
    ranking.pop(5)
    arq_rank = open("ranking.txt","w")
    for i in range(0,5):
        arq_rank.write("%d\n" % ranking[i])
    arq_rank.close()

def draw_screen(screen):
    global tela, px_fundo, px_montanha

    if tela == 'menu':
        menu()
    elif tela == 'intro':
        intro()
    elif tela == 'jogo':
        jogo()
    elif tela == 'top 5':
        top5()
    elif tela =='game over':
        gameover()

def mouse_click_down(px_mouse, py_mouse, mouse_buttons):
    global musica, continuacao, tela

    if mouse_buttons[0]:
        if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
            musica = not musica

        if check_click(1350, 130, 80, 80, px_mouse, py_mouse):
            continuacao = not continuacao
    
    if tela == 'menu':
        if mouse_buttons[0]:
            if check_click(855,480, 200, 80, px_mouse, py_mouse):
                resetajogo()
                tela = 'intro'

            if check_click(870, 560, 150, 80, px_mouse, py_mouse):
                tela = 'top 5'

            if check_click(880,640, 100, 80, px_mouse, py_mouse):
                pygame.quit()

    if tela == 'intro':
        if mouse_buttons[0]:
            if check_click(1400,800, 150, 80, px_mouse, py_mouse):
                resetajogo()
                tela = 'jogo'
                
    if tela == 'top 5':
        if mouse_buttons[0]:
            if check_click(300,125, 80, 80, px_mouse, py_mouse): 
                tela = 'menu'
    
    if tela =='game over':
        if mouse_buttons[0]:
            if check_click(650,550, 600, 80, px_mouse, py_mouse):
                resetajogo()
                tela = 'jogo'
            if check_click(860,650, 200, 80, px_mouse, py_mouse):
                tela = 'menu'
            if check_click(1450, 110, 90, 80, px_mouse, py_mouse):
                musica = not musica


def update(dt):
    global px_fundo, px_montanha, y_pers, tempo, x_obj, vel_obj, pontuacao, continuacao, tela
    global anda, vel_obj

    k = pygame.key.get_pressed()
        
    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
    if continuacao:
        anda = True
    else:
        anda = False
        pygame.mixer.music.pause()

    if colisao and tela == 'jogo':
        atualizaranking()
        tela = 'game over'
        
    if tela == 'jogo':
        if k[pygame.K_SPACE]:
            continuacao = True
    
        if anda:
            vel_obj += 0.0002
            if px_fundo > (background_largura * -1) + width:
                px_fundo -= (vel_fundo * dt)
                px_montanha -=  (vel_montanha * dt)
                x_obj -= (vel_obj * dt)
            else:
                px_fundo = -8

            if k[pygame.K_UP]:
                y_pers = max(0, y_pers - (0.2 * dt))
                
            if k[pygame.K_DOWN]:
                y_pers = min(height - skin.get_height(), y_pers + (0.2 * dt))
            pontuacao += round((0.1 * dt)/4)
    else:
        if px_fundo > (background_largura * -1) + width:
                px_fundo -= (vel_fundo * dt)
        else:
            px_fundo = -8

    if musica:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

    
def main_loop(screen):
    global tela
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
                if e.key == pygame.K_ESCAPE:
                    tela = 'menu'
            elif e.type == pygame.USEREVENT + 1:  # Event for music end
                pygame.mixer.music.play()
                
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
