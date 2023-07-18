import Quiz2

def levelCompleted2():
    import pygame
    import sys

    pygame.init()

    screenHeight = 550
    screenWidth = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            triviaTwo()
            clock.tick(30)


def triviaTwo():

    import pygame
    import os
    import random

    pygame.init()

    screenHeight = 550
    screenWidth = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

    trivia1 = pygame.image.load(os.path.join("Images/Trivias", "Trivia1Level2.png"))
    trivia2 = pygame.image.load(os.path.join("Images/Trivias", "Trivia2Level2.png"))
    trivia3 = pygame.image.load(os.path.join("Images/Trivias", "Trivia3Level2.png"))
    trivia4 = pygame.image.load(os.path.join("Images/Trivias", "Trivia4Level2.png"))
    trivia5 = pygame.image.load(os.path.join("Images/Trivias", "Trivia5Level2.png"))
    trivia6 = pygame.image.load(os.path.join("Images/Trivias", "Trivia6Level2.png"))
    trivia7 = pygame.image.load(os.path.join("Images/Trivias", "Trivia7Level2.png"))
    trivia8 = pygame.image.load(os.path.join("Images/Trivias", "Trivia8Level2.png"))
    trivia9 = pygame.image.load(os.path.join("Images/Trivias", "Trivia9Level2.png"))
    trivia10 = pygame.image.load(os.path.join("Images/Trivias", "Trivia10Level2.png"))
    randomList = random.choice((trivia1, trivia2, trivia3, trivia4, trivia5, trivia6, trivia7, trivia8, trivia9, trivia10))


    def button(x, y, w, h, image, imageOn, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed() #py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

        rect = pygame.Rect(x, y, w, h)
        on_button = rect.collidepoint(mouse)

        if on_button:  # if x+width > mouseposition[0] right side of box > x and y loc + height wch is the bottom of the box
            screen.blit(imageOn, imageOn.get_rect(center=rect.center))
        else:
            screen.blit(image, image.get_rect(center=rect.center))

        if on_button:
            if click[0] == 1 and action!= None:
                if action == "continue":
                    Quiz2.quiz2()

    buttonImg = pygame.image.load(os.path.join("Images/Trivias", "button.png")).convert_alpha()
    buttonImgHover = pygame.image.load(os.path.join("Images/Trivias", "buttonclicked.png")).convert_alpha()

    while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(randomList, [0, 0])
                button(399, 390, 300, 50, buttonImg, buttonImgHover, "continue")
                pygame.display.update()


def mainTrivia2():
    while True:
        levelCompleted2()

