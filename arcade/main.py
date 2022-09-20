import pygame
import random

pygame.init()
pygame.font.init()

my_font = pygame.font.SysFont('Comic Sans MS', 30)

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Дэн собирает грибы")
clock = pygame.time.Clock()

player = pygame.image.load('danchik_sprite.png').convert_alpha()
bg = pygame.image.load('forest_bg.png').convert()

bg = pygame.transform.scale(bg, (500, 500))
player = pygame.transform.scale(player, (60, 200))

x = 50
y = 50
speed = 50

x_mashroom = 500
y_mashroom = 500
s = 0

def food_drawing(x, y):
    if x == 500 and y == 500:
        global x_mashroom
        x_mashroom = random.randrange(50, 450, 50)
        global y_mashroom
        y_mashroom = random.randrange(50, 450, 50)
    mashroom = pygame.transform.scale(pygame.image.load('mushroom.png'), (60, 50))
    win.blit(mashroom, (x, y))




def sbor():
    global x_mashroom
    global y_mashroom
    if (x//speed, y//speed + 1) == (x_mashroom//speed, y_mashroom//speed):

        x_mashroom = 500
        y_mashroom = 500
        score()


def score():
    global s
    s += 1
    return s

score_text = my_font.render(f'SCORE:{s}', False, (170, 80, 96))

run = True
while (run):
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x -= speed

    elif key[pygame.K_RIGHT]:
        x += speed

    elif key[pygame.K_UP]:
        y -= speed

    elif key[pygame.K_DOWN]:
        y += speed

    score_text = my_font.render(f'SCORE:{s}', False, (170, 80, 96))

    win.blit(bg, (0, 0))
    win.blit(player, (x, y))
    win.blit(score_text, (300, 50))




    food_drawing(x_mashroom, y_mashroom)
    sbor()

    if s == 10:
        win.fill((250, 250, 250))
        text = my_font.render(f'Дэн собрал все грибы на полянке!!', False, (0, 0, 0))
        text_2 = my_font.render(f' Ты победил', False, (0, 0, 0))
        text_3 = my_font.render(f'Нажми пробел, чтобы повторить', False, (0, 0, 0))
        win.blit(text, (0, 50))
        win.blit(text_2, (150, 100))
        win.blit(text_3, (10, 250))

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            s = 0




    pygame.display.update()



pygame.quit()