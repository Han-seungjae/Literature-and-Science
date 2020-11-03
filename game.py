import pygame
import sys
pygame.init()
pygame.font.init()

############################## 화면 띄우기
pygame.display.set_caption("문과 vs 이과 알파")
SCREEN = pygame.display.set_mode((1280,720))
bg1 = pygame.image.load('bg.png')

a = pygame.mixer.Sound("123.wav")
a.play(-1)

SCREEN.blit(bg1, (0, 0))



moneyfont = pygame.font.SysFont(None,40)
img = moneyfont.render('Money',True,'black')
SCREEN.blit(img, (10,50))

hpfont = pygame.font.SysFont(None,40)
img = hpfont.render('HP',True,'red')
SCREEN.blit(img, (10,10))   




def run():
    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.blit(bg1, (0,0))
        

def ip():
    pygame.display.update()

#def 적는곳 
################################
###############################
ip()
run()





pygame.quit()
sys.exit()
            
