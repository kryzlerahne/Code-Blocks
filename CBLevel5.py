def stageFive():
    import pygame
    import os
    import random
    import sys

    # Initialize the pygame
    pygame.init()

    # Create the screen/ Global Constants
    screenHeight = 550
    screenWidth = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

    Running = [pygame.image.load(os.path.join("Images/Character", "run1.png")),
               pygame.image.load(os.path.join("Images/Character", "run2.png"))]
    Jumping = pygame.image.load(os.path.join("Images/Character", "jump.png"))
    Ducking = [pygame.image.load(os.path.join("Images/Character", "ducking1.1.png")),
               pygame.image.load(os.path.join("Images/Character", "ducking2.1.png"))]
    SpaceTree = [pygame.image.load(os.path.join("Images/Objects", "spaceship.png")),
            pygame.image.load(os.path.join("Images/Objects", "spaceship2.png"))]
    Space = [pygame.image.load(os.path.join("Images/Objects", "flag.png")),
             pygame.image.load(os.path.join("Images/Objects", "planet.png")),
             pygame.image.load(os.path.join("Images/Objects", "planet2.png"))]
    Clouds = pygame.image.load(os.path.join("Images/Objects", "clouds.png"))
    Meteor = [pygame.image.load(os.path.join("Images/Objects", "meteorite.png")),
             pygame.image.load(os.path.join("Images/Objects", "meteorite2.png"))]
    Background = pygame.image.load(os.path.join("Images/Objects", "ground5.png"))
    Finish = pygame.image.load(os.path.join("Images/Objects", "Finish.png"))

    class Character:
        positionX = 80
        positionY = 310
        positionYDucking = 340
        jumpVelocity = 8.5

        def __init__(self):
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

        def update(self, playerInput):
            if self.character_run:
                self.run()
            if self.character_jump:
                self.jump()
            if self.character_duck:
                self.duck()

            if self.step_index >= 10:
                self.step_index = 0

            if playerInput[pygame.K_UP] and not self.character_jump:
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
            self.image = self.run_img[self.step_index // 5]
            self.character_rect = self.image.get_rect()
            self.character_rect.x = self.positionX
            self.character_rect.y = self.positionY
            self.step_index += 1

        def jump(self):
            self.image = self.jump_img
            if self.character_jump:
                self.character_rect.y -= self.jump_vel * 5
                self.jump_vel -= 0.6
            if self.jump_vel < - self.jumpVelocity:
                self.character_jump = False
                self.jump_vel = self.jumpVelocity

        def draw(self, screen):
            screen.blit(self.image, (self.character_rect.x, self.character_rect.y))

    class Cloud:
        def __init__(self):
            self.x = screenWidth + random.randint(800, 1000)
            self.y = random.randint(50, 100)
            self.image = Clouds
            self.width = self.image.get_width()

        def update(self):
            self.x -= gameSpeed
            if self.x < -self.width:
                self.x = screenWidth + random.randint(2500, 3000)
                self.y = random.randint(50, 100)

        def draw(self, screen):
            screen.blit(self.image, (self.x, self.y))

    class Obstacle:
        def __init__(self, image, type):
            self.image = image
            self.type = type
            self.rect = self.image[self.type].get_rect()
            self.rect.x = screenWidth

        def update(self):
            self.rect.x -= gameSpeed
            if self.rect.x < -self.rect.width:
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

    class SpaceBlocks(Obstacle):
        def __init__(self, image):
            self.type = random.randint(0, 2)
            super().__init__(image, self.type)
            self.rect.y = 270

    class Trees(Obstacle):
        def __init__(self, image):
            self.type = random.randint(0, 1)
            super().__init__(image, self.type)
            self.rect.y = 270

    class Meteors(Obstacle):
        def __init__(self, image):
            self.type = 0
            super().__init__(image, self.type)
            self.rect.y = 240
            self.index = 0

        def draw(self, screen):
            if self.index >= 9:
                self.index = 0
            screen.blit(self.image[self.index // 5], self.rect)
            self.index += 1

    def background5():
        global posXBg, posYBg
        image_width = Background.get_width()
        screen.blit(Background, (posXBg, posYBg))
        screen.blit(Background, (image_width + posXBg, posYBg))
        if posXBg <= -image_width:
            screen.blit(Background, (image_width + posXBg, posYBg))
            posXBg = 0
        posXBg -= gameSpeed

    def score5():
        global scorePoints, gameSpeed
        scorePoints += 1
        if scorePoints % 100 == 0:
            gameSpeed += 1  # para lalong bumilis

        font = pygame.font.Font('Fonts/Affogato-Medium.otf', 20)
        text = font.render("Points: " + str(scorePoints), True, (0, 0, 0))
        screen.blit(text, (879,20))
        text1 = font.render("Level 5/5", True, (0, 0, 0))
        screen.blit(text1, (35, 20))

    def menu5(death_count):
        global scorePoints

        while True:
            if death_count == 0:
                def levelFive(x, y, w, h, image, imageOn, action=None):
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
                            if action == "level5":
                                main5()

                background = pygame.image.load(os.path.join("Images/Start", "level5map.png"))
                nextLevel = pygame.image.load(os.path.join("Images/Start", "level5button.png"))
                nextLevelHover = pygame.image.load(os.path.join("Images/Start", "level5buttonhover.png"))

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                    screen.blit(background, [0, 0])
                    levelFive(707, 475, 300, 50, nextLevel, nextLevelHover, "level5")  # x,y, width, height
                    pygame.display.update()

            elif death_count > 0:
                font = pygame.font.Font('Fonts/Affogato-Bold.otf', 22)
                background_image = pygame.image.load(os.path.join("Images/Start", "Level5Lose.png"))
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
                elif event.type == pygame.KEYDOWN:
                    main5()

    def quiz5():
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
                click = pygame.mouse.get_pressed()  # py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

                rect = pygame.Rect(x, y, w, h)
                on_button = rect.collidepoint(mouse)

                if on_button:  # panghover
                    screen.blit(imageOn, imageOn.get_rect(center=rect.center))

                else:
                    screen.blit(image, image.get_rect(center=rect.center))

                if on_button:
                    if click[0] == 1 and action != None:
                        if action == "quit":
                            pygame.quit()
                            quit()

            background = pygame.image.load(os.path.join("Images/Quiz", "Level5Passed.png"))
            homeButton = pygame.image.load(os.path.join("Images/Objects", "quit.png"))
            homeHover = pygame.image.load(os.path.join("Images/Objects", "quitHover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(background, [0, 0])
                continueButton(350, 420, 300, 50, homeButton, homeHover, "quit")  # x,y, width, height
                pygame.display.update()

        def failed():
            def tryButton(x, y, w, h, image, imageOn, action=None):
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
                        if action == "try":
                            main5()

            background = pygame.image.load(os.path.join("Images/Quiz", "Level5Failed.png"))
            tryagainButton = pygame.image.load(os.path.join("Images/Quiz", "tryagain.png"))
            tryagainHover = pygame.image.load(os.path.join("Images/Quiz", "tryagainHover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(background, [0, 0])
                tryButton(350, 420, 300, 50, tryagainButton, tryagainHover, "try")  # x,y, width, height
                pygame.display.update()

        def quizOne():  # Answer: A
            q1BG = pygame.image.load(os.path.join("Images/Quiz", "question1.5.png"))
            q1A = pygame.image.load(os.path.join("Images/Quiz", "q1.5A.png"))
            q1AHover = pygame.image.load(os.path.join("Images/Quiz", "q1.5Ahover.png"))
            q1B = pygame.image.load(os.path.join("Images/Quiz", "q1.5B.png"))
            q1BHover = pygame.image.load(os.path.join("Images/Quiz", "q1.5Bhover.png"))
            q1C = pygame.image.load(os.path.join("Images/Quiz", "q1.5C.png"))
            q1CHover = pygame.image.load(os.path.join("Images/Quiz", "q1.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q1BG, [0, 0])
                checker(370, 245, 300, 50, q1A, q1AHover, "passed")  # x,y, width, height
                checker(370, 305, 300, 50, q1B, q1BHover, "failed")
                checker(370, 365, 300, 50, q1C, q1CHover, "failed")
                pygame.display.update()

        def quizTwo():  # Answer: C
            q2BG = pygame.image.load(os.path.join("Images/Quiz", "question2.5.png"))
            q2A = pygame.image.load(os.path.join("Images/Quiz", "q2.5A.png"))
            q2AHover = pygame.image.load(os.path.join("Images/Quiz", "q2.5Ahover.png"))
            q2B = pygame.image.load(os.path.join("Images/Quiz", "q2.5B.png"))
            q2BHover = pygame.image.load(os.path.join("Images/Quiz", "q2.5Bhover.png"))
            q2C = pygame.image.load(os.path.join("Images/Quiz", "q2.5C.png"))
            q2CHover = pygame.image.load(os.path.join("Images/Quiz", "q2.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q2BG, [0, 0])
                checker(370, 255, 300, 50, q2A, q2AHover, "failed")  # x,y, width, height
                checker(370, 315, 300, 50, q2B, q2BHover, "failed")
                checker(370, 375, 300, 50, q2C, q2CHover, "passed")
                pygame.display.update()

        def quizThree():  # Answer: B
            q3BG = pygame.image.load(os.path.join("Images/Quiz", "question3.5.png"))
            q3A = pygame.image.load(os.path.join("Images/Quiz", "q3.5A.png"))
            q3AHover = pygame.image.load(os.path.join("Images/Quiz", "q3.5Ahover.png"))
            q3B = pygame.image.load(os.path.join("Images/Quiz", "q3.5B.png"))
            q3BHover = pygame.image.load(os.path.join("Images/Quiz", "q3.5Bhover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q3BG, [0, 0])
                checker(370, 295, 300, 50, q3A, q3AHover, "failed")  # x,y, width, height
                checker(370, 355, 300, 50, q3B, q3BHover, "passed")
                pygame.display.update()

        def quizFour():  # Answer: A
            q4BG = pygame.image.load(os.path.join("Images/Quiz", "question4.5.png"))
            q4A = pygame.image.load(os.path.join("Images/Quiz", "q4.5A.png"))
            q4AHover = pygame.image.load(os.path.join("Images/Quiz", "q4.5Ahover.png"))
            q4B = pygame.image.load(os.path.join("Images/Quiz", "q4.5B.png"))
            q4BHover = pygame.image.load(os.path.join("Images/Quiz", "q4.5Bhover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q4BG, [0, 0])
                checker(370, 320, 300, 50, q4A, q4AHover, "passed")  # x,y, width, height
                checker(370, 380, 300, 50, q4B, q4BHover, "failed")
                pygame.display.update()

        def quizFive():  # Answer: B
            q5BG = pygame.image.load(os.path.join("Images/Quiz", "question5.5.png"))
            q5A = pygame.image.load(os.path.join("Images/Quiz", "q5.5A.png"))
            q5AHover = pygame.image.load(os.path.join("Images/Quiz", "q5.5Ahover.png"))
            q5B = pygame.image.load(os.path.join("Images/Quiz", "q5.5B.png"))
            q5BHover = pygame.image.load(os.path.join("Images/Quiz", "q5.5Bhover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q5BG, [0, 0])
                checker(370, 315, 300, 50, q5A, q5AHover, "failed")  # x,y, width, height
                checker(370, 375, 300, 50, q5B, q5BHover, "passed")
                pygame.display.update()

        def quizSix():  # Answer: A
            q6BG = pygame.image.load(os.path.join("Images/Quiz", "question6.5.png"))
            q6A = pygame.image.load(os.path.join("Images/Quiz", "q6.5A.png"))
            q6AHover = pygame.image.load(os.path.join("Images/Quiz", "q6.5Ahover.png"))
            q6B = pygame.image.load(os.path.join("Images/Quiz", "q6.5B.png"))
            q6BHover = pygame.image.load(os.path.join("Images/Quiz", "q6.5Bhover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q6BG, [0, 0])
                checker(370, 315, 300, 50, q6A, q6AHover, "passed")  # x,y, width, height
                checker(370, 370, 300, 50, q6B, q6BHover, "failed")
                pygame.display.update()

        def quizSeven():  # Answer: B
            q7BG = pygame.image.load(os.path.join("Images/Quiz", "question7.5.png"))
            q7A = pygame.image.load(os.path.join("Images/Quiz", "q7.5A.png"))
            q7AHover = pygame.image.load(os.path.join("Images/Quiz", "q7.5Ahover.png"))
            q7B = pygame.image.load(os.path.join("Images/Quiz", "q7.5B.png"))
            q7BHover = pygame.image.load(os.path.join("Images/Quiz", "q7.5Bhover.png"))
            q7C = pygame.image.load(os.path.join("Images/Quiz", "q7.5C.png"))
            q7CHover = pygame.image.load(os.path.join("Images/Quiz", "q7.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q7BG, [0, 0])
                checker(370, 255, 300, 50, q7A, q7AHover, "failed")  # x,y, width, height
                checker(370, 315, 300, 50, q7B, q7BHover, "passed")
                checker(370, 375, 300, 50, q7C, q7CHover, "failed")
                pygame.display.update()

        def quizEight():  # Answer: C
            q8BG = pygame.image.load(os.path.join("Images/Quiz", "question8.5.png"))
            q8A = pygame.image.load(os.path.join("Images/Quiz", "q8.5A.png"))
            q8AHover = pygame.image.load(os.path.join("Images/Quiz", "q8.5Ahover.png"))
            q8B = pygame.image.load(os.path.join("Images/Quiz", "q8.5B.png"))
            q8BHover = pygame.image.load(os.path.join("Images/Quiz", "q8.5Bhover.png"))
            q8C = pygame.image.load(os.path.join("Images/Quiz", "q8.5C.png"))
            q8CHover = pygame.image.load(os.path.join("Images/Quiz", "q8.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q8BG, [0, 0])
                checker(370, 245, 300, 50, q8A, q8AHover, "failed")  # x,y, width, height
                checker(370, 305, 300, 50, q8B, q8BHover, "failed")
                checker(370, 365, 300, 50, q8C, q8CHover, "passed")
                pygame.display.update()

        def quizNine():  # Answer: A
            q9BG = pygame.image.load(os.path.join("Images/Quiz", "question9.5.png"))
            q9A = pygame.image.load(os.path.join("Images/Quiz", "q9.5A.png"))
            q9AHover = pygame.image.load(os.path.join("Images/Quiz", "q9.5Ahover.png"))
            q9B = pygame.image.load(os.path.join("Images/Quiz", "q9.5B.png"))
            q9BHover = pygame.image.load(os.path.join("Images/Quiz", "q9.5Bhover.png"))
            q9C = pygame.image.load(os.path.join("Images/Quiz", "q9.5C.png"))
            q9CHover = pygame.image.load(os.path.join("Images/Quiz", "q9.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q9BG, [0, 0])
                checker(370, 245, 300, 50, q9A, q9AHover, "passed")  # x,y, width, height
                checker(370, 305, 300, 50, q9B, q9BHover, "failed")
                checker(370, 365, 300, 50, q9C, q9CHover, "failed")
                pygame.display.update()

        def quizTen():  # Answer: A
            q10BG = pygame.image.load(os.path.join("Images/Quiz", "question10.5.png"))
            q10A = pygame.image.load(os.path.join("Images/Quiz", "q10.5A.png"))
            q10AHover = pygame.image.load(os.path.join("Images/Quiz", "q10.5Ahover.png"))
            q10B = pygame.image.load(os.path.join("Images/Quiz", "q10.5B.png"))
            q10BHover = pygame.image.load(os.path.join("Images/Quiz", "q10.5Bhover.png"))
            q10C = pygame.image.load(os.path.join("Images/Quiz", "q10.5C.png"))
            q10CHover = pygame.image.load(os.path.join("Images/Quiz", "q10.5Chover.png"))

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q10BG, [0, 0])
                checker(370, 255, 300, 50, q10A, q10AHover, "passed")  # x,y, width, height
                checker(370, 315, 300, 50, q10B, q10BHover, "failed")
                checker(370, 375, 300, 50, q10C, q10CHover, "failed")
                pygame.display.update()

        functions = [quizOne, quizTwo, quizThree, quizFour, quizFive, quizSix, quizSeven, quizEight, quizNine, quizTen]
        while True:
            fn = random.choice(functions)
            fn()

    def levelCompleted5():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                triviaFive()
                clock.tick(30)

    def triviaFive():
        trivia1 = pygame.image.load(os.path.join("Images/Trivias", "Trivia1Level5.png"))
        trivia2 = pygame.image.load(os.path.join("Images/Trivias", "Trivia2Level5.png"))
        trivia3 = pygame.image.load(os.path.join("Images/Trivias", "Trivia3Level5.png"))
        trivia4 = pygame.image.load(os.path.join("Images/Trivias", "Trivia4Level5.png"))
        trivia5 = pygame.image.load(os.path.join("Images/Trivias", "Trivia5Level5.png"))
        trivia6 = pygame.image.load(os.path.join("Images/Trivias", "Trivia6Level5.png"))
        trivia7 = pygame.image.load(os.path.join("Images/Trivias", "Trivia7Level5.png"))
        trivia8 = pygame.image.load(os.path.join("Images/Trivias", "Trivia8Level5.png"))
        trivia9 = pygame.image.load(os.path.join("Images/Trivias", "Trivia9Level5.png"))
        trivia10 = pygame.image.load(os.path.join("Images/Trivias", "Trivia10Level5.png"))
        randomList = random.choice((trivia1, trivia2, trivia3, trivia4, trivia5, trivia6, trivia7, trivia8, trivia9, trivia10))

        def button(x, y, w, h, image, imageOn, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()  # py collects left middle right button; (1,0,0) -leftclick; (0,0,1)rightclick

            rect = pygame.Rect(x, y, w, h)
            on_button = rect.collidepoint(mouse)

            if on_button:  # if x+width > mouseposition[0] right side of box > x and y loc + height wch is the bottom of the box
                screen.blit(imageOn, imageOn.get_rect(center=rect.center))
            else:
                screen.blit(image, image.get_rect(center=rect.center))

            if on_button:
                if click[0] == 1 and action != None:
                    if action == "continue":
                        quiz5()

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

    def mainTrivia5():
        while True:
            levelCompleted5()

    def main5():
        # Game Loop
        global gameSpeed, posXBg, posYBg, scorePoints, obstacles
        run = True
        star = FinishStar()
        player = Character()
        cloud = Cloud()
        gameSpeed = 29
        posXBg = 0
        posYBg = 350
        scorePoints = 0
        obstacles = []
        death_count = 0

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            screen.fill((194, 194, 194))
            playerInput = pygame.key.get_pressed()

            background5()

            if len(obstacles) == 0:
                if random.randint(0, 2) == 0:
                    obstacles.append(SpaceBlocks(Space))
                elif random.randint(0, 1) == 0:
                    obstacles.append(Trees(SpaceTree))
                elif random.randint(0, 1) == 0:
                    obstacles.append(Meteors(Meteor))

            player.draw(screen)
            player.update(playerInput)

            cloud.draw(screen)
            cloud.update()

            score5()

            for obstacle in obstacles:
                obstacle.draw(screen)
                obstacle.update()
                if player.character_rect.colliderect(obstacle.rect):
                    pygame.time.delay(200)
                    death_count += 1
                    menu5(death_count)

            if scorePoints >= 670:
                star.draw(screen)
                star.update()
                if player.character_rect.colliderect(star.rect):
                    font = pygame.font.Font('Fonts/Bubblebody.ttf', 22)
                    font1 = pygame.font.Font('Fonts/Affogato-Bold.otf', 20)
                    font2 = pygame.font.Font('Fonts/Billgis - Personal Use.ttf', 38)
                    font3 = pygame.font.Font('Fonts/Affogato-Medium.otf', 31)
                    background_image = pygame.image.load(os.path.join("Images/Start", "Level5Complete.png"))
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
                    mainTrivia5()

            pygame.display.update()
            clock.tick(30)

    menu5(death_count=0)
