import Level2

def quiz():
    import pygame
    import os
    import random

    pygame.init()

    screenHeight = 550
    screenWidth = 1000
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()

    pygame.display.set_caption("Code Blocks: Learn the Basics of Python")

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
                        Level2.stageTwo()

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
                        fn()

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