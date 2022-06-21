#Physical Computing Project
#소프트웨어학부 2018044857 이강영

import serial
import pygame

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (0, 0, 128)
PURPLE = (128, 0, 255)
font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Physical Computing Project", True, (0, 0, 0))

pyscreen = pygame.display.set_mode((1024,768), 0, 32)
pyscreen.fill(WHITE)
pyscreen.blit(text,(512 - text.get_width() // 2, 384 - text.get_height() // 2))
pygame.display.flip()


ser = serial.Serial(
    port="/dev/cu.usbserial-14440",
    baudrate=9600,
) #port 입력 필요
run = True
a_sound = pygame.mixer.Sound("도.wav")
b_sound = pygame.mixer.Sound("레.wav")
c_sound = pygame.mixer.Sound("미.wav")
d_sound = pygame.mixer.Sound("파.wav")
e_sound = pygame.mixer.Sound("솔.wav")
f_sound = pygame.mixer.Sound("라.wav")
g_sound = pygame.mixer.Sound("시.wav")

while run:
    if ser.readable():

        res = ser.readline()  

        data = res.decode()[:len(res)-1] 
        
        print("data : ",data)
        for event in pygame.event.get(): #ESC키를 누르면 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        if '0' in data:
            pygame.mixer.stop()
            print("도")
            a_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("C", True, (0, 0, 0))
            pyscreen.fill(RED)
        elif '1' in data:
            pygame.mixer.stop()
            print("레")
            b_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("D", True, (0, 0, 0))
            pyscreen.fill(ORANGE)
        elif '2' in data:
            pygame.mixer.stop()
            
            print("미")
            c_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("E", True, (0, 0, 0))
            pyscreen.fill(YELLOW)
        elif '3' in data:
            pygame.mixer.stop()
            print("파")
            d_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("F", True, (0, 0, 0))
            pyscreen.fill(GREEN)
        elif '4' in data:
            pygame.mixer.stop()
            print("솔")
            e_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("G", True, (0, 0, 0))
            pyscreen.fill(BLUE)
        elif '5' in data:
            pygame.mixer.stop()
            print("라")
            f_sound.play() 
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("A", True, (0, 0, 0))
            pyscreen.fill(INDIGO)
        elif '6' in data:
            pygame.mixer.stop()
            print("시")
            g_sound.play()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("B", True, (0, 0, 0))
            pyscreen.fill(PURPLE)
            
        elif '7' in data:
            pygame.mixer.stop()
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("Physical Computing Project", True, (0, 0, 0))
            pyscreen.fill(WHITE)
        
        pyscreen.blit(text,(512 - text.get_width() // 2, 384 - text.get_height() // 2))
        pygame.display.update()

pygame.quit()