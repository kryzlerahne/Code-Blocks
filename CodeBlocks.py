import pygame
import os
import random
import sys
import TriviaLvl1

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
                TriviaLvl1.mainTrivia()

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

