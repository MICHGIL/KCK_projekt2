import pygame
from pygame.locals import *

(width, height) = (1350,700)
background_colour = (200,200,255)
white = (255,255,255)
white_blur = (127,127,127)
black = (0,0,0)
# black_blur = (0,0,100) # można zrobić dla czarnego inny blur, ale w sumie po co

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PerfectPiano (nope)')
screen.fill(background_colour)
cursor_positions = [[50+0.5*100,150+0.5*400],[155+0.5*75,50+0.5*300],[235+0.5*100,150+0.5*400],[340+0.5*75,50+0.5*300],[420+0.5*100,150+0.5*400],
                            [525+0.5*100,150+0.5*400],[630+0.5*75,50+0.5*300],[710+0.5*100,150+0.5*400],[815+0.5*75,50+0.5*300],[895+0.5*100,150+0.5*400],
                            [1000+0.5*75,50+0.5*300],[1080+0.5*100,150+0.5*400],[1185+0.5*100,150+0.5*400]]
k = 0

def cursor_jump():
    print(pygame.mouse.set_pos(cursor_positions[k]))

def keys (x, y, width, height, inactive_button, active_button, action=None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+width > cursor[0] > x and y+height > cursor[1] > y:
        pygame.draw.rect(screen,active_button,(x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "C_sound":
                sound = pygame.mixer.Sound('Music_Notes\C.wav')
                sound.play()
            if action == "Cs_sound":
                sound = pygame.mixer.Sound('Music_Notes\C_s.wav')
                sound.play()
            if action == "D_sound":
                sound = pygame.mixer.Sound('Music_Notes\D.wav')
                sound.play()
            if action == "Ds_sound":
                sound = pygame.mixer.Sound('Music_Notes\D_s.wav')
                sound.play()
            if action == "E_sound":
                sound = pygame.mixer.Sound('Music_Notes\E.wav')
                sound.play()
            if action == "F_sound":
                sound = pygame.mixer.Sound('Music_Notes\F.wav')
                sound.play()
            if action == "Fs_sound":
                sound = pygame.mixer.Sound('Music_Notes\F_s.wav')
                sound.play()
            if action == "G_sound":
                sound = pygame.mixer.Sound('Music_Notes\G.wav')
                sound.play()
            if action == "Gs_sound":
                sound = pygame.mixer.Sound('Music_Notes\G_s.wav')
                sound.play()
            if action == "A_sound":
                sound = pygame.mixer.Sound('Music_Notes\A.wav')
                sound.play()
            if action == "As_sound":
                sound = pygame.mixer.Sound('Music_Notes\As.wav')
                sound.play()
            if action == "H_sound":
                sound = pygame.mixer.Sound('Music_Notes\B.wav')
                sound.play()
            if action == "C1_sound":
                sound = pygame.mixer.Sound('Music_Notes\C1.wav')
                sound.play()
    else:
        pygame.draw.rect(screen,inactive_button,(x,y,width,height))

pygame.init()
pygame.time.set_timer(USEREVENT+1, 2000)
pygame.display.flip()

running = True
while running:
    keys(50,150,100,400,white,white_blur,action="C_sound")
    keys(155,50,75,300,black,white_blur,action="Cs_sound")
    keys(235,150,100,400,white,white_blur,action="D_sound")
    keys(340,50,75,300,black,white_blur,action="Ds_sound")
    keys(420,150,100,400,white,white_blur,action="E_sound")
    keys(525,150,100,400,white,white_blur,action="F_sound")
    keys(630,50,75,300,black,white_blur,action="Fs_sound")
    keys(710,150,100,400,white,white_blur,action="G_sound")
    keys(815,50,75,300,black,white_blur,action="Gs_sound")
    keys(895,150,100,400,white,white_blur,action="A_sound")
    keys(1000,50,75,300,black,white_blur,action="As_sound")
    keys(1080,150,100,400,white,white_blur,action="H_sound")
    keys(1185,150,100,400,white,white_blur,action="C1_sound")
    start = pygame.mouse.set_pos(cursor_positions[k])

    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            if k == 12:
                k = 0
                cursor_jump()
            else:
                k += 1
                cursor_jump()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:   # If user clicked escape key
            running = False     # Flag that we are done so we exit this loop

        pygame.display.update()

pygame.quit()
