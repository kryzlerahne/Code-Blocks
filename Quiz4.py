import Level5

def quiz4():
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
                        Level5.stageFive()

        background = pygame.image.load(os.path.join("Images/Quiz", "Level4Passed.png"))
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

        background = pygame.image.load(os.path.join("Images/Quiz", "Level4Failed.png"))
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
        q1BG = pygame.image.load(os.path.join("Images/Quiz", "question1.4.png"))
        q1A = pygame.image.load(os.path.join("Images/Quiz", "q1.4A.png"))
        q1AHover = pygame.image.load(os.path.join("Images/Quiz", "q1.4Ahover.png"))
        q1B = pygame.image.load(os.path.join("Images/Quiz", "q1.4B.png"))
        q1BHover = pygame.image.load(os.path.join("Images/Quiz", "q1.4Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q1BG, [0, 0])
                checker(370, 315, 300, 50, q1A, q1AHover, "failed") #x,y, width, height
                checker(370, 375, 300, 50, q1B, q1BHover, "passed")
                pygame.display.update()


    def quizTwo(): #Answer: B
        q2BG = pygame.image.load(os.path.join("Images/Quiz", "question2.4.png"))
        q2A = pygame.image.load(os.path.join("Images/Quiz", "q2.4A.png"))
        q2AHover = pygame.image.load(os.path.join("Images/Quiz", "q2.4Ahover.png"))
        q2B = pygame.image.load(os.path.join("Images/Quiz", "q2.4B.png"))
        q2BHover = pygame.image.load(os.path.join("Images/Quiz", "q2.4Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q2BG, [0, 0])
                checker(370, 310, 300, 50, q2A, q2AHover, "failed") #x,y, width, height
                checker(370, 370, 300, 50, q2B, q2BHover, "passed")
                pygame.display.update()


    def quizThree(): #Answer: C
        q3BG = pygame.image.load(os.path.join("Images/Quiz", "question3.4.png"))
        q3A = pygame.image.load(os.path.join("Images/Quiz", "q3.4A.png"))
        q3AHover = pygame.image.load(os.path.join("Images/Quiz", "q3.4Ahover.png"))
        q3B = pygame.image.load(os.path.join("Images/Quiz", "q3.4B.png"))
        q3BHover = pygame.image.load(os.path.join("Images/Quiz", "q3.4Bhover.png"))
        q3C = pygame.image.load(os.path.join("Images/Quiz", "q3.4C.png"))
        q3CHover = pygame.image.load(os.path.join("Images/Quiz", "q3.4Chover.png"))


        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q3BG, [0, 0])
                checker(370, 255, 300, 50, q3A, q3AHover, "failed") #x,y, width, height
                checker(370, 315, 300, 50, q3B, q3BHover, "failed")
                checker(370, 375, 300, 50, q3C, q3CHover, "passed")
                pygame.display.update()


    def quizFour(): #Answer: A
        q4BG = pygame.image.load(os.path.join("Images/Quiz", "question4.4.png"))
        q4A = pygame.image.load(os.path.join("Images/Quiz", "q4.4A.png"))
        q4AHover = pygame.image.load(os.path.join("Images/Quiz", "q4.4Ahover.png"))
        q4B = pygame.image.load(os.path.join("Images/Quiz", "q4.4B.png"))
        q4BHover = pygame.image.load(os.path.join("Images/Quiz", "q4.4Bhover.png"))
        q4C = pygame.image.load(os.path.join("Images/Quiz", "q4.4C.png"))
        q4CHover = pygame.image.load(os.path.join("Images/Quiz", "q4.4Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q4BG, [0, 0])
                checker(370, 255, 300, 50, q4A, q4AHover, "passed") #x,y, width, height
                checker(370, 315, 300, 50, q4B, q4BHover, "failed")
                checker(370, 370, 300, 50, q4C, q4CHover, "failed")
                pygame.display.update()


    def quizFive(): #Answer: A
        q5BG = pygame.image.load(os.path.join("Images/Quiz", "question5.4.png"))
        q5A = pygame.image.load(os.path.join("Images/Quiz", "q5.4A.png"))
        q5AHover = pygame.image.load(os.path.join("Images/Quiz", "q5.4Ahover.png"))
        q5B = pygame.image.load(os.path.join("Images/Quiz", "q5.4B.png"))
        q5BHover = pygame.image.load(os.path.join("Images/Quiz", "q5.4Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q5BG, [0, 0])
                checker(370, 315, 300, 50, q5A, q5AHover, "passed") #x,y, width, height
                checker(370, 375, 300, 50, q5B, q5BHover, "failed")
                pygame.display.update()


    def quizSix(): #Answer: B
        q6BG = pygame.image.load(os.path.join("Images/Quiz", "question6.4.png"))
        q6A = pygame.image.load(os.path.join("Images/Quiz", "q6.4A.png"))
        q6AHover = pygame.image.load(os.path.join("Images/Quiz", "q6.4Ahover.png"))
        q6B = pygame.image.load(os.path.join("Images/Quiz", "q6.4B.png"))
        q6BHover = pygame.image.load(os.path.join("Images/Quiz", "q6.4Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q6BG, [0, 0])
                checker(370, 300, 300, 50, q6A, q6AHover, "failed") #x,y, width, height
                checker(370, 355, 300, 50, q6B, q6BHover, "passed")
                pygame.display.update()


    def quizSeven(): #Answer: B
        q7BG = pygame.image.load(os.path.join("Images/Quiz", "question7.4.png"))
        q7A = pygame.image.load(os.path.join("Images/Quiz", "q7.4A.png"))
        q7AHover = pygame.image.load(os.path.join("Images/Quiz", "q7.4Ahover.png"))
        q7B = pygame.image.load(os.path.join("Images/Quiz", "q7.4B.png"))
        q7BHover = pygame.image.load(os.path.join("Images/Quiz", "q7.4Bhover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q7BG, [0, 0])
                checker(370, 300, 300, 50, q7A, q7AHover, "failed") #x,y, width, height
                checker(370, 355, 300, 50, q7B, q7BHover, "passed")
                pygame.display.update()


    def quizEight(): #Answer: A
        q8BG = pygame.image.load(os.path.join("Images/Quiz", "question8.4.png"))
        q8A = pygame.image.load(os.path.join("Images/Quiz", "q8.4A.png"))
        q8AHover = pygame.image.load(os.path.join("Images/Quiz", "q8.4Ahover.png"))
        q8B = pygame.image.load(os.path.join("Images/Quiz", "q8.4B.png"))
        q8BHover = pygame.image.load(os.path.join("Images/Quiz", "q8.4Bhover.png"))
        q8C = pygame.image.load(os.path.join("Images/Quiz", "q8.4C.png"))
        q8CHover = pygame.image.load(os.path.join("Images/Quiz", "q8.4Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q8BG, [0, 0])
                checker(370, 255, 300, 50, q8A, q8AHover, "passed") #x,y, width, height
                checker(370, 315, 300, 50, q8B, q8BHover, "failed")
                checker(370, 375, 300, 50, q8C, q8CHover, "failed")
                pygame.display.update()


    def quizNine(): #Answer: C
        q9BG = pygame.image.load(os.path.join("Images/Quiz", "question9.4.png"))
        q9A = pygame.image.load(os.path.join("Images/Quiz", "q9.4A.png"))
        q9AHover = pygame.image.load(os.path.join("Images/Quiz", "q9.4Ahover.png"))
        q9B = pygame.image.load(os.path.join("Images/Quiz", "q9.4B.png"))
        q9BHover = pygame.image.load(os.path.join("Images/Quiz", "q9.4Bhover.png"))
        q9C = pygame.image.load(os.path.join("Images/Quiz", "q9.4C.png"))
        q9CHover = pygame.image.load(os.path.join("Images/Quiz", "q9.4Chover.png"))

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
        q10BG = pygame.image.load(os.path.join("Images/Quiz", "question10.4.png"))
        q10A = pygame.image.load(os.path.join("Images/Quiz", "q10.4A.png"))
        q10AHover = pygame.image.load(os.path.join("Images/Quiz", "q10.4Ahover.png"))
        q10B = pygame.image.load(os.path.join("Images/Quiz", "q10.4B.png"))
        q10BHover = pygame.image.load(os.path.join("Images/Quiz", "q10.4Bhover.png"))
        q10C = pygame.image.load(os.path.join("Images/Quiz", "q10.4C.png"))
        q10CHover = pygame.image.load(os.path.join("Images/Quiz", "q10.4Chover.png"))

        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                screen.blit(q10BG, [0, 0])
                checker(370, 255, 300, 50, q10A, q10AHover, "passed") #x,y, width, height
                checker(370, 315, 300, 50, q10B, q10BHover, "failed")
                checker(370, 375, 300, 50, q10C, q10CHover, "failed")
                pygame.display.update()

    functions = [quizOne, quizTwo, quizThree, quizFour, quizFive, quizSix, quizSeven, quizEight, quizNine, quizTen]
    while True:
            fn = random.choice(functions)
            fn()
