import pygame
import os
import random
import sys
import CBLevel2


# Initialize the pygame
pygame.init()

# Create the screen/ Global Constants
screenHeight = 550
screenWidth = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight)) #defines the display where the game will be shown/ window
clock = pygame.time.Clock()

pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

Running = [pygame.image.load(os.path.join("Images/Character", "run1.png")),
           pygame.image.load(os.path.join("Images/Character", "run2.png"))]
Jumping = pygame.image.load(os.path.join("Images/Character", "jump.png"))
Ducking = [pygame.image.load(os.path.join("Images/Character", "ducking1.1.png")),
           pygame.image.load(os.path.join("Images/Character", "ducking2.1.png"))]
Tree = [pygame.image.load(os.path.join("Images/Objects", "trees1.png")),
        pygame.image.load(os.path.join("Images/Objects", "trees2.png")),
        pygame.image.load(os.path.join("Images/Objects", "trees3.png"))]
Woods = [pygame.image.load(os.path.join("Images/Objects", "wood1.png")),
         pygame.image.load(os.path.join("Images/Objects", "wood2.png")),
         pygame.image.load(os.path.join("Images/Objects", "wood3.png")),
         pygame.image.load(os.path.join("Images/Objects", "wood4.png"))]
Clouds = pygame.image.load(os.path.join("Images/Objects", "clouds.png"))
Birds = [pygame.image.load(os.path.join("Images/Character", "ducking1.png")),
         pygame.image.load(os.path.join("Images/Character", "ducking2.png"))]
Background = pygame.image.load(os.path.join("Images/Objects", "ground.png"))
Finish = pygame.image.load(os.path.join("Images/Objects", "Finish.png"))


class Character:
    positionX = 80
    positionY = 310
    positionYDucking = 340
    jumpVelocity = 8.5 #taas ng talon

    def __init__(self): #to initialize the character
        self.run_img = Running
        self.jump_img = Jumping
        self.duck_img = Ducking

        self.character_run = True
        self.character_jump = False
        self.character_duck = False

        self.step_index = 0
        self.jump_vel = self.jumpVelocity
        self.image = self.run_img[0]
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.positionX
        self.character_rect.y = self.positionY

    def update(self, playerInput): #update on every while loop
        if self.character_run:
            self.run()
        if self.character_jump:
            self.jump()
        if self.character_duck:
            self.duck()

        if self.step_index >= 10: #reset image after 10 steps; used to animate the character
            self.step_index = 0

        if playerInput[pygame.K_UP] and not self.character_jump: #when we press up key and character is not jumping
            self.character_run = False
            self.character_jump = True
            self.character_duck = False
        elif playerInput[pygame.K_DOWN] and not self.character_jump:
            self.character_run = False
            self.character_jump = False
            self.character_duck = True
        elif not (self.character_jump or playerInput[pygame.K_DOWN]):
            self.character_run = True
            self.character_jump = False
            self.character_duck = False

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.positionX
        self.character_rect.y = self.positionYDucking
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5] #kapag ang self index ay between 0 and 5, first img ang didisplay
        self.character_rect = self.image.get_rect()
        self.character_rect.x = self.positionX
        self.character_rect.y = self.positionY
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.character_jump:
            self.character_rect.y -= self.jump_vel * 5 #kapag tumalon, decrease ang rect.y
            self.jump_vel -= 0.6 #decrease the velocity
        if self.jump_vel < - self.jumpVelocity: #kapag nareach ang negative, magfalse ang jump
            self.character_jump = False
            self.jump_vel = self.jumpVelocity #to reset the jump velocity

    def draw(self, screen):
        screen.blit(self.image, (self.character_rect.x, self.character_rect.y))


class Cloud:
    def __init__(self):
        self.x = screenWidth + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = Clouds
        self.width = self.image.get_width()

    def update(self):
        self.x -= gameSpeed #clouds to exit the screen
        if self.x < -self.width: #reset the position of clouds
            self.x = screenWidth + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class Obstacle: #parent class of all the obstacles
    def __init__(self, image, type):
        self.image = image
        self.type = type #what type of image will be displayed to the screen
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screenWidth

    def update(self):
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width: #to remove the obstacle once it is on the left side offscreen
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)


class FinishStar:
    def __init__(self):
        self.image = Finish
        self.rect = self.image.get_rect(topleft = (screenWidth + 100, 290))

    def update(self): # pygame.Surface.get_rect.get_rect() returns a rectangle with the size of the Surface object, that always starts at (0, 0) since a Surface object has no position. You have to update the position of the rect attribute:
        self.rect.x -= gameSpeed
        if self.rect.x < -self.rect.width:
            self.rect.x = screenWidth + 2500
            self.rect.y = 50

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class WoodBlocks(Obstacle): #() this will inherit the class obstacle
    def __init__(self, image):
        self.type = random.randint(0, 3)
        super().__init__(image, self.type) #initialize to the parent class
        self.rect.y = 270


class Trees(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 270


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 240
        self.index = 0

    def draw(self, screen): #overwrites the parentclass bc bird is animated
        if self.index >= 9: #pag ang index ay 10, marereset ang index
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect) #if self index is 0-4, frst img will be shown and 5-9, second img
        self.index += 1


def background():
    global posXBg, posYBg
    image_width = Background.get_width() #width of the image
    screen.blit(Background, (posXBg, posYBg))
    screen.blit(Background, (image_width + posXBg, posYBg))
    if posXBg <= -image_width:
        screen.blit(Background, (image_width + posXBg, posYBg))
        posXBg = 0
    posXBg -= gameSpeed


def score():
    global scorePoints, gameSpeed
    scorePoints += 1
    if scorePoints % 100 == 0: #every 100 pts bibilis ang gamespeed
        gameSpeed += 1  # para lalong bumilis

    font = pygame.font.Font('Fonts/Affogato-Medium.otf', 20)
    text = font.render("Points: " + str(scorePoints), True, (0, 0, 0))
    screen.blit(text, (879,20))
    text1 = font.render("Level 1/5", True, (0, 0, 0))
    screen.blit(text1, (35, 20))


def menu(death_count):
    global scorePoints

    while True:
        if death_count == 0:
            font = pygame.font.Font('Fonts/Affogato-Medium.otf', 34)
            background_image = pygame.image.load(os.path.join("Images/Start", "background.png"))
            screen.blit(background_image, [0, 0])
            start = font.render("PRESS ANY KEY TO START", True, (129, 185, 201))
            screen.blit(start, [370,277])

        elif death_count > 0:
            font = pygame.font.Font('Fonts/Affogato-Bold.otf', 22)
            background_image = pygame.image.load(os.path.join("Images/Start", "Level1Lose.png"))
            screen.blit(background_image, [0, 0])
            text = font.render("PRESS ANY KEY TO RESTART", True, (122, 166, 185))
            screen.blit(text, [372, 399])
            text = font.render("You CODE do it!", True, (163, 213, 176))
            screen.blit(text, [440, 364])

            font = pygame.font.Font('Fonts/Affogato-Medium.otf', 28)
            score = font.render("Your score: " + str(scorePoints), True, (122, 166, 185))
            screen.blit(score, [447, 300])
            text = font.render("Score not reached", True, (122, 166, 185))
            screen.blit(text, [407, 330])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: #any key is pressed
                main()


def quiz():
    def checker(x, y, w, h, image, imageOn, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()  # py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

        rect = pygame.Rect(x, y, w, h)
        on_button = rect.collidepoint(mouse)

        if on_button:  # panghover
            screen.blit(imageOn, imageOn.get_rect(center=rect.center))

        else:
            screen.blit(image, image.get_rect(center=rect.center))

        if on_button:
            if click[0] == 1 and action != None:
                if action == "passed":
                    passed()
                elif action == "failed":
                    failed()

    def passed():
        def continueButton(x, y, w, h, image, imageOn, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

            rect = pygame.Rect(x, y, w, h)
            on_button = rect.collidepoint(mouse)

            if on_button: #panghover
                screen.blit(imageOn, imageOn.get_rect(center=rect.center))

            else:
                screen.blit(image, image.get_rect(center=rect.center))

            if on_button:
                if click[0] == 1 and action!= None:
                    if action == "continue":
                        CBLevel2.stageTwo()

        background = pygame.image.load(os.path.join("Images/Quiz", "Level1Passed.png"))
        contButton = pygame.image.load(os.path.join("Images/Quiz", "continue.png"))
        contButtonHover = pygame.image.load(os.path.join("Images/Quiz", "continueHover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(background, [0, 0])
                continueButton(350, 420, 300, 50, contButton, contButtonHover, "continue") #x,y, width, height
                pygame.display.update()

    def failed():
        def tryButton(x, y, w, h, image, imageOn, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed() #py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

            rect = pygame.Rect(x, y, w, h)
            on_button = rect.collidepoint(mouse)

            if on_button: #panghover
                screen.blit(imageOn, imageOn.get_rect(center=rect.center))

            else:
                screen.blit(image, image.get_rect(center=rect.center))

            if on_button:
                if click[0] == 1 and action!= None:
                    if action == "try":
                        main()

        background = pygame.image.load(os.path.join("Images/Quiz", "Level1Failed.png"))
        tryagainButton = pygame.image.load(os.path.join("Images/Quiz", "tryagain.png"))
        tryagainHover = pygame.image.load(os.path.join("Images/Quiz", "tryagainHover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(background, [0, 0])
                tryButton(350, 420, 300, 50, tryagainButton, tryagainHover, "try") #x,y, width, height
                pygame.display.update()

    def quizOne():  #Answer: B
        q1BG = pygame.image.load(os.path.join("Images/Quiz", "question1.png"))
        q1A = pygame.image.load(os.path.join("Images/Quiz", "q1A.png"))
        q1AHover = pygame.image.load(os.path.join("Images/Quiz", "q1Ahover.png"))
        q1B = pygame.image.load(os.path.join("Images/Quiz", "q1B.png"))
        q1BHover = pygame.image.load(os.path.join("Images/Quiz", "q1Bhover.png"))
        q1C = pygame.image.load(os.path.join("Images/Quiz", "q1C.png"))
        q1CHover = pygame.image.load(os.path.join("Images/Quiz", "q1Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q1BG, [0, 0])
                checker(370, 225, 300, 50, q1A, q1AHover, "failed") #x,y, width, height
                checker(370, 285, 300, 50, q1B, q1BHover, "passed")
                checker(370, 350, 300, 50, q1C, q1CHover, "failed")
                pygame.display.update()

    def quizTwo(): #Answer: A
        q2BG = pygame.image.load(os.path.join("Images/Quiz", "question2.png"))
        q2A = pygame.image.load(os.path.join("Images/Quiz", "q2A.png"))
        q2AHover = pygame.image.load(os.path.join("Images/Quiz", "q2Ahover.png"))
        q2B = pygame.image.load(os.path.join("Images/Quiz", "q2B.png"))
        q2BHover = pygame.image.load(os.path.join("Images/Quiz", "q2Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q2BG, [0, 0])
                checker(370, 265, 300, 50, q2A, q2AHover, "passed") #x,y, width, height
                checker(370, 335, 300, 50, q2B, q2BHover, "failed")
                pygame.display.update()

    def quizThree(): #Answer: C
        q3BG = pygame.image.load(os.path.join("Images/Quiz", "question3.png"))
        q3A = pygame.image.load(os.path.join("Images/Quiz", "q3A.png"))
        q3AHover = pygame.image.load(os.path.join("Images/Quiz", "q3Ahover.png"))
        q3B = pygame.image.load(os.path.join("Images/Quiz", "q3B.png"))
        q3BHover = pygame.image.load(os.path.join("Images/Quiz", "q3Bhover.png"))
        q3C = pygame.image.load(os.path.join("Images/Quiz", "q3C.png"))
        q3CHover = pygame.image.load(os.path.join("Images/Quiz", "q3Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q3BG, [0, 0])
                checker(370, 245, 300, 50, q3A, q3AHover, "failed") #x,y, width, height
                checker(370, 305, 300, 50, q3B, q3BHover, "failed")
                checker(370, 365, 300, 50, q3C, q3CHover, "passed")
                pygame.display.update()

    def quizFour(): #Answer: B
        q4BG = pygame.image.load(os.path.join("Images/Quiz", "question4.png"))
        q4A = pygame.image.load(os.path.join("Images/Quiz", "q4A.png"))
        q4AHover = pygame.image.load(os.path.join("Images/Quiz", "q4Ahover.png"))
        q4B = pygame.image.load(os.path.join("Images/Quiz", "q4B.png"))
        q4BHover = pygame.image.load(os.path.join("Images/Quiz", "q4Bhover.png"))
        q4C = pygame.image.load(os.path.join("Images/Quiz", "q4C.png"))
        q4CHover = pygame.image.load(os.path.join("Images/Quiz", "q4Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q4BG, [0, 0])
                checker(370, 245, 300, 50, q4A, q4AHover, "failed") #x,y, width, height
                checker(370, 305, 300, 50, q4B, q4BHover, "passed")
                checker(370, 365, 300, 50, q4C, q4CHover, "failed")
                pygame.display.update()

    def quizFive(): #Answer: A
        q5BG = pygame.image.load(os.path.join("Images/Quiz", "question5.png"))
        q5A = pygame.image.load(os.path.join("Images/Quiz", "q5A.png"))
        q5AHover = pygame.image.load(os.path.join("Images/Quiz", "q5Ahover.png"))
        q5B = pygame.image.load(os.path.join("Images/Quiz", "q5B.png"))
        q5BHover = pygame.image.load(os.path.join("Images/Quiz", "q5Bhover.png"))
        q5C = pygame.image.load(os.path.join("Images/Quiz", "q5C.png"))
        q5CHover = pygame.image.load(os.path.join("Images/Quiz", "q5Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q5BG, [0, 0])
                checker(370, 245, 300, 50, q5A, q5AHover, "passed") #x,y, width, height
                checker(370, 305, 300, 50, q5B, q5BHover, "failed")
                checker(370, 365, 300, 50, q5C, q5CHover, "failed")
                pygame.display.update()

    def quizSix(): #Answer: A
        q6BG = pygame.image.load(os.path.join("Images/Quiz", "question6.png"))
        q6A = pygame.image.load(os.path.join("Images/Quiz", "q6A.png"))
        q6AHover = pygame.image.load(os.path.join("Images/Quiz", "q6Ahover.png"))
        q6B = pygame.image.load(os.path.join("Images/Quiz", "q6B.png"))
        q6BHover = pygame.image.load(os.path.join("Images/Quiz", "q6Bhover.png"))
        q6C = pygame.image.load(os.path.join("Images/Quiz", "q6C.png"))
        q6CHover = pygame.image.load(os.path.join("Images/Quiz", "q6Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q6BG, [0, 0])
                checker(370, 245, 300, 50, q6A, q6AHover, "passed") #x,y, width, height
                checker(370, 305, 300, 50, q6B, q6BHover, "failed")
                checker(370, 365, 300, 50, q6C, q6CHover, "failed")
                pygame.display.update()

    def quizSeven(): #Answer: B
        q7BG = pygame.image.load(os.path.join("Images/Quiz", "question7.png"))
        q7A = pygame.image.load(os.path.join("Images/Quiz", "q7A.png"))
        q7AHover = pygame.image.load(os.path.join("Images/Quiz", "q7Ahover.png"))
        q7B = pygame.image.load(os.path.join("Images/Quiz", "q7B.png"))
        q7BHover = pygame.image.load(os.path.join("Images/Quiz", "q7Bhover.png"))
        q7C = pygame.image.load(os.path.join("Images/Quiz", "q7C.png"))
        q7CHover = pygame.image.load(os.path.join("Images/Quiz", "q7Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q7BG, [0, 0])
                checker(370, 245, 300, 50, q7A, q7AHover, "failed") #x,y, width, height
                checker(370, 305, 300, 50, q7B, q7BHover, "passed")
                checker(370, 365, 300, 50, q7C, q7CHover, "failed")
                pygame.display.update()

    def quizEight(): #Answer: C
        q8BG = pygame.image.load(os.path.join("Images/Quiz", "question8.png"))
        q8A = pygame.image.load(os.path.join("Images/Quiz", "q8A.png"))
        q8AHover = pygame.image.load(os.path.join("Images/Quiz", "q8Ahover.png"))
        q8B = pygame.image.load(os.path.join("Images/Quiz", "q8B.png"))
        q8BHover = pygame.image.load(os.path.join("Images/Quiz", "q8Bhover.png"))
        q8C = pygame.image.load(os.path.join("Images/Quiz", "q8C.png"))
        q8CHover = pygame.image.load(os.path.join("Images/Quiz", "q8Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q8BG, [0, 0])
                checker(370, 245, 300, 50, q8A, q8AHover, "failed") #x,y, width, height
                checker(370, 305, 300, 50, q8B, q8BHover, "failed")
                checker(370, 365, 300, 50, q8C, q8CHover, "passed")
                pygame.display.update()

    def quizNine(): #Answer: C
        q9BG = pygame.image.load(os.path.join("Images/Quiz", "question9.png"))
        q9A = pygame.image.load(os.path.join("Images/Quiz", "q9A.png"))
        q9AHover = pygame.image.load(os.path.join("Images/Quiz", "q9Ahover.png"))
        q9B = pygame.image.load(os.path.join("Images/Quiz", "q9B.png"))
        q9BHover = pygame.image.load(os.path.join("Images/Quiz", "q9Bhover.png"))
        q9C = pygame.image.load(os.path.join("Images/Quiz", "q9C.png"))
        q9CHover = pygame.image.load(os.path.join("Images/Quiz", "q9Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q9BG, [0, 0])
                checker(370, 245, 300, 50, q9A, q9AHover, "failed") #x,y, width, height
                checker(370, 305, 300, 50, q9B, q9BHover, "failed")
                checker(370, 365, 300, 50, q9C, q9CHover, "passed")
                pygame.display.update()

    def quizTen(): #Answer: A
        q10BG = pygame.image.load(os.path.join("Images/Quiz", "question10.png"))
        q10A = pygame.image.load(os.path.join("Images/Quiz", "q10A.png"))
        q10AHover = pygame.image.load(os.path.join("Images/Quiz", "q10Ahover.png"))
        q10B = pygame.image.load(os.path.join("Images/Quiz", "q10B.png"))
        q10BHover = pygame.image.load(os.path.join("Images/Quiz", "q10Bhover.png"))
        q10C = pygame.image.load(os.path.join("Images/Quiz", "q10C.png"))
        q10CHover = pygame.image.load(os.path.join("Images/Quiz", "q10Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q10BG, [0, 0])
                checker(370, 245, 300, 50, q10A, q10AHover, "passed") #x,y, width, height
                checker(370, 305, 300, 50, q10B, q10BHover, "failed")
                checker(370, 365, 300, 50, q10C, q10CHover, "failed")
                pygame.display.update()

    functions = [quizOne, quizTwo, quizThree, quizFour, quizFive, quizSix, quizSeven, quizEight, quizNine, quizTen]
    while True:
            fn = random.choice(functions)
            fn()


def levelCompleted():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            triviaOne()
            clock.tick(30)


def triviaOne():
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
                    quiz()

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


def main():
    # Game Loop
    global gameSpeed, posXBg, posYBg, scorePoints, obstacles
    run = True
    star = FinishStar()
    player = Character()
    cloud = Cloud()
    gameSpeed = 15
    posXBg = 0
    posYBg = 350
    scorePoints = 0
    obstacles = []
    death_count = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((192, 226, 236))
        playerInput = pygame.key.get_pressed()

        background()

        if len(obstacles) == 0: # kapag walang laman ang list by appending dun sa list
            if random.randint(0, 3) == 0:
                obstacles.append(WoodBlocks(Woods))
            elif random.randint(0, 2) == 0:
                obstacles.append(Trees(Tree))
            elif random.randint(0, 1) == 0:
                obstacles.append(Bird(Birds))

        player.draw(screen)
        player.update(playerInput)

        cloud.draw(screen)
        cloud.update()

        score()

        if scorePoints >= 320:
            star.draw(screen)
            star.update()

            if player.character_rect.colliderect(star.rect):
                font = pygame.font.Font('Fonts/Bubblebody.ttf', 22)
                font1 = pygame.font.Font('Fonts/Affogato-Bold.otf', 20)
                font2 = pygame.font.Font('Fonts/Billgis - Personal Use.ttf', 38)
                font3 = pygame.font.Font('Fonts/Affogato-Medium.otf', 31)
                background_image = pygame.image.load(os.path.join("Images/Start", "Level1Complete.png"))
                screen.blit(background_image, [0, 0])
                textContinue = font1.render("PRESS ANY KEY TO CONTINUE", True, (122, 166, 185))
                screen.blit(textContinue, [411, 400])
                textComplete = font2.render("level one completed", True, (163, 213, 176))
                screen.blit(textComplete, [467, 292])
                textCongrats = font.render("Congratulations!", True, (163, 213, 176))
                screen.blit(textCongrats, [473, 321])
                textScore = font3.render("SCORE REACHED!", True, (122, 166, 185))
                screen.blit(textScore, [450, 349])
                pygame.display.update()
                mainTrivia()

        for obstacle in obstacles: #in every single obstacle dun sa loob ng obstacles list
            obstacle.draw(screen)
            obstacle.update()
            if player.character_rect.colliderect(obstacle.rect): #collision detection
                pygame.time.delay(200)
                death_count += 1
                menu(death_count)

        pygame.display.update()
        clock.tick(30)


menu(death_count=0)

