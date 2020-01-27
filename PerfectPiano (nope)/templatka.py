# -*- coding: utf-8 -*-

import multiprocessing as mp
import pygame
from pygame.locals import *
import pandas as pd
import filterlib as flt
import blink as blk
#from pyOpenBCI import OpenBCIGanglion


def blinks_detector(quit_program, blink_det, blinks_num, blink,):
    def detect_blinks(sample):
        if SYMULACJA_SYGNALU:
            smp_flted = sample
        else:
            smp = sample.channels_data[0]
            smp_flted = frt.filterIIR(smp, 0)
        #print(smp_flted)

        brt.blink_detect(smp_flted, -38000)
        if brt.new_blink:
            if brt.blinks_num == 1:
                #connected.set()
                print('CONNECTED. Speller starts detecting blinks.')
            else:
                blink_det.put(brt.blinks_num)
                blinks_num.value = brt.blinks_num
                blink.value = 1

        if quit_program.is_set():
            if not SYMULACJA_SYGNALU:
                print('Disconnect signal sent...')
                board.stop_stream()


####################################################
    SYMULACJA_SYGNALU = True
####################################################
    mac_adress = 'd2:b4:11:81:48:ad'
####################################################

    clock = pygame.time.Clock()
    frt = flt.FltRealTime()
    brt = blk.BlinkRealTime()

    if SYMULACJA_SYGNALU:
        df = pd.read_csv('dane_do_symulacji/data.csv')
        for sample in df['signal']:
            if quit_program.is_set():
                break
            detect_blinks(sample)
            clock.tick(200)
        print('KONIEC SYGNAŁU')
        quit_program.set()
    else:
        board = OpenBCIGanglion(mac=mac_adress)
        board.start_stream(detect_blinks)

if __name__ == "__main__":


    blink_det = mp.Queue()
    blink = mp.Value('i', 0)
    blinks_num = mp.Value('i', 0)
    #connected = mp.Event()
    quit_program = mp.Event()

    proc_blink_det = mp.Process(
        name='proc_',
        target=blinks_detector,
        args=(quit_program, blink_det, blinks_num, blink,)
        )

    # rozpoczęcie podprocesu
    proc_blink_det.start()
    print('subprocess started')

    ############################################
    # Poniżej należy dodać rozwinięcie programu
    ############################################
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
        if blink.value == 1:
            print ("BLINK!")
            if k == 0:
                sound = pygame.mixer.Sound('Music_Notes\C.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 1:
                sound = pygame.mixer.Sound('Music_Notes\C_s.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 2:
                sound = pygame.mixer.Sound('Music_Notes\D.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 3:
                sound = pygame.mixer.Sound('Music_Notes\D_s.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 4:
                sound = pygame.mixer.Sound('Music_Notes\E.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 5:
                sound = pygame.mixer.Sound('Music_Notes\F.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 6:
                sound = pygame.mixer.Sound('Music_Notes\F_s.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 7:
                sound = pygame.mixer.Sound('Music_Notes\G.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 8:
                sound = pygame.mixer.Sound('Music_Notes\G_s.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 9:
                sound = pygame.mixer.Sound('Music_Notes\A.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 10:
                sound = pygame.mixer.Sound('Music_Notes\As.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 11:
                sound = pygame.mixer.Sound('Music_Notes\B.wav')
                sound.play()
                sound.fadeout(1000)
            if k == 12:
                sound = pygame.mixer.Sound('Music_Notes\C1.wav')
                sound.play()
                sound.fadeout(1000)
            blink.value = 0

    def keys (x, y, width, height, inactive_button, active_button):#, action=None):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+width > cursor[0] > x and y+height > cursor[1] > y:
            pygame.draw.rect(screen,active_button,(x,y,width,height))
        else:
            pygame.draw.rect(screen,inactive_button,(x,y,width,height))

    pygame.init()
    pygame.time.set_timer(USEREVENT+1, 1200)
    pygame.display.flip()

    running = True
    while running:
        keys(50,150,100,400,white,white_blur)
        keys(155,50,75,300,black,white_blur)
        keys(235,150,100,400,white,white_blur)
        keys(340,50,75,300,black,white_blur)
        keys(420,150,100,400,white,white_blur)
        keys(525,150,100,400,white,white_blur)
        keys(630,50,75,300,black,white_blur)
        keys(710,150,100,400,white,white_blur)
        keys(815,50,75,300,black,white_blur)
        keys(895,150,100,400,white,white_blur)
        keys(1000,50,75,300,black,white_blur)
        keys(1080,150,100,400,white,white_blur)
        keys(1185,150,100,400,white,white_blur)
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
                running = False     # Flag that we are done so we exit this loop (piano)
                print('quitting')
                quit_program.set()  # Flag that we are done so we exit this loop (blink)
                if quit_program.is_set():
                    break
            pygame.display.update()
    pygame.quit()

# Zakończenie podprocesów
    proc_blink_det.join()
