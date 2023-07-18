import Quiz

def levelCompleted():
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
            triviaOne()
            clock.tick(30)


def triviaOne():

    import pygame
    import os
    import random

    pygame.init()

    screenHeight = 550
    screenWidth = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

    trivia1 = pygame.image.load(os.path.join("Images/Trivias", "Trivia1Level1.png"))
    trivia2 = pygame.image.load(os.path.join("Images/Trivias", "Trivia2Level1.png"))
    trivia3 = pygame.image.load(os.path.join("Images/Trivias", "Trivia3Level1.png"))
    trivia4 = pygame.image.load(os.path.join("Images/Trivias", "Trivia4Level1.png"))
    trivia5 = pygame.image.load(os.path.join("Images/Trivias", "Trivia5Level1.png"))
    trivia6 = pygame.image.load(os.path.join("Images/Trivias", "Trivia6Level1.png"))
    trivia7 = pygame.image.load(os.path.join("Images/Trivias", "Trivia7Level1.png"))
    trivia8 = pygame.image.load(os.path.join("Images/Trivias", "Trivia8Level1.png"))
    trivia9 = pygame.image.load(os.path.join("Images/Trivias", "Trivia9Level1.png"))
    trivia10 = pygame.image.load(os.path.join("Images/Trivias", "Trivia10Level1.png"))
    randomList = random.choice((trivia1, trivia2, trivia3, trivia4, trivia5, trivia6, trivia7, trivia8, trivia9, trivia10))


    def button(x, y, w, h, image, imageOn, action=None):
        mouse = pygame.mouse.get_pos() #get the mouse cursor position
        click = pygame.mouse.get_pressed() #py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

        rect = pygame.Rect(x, y, w, h)
        on_button = rect.collidepoint(mouse)

        if on_button:
            screen.blit(imageOn, imageOn.get_rect(center=rect.center))
        else:
            screen.blit(image, image.get_rect(center=rect.center))

        if on_button:
            if click[0] == 1 and action!= None:
                if action == "continue":
                    Quiz.quiz()

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


def mainTrivia():
    while True:
        levelCompleted()

