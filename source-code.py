import pygame
import time
import random

pygame.init()

# R,G,B - SomeColors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (17, 124, 47)
blue = (0, 0, 255)

#LoadingImages
sunImg = pygame.image.load("background.jpg")
rocketImg = pygame.image.load("pixrocketimage.png")
clickedRocketImg = pygame.image.load("clickedrocket.png")
rocket2Img = pygame.image.load("rocket2image.png")
clickedRocket2Img = pygame.image.load("clickedrocket2.png")
fuelImg = pygame.image.load("fuelimage.jpg")
bombImg = pygame.image.load("bombimage.png")
planetImg = pygame.image.load("planetimage.png")
startImg = pygame.image.load("starticon.png")
quitImg = pygame.image.load("quiticon.png")
titleImg = pygame.image.load("titleicon.png")
clickStartImg = pygame.image.load("clickedStartIcon.png")
clickQuitImg = pygame.image.load("clickedQuitIcon.png")
selectText = pygame.image.load("selectscreentext.png")

#SettingFrame
display_width = 750
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("SPACE CRASH GAME BY THE INSIDE CODES")

#SettingClock
clock = pygame.time.Clock()

#PlayerClassParameters
playerparms = []
rocket1parms = [rocketImg, 5, 377, 450, 36, 30, 1.1]
rocket2parms = [rocket2Img,3.5,380,510,30,25, 1.02]
#ButtonClass
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))
#ButtonsForCharacterSelection
class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms.append(parms[0])
                playerparms.append(parms[1])
                playerparms.append(parms[2])
                playerparms.append(parms[3])
                playerparms.append(parms[4])
                playerparms.append(parms[5])
                playerparms.append(parms[6])
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

# BackgroundClass
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))

# PlayerClass
class Player:
    def __init__(self,p_img,speedIn,rocket_x,rocket_y,hitbox_x,hitbox_y,speedmultiplier):
        self.speed = speedIn
        self.rocket_x = rocket_x
        self.rocket_y = rocket_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier


# GameObjectsClass
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, white)
    gameDisplay.blit(text, (0, 0))

# CrashFunction/MessageDisplay
def text_objects(text, font):
    textsurface = font.render(text, True, blue)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash(message):
    message_display(message)

#QuitFunction
def quitgame():
    pygame.quit()
    quit()

#MainMenu
def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)

        titletext = gameDisplay.blit(titleImg, (275,200))
        startButton = Button(startImg,280,260,60,20,clickStartImg,273,258,selectScreen)
        quitButton = Button(quitImg,475,260,60,20,clickQuitImg,470,258,quitgame)

        pygame.display.update()
        clock.tick(15)

#CharacterSelect
def selectScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        gameDisplay.blit(selectText,(200,150))
        rocketSelect = Button2(rocketImg, 280,260,40,150,clickedRocketImg,278,226,rocket1parms,game_loop)
        rocket2select = Button2(rocket2Img,480,260,40,100, clickedRocket2Img,479,239,rocket2parms,game_loop)

        pygame.display.update()
        clock.tick(15)

#MainGame
def game_loop():
#CreatingObjects
    rocket = Player(playerparms[0],playerparms[1],playerparms[2],playerparms[3],playerparms[4],playerparms[5],playerparms[6])
    fuel = Gameobject(fuelImg, 5, random.randrange(0, display_width - 20),-600,40,35)
    bomb1 = Gameobject(bombImg, 3, random.randrange(0, display_width - 20),-600,40,35)
    bomb2 = Gameobject(bombImg, 3, random.randrange(0, display_width - 20),-1000,40,35)
    planet = Gameobject(planetImg, 4, random.randrange(0, display_width - 20),random.randrange(-2000, -1000),55,100)
#Constants
    x_change = 0
    score = 0

    gameexit = False
#GameLoop
    while not gameexit:

#Background
        gameDisplay.fill(black)
        bg = Background(sunImg, 0, 0)
# Objects
        gameDisplay.blit(fuel.b_image, (fuel.coord_x, fuel.coord_y))
        gameDisplay.blit(bomb1.b_image, (bomb1.coord_x, bomb1.coord_y))
        gameDisplay.blit(bomb2.b_image, (bomb2.coord_x, bomb2.coord_y))
        gameDisplay.blit(planet.b_image, (planet.coord_x, planet.coord_y))
#Player
        gameDisplay.blit(rocket.p_img, (rocket.rocket_x,rocket.rocket_y))

#Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and rocket.rocket_x > 0:
                    x_change = rocket.speed*-1 + -1*rocket.speedmult*score
                elif event.key == pygame.K_RIGHT and rocket.rocket_x < display_width - 45:
                    x_change = rocket.speed + rocket.speedmult*score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        rocket.rocket_x += x_change

        # print(event)

# ObjectSpeeds
        fuel.coord_y += fuel.speed
        bomb1.coord_y += bomb1.speed + 1.2 * score
        bomb2.coord_y += bomb1.speed + 1.2 * score
        planet.coord_y += planet.speed
        # if score >= 1:
        # vac_y += 10

# Boundaries
        if rocket.rocket_x > display_width - rocket.hitbox_x or rocket.rocket_x < 0:
            x_change = 0

# RecallingObjects
        if fuel.coord_y > display_height:
            fuel.coord_y = -10
            fuel.coord_x = random.randrange(0, display_width - 25)
        if bomb1.coord_y > display_height - 10:
            bomb1.coord_y = -10
            bomb1.coord_x = random.randrange(0, display_width - 25)
        if bomb2.coord_y > display_height:
            bomb2.coord_y = -410
            bomb2.coord_x = random.randrange(0, display_width - 25)
        if planet.coord_y > display_height:
            planet.coord_y = -2000
            planet.coord_x = random.randrange(0, display_width - 56)
# Score
        scorecounter(score)

# Collisons
    # bomb
        if rocket.rocket_y < bomb1.coord_y + bomb1.hitbox_y and rocket.rocket_y > bomb1.coord_y or rocket.rocket_y + rocket.hitbox_y > bomb1.coord_y and rocket.rocket_y + rocket.hitbox_y < bomb1.coord_y + bomb1.hitbox_y:
            if rocket.rocket_x > bomb1.coord_x and rocket.rocket_x < bomb1.coord_x + bomb1.hitbox_x or rocket.rocket_x + rocket.hitbox_x > bomb1.coord_x and rocket.rocket_x + rocket.hitbox_x < bomb1.coord_x + bomb1.hitbox_x:
                crash("Rocket got headburst")
                # Choc2
        if rocket.rocket_y < bomb2.coord_y + bomb2.hitbox_y and rocket.rocket_y > bomb2.coord_y or rocket.rocket_y + rocket.hitbox_y > bomb2.coord_y and rocket.rocket_y + rocket.hitbox_y < bomb2.coord_y + bomb2.hitbox_y:
            if rocket.rocket_x > bomb2.coord_x and rocket.rocket_x < bomb2.coord_x + bomb2.hitbox_x or rocket.rocket_x + rocket.hitbox_x > bomb2.coord_x and rocket.rocket_x + rocket.hitbox_x < bomb2.coord_x + bomb2.hitbox_x:
                crash("Rocket got headburst")
    # planet
        if rocket.rocket_y < planet.coord_y + planet.hitbox_y:
            if rocket.rocket_x > planet.coord_x and rocket.rocket_x < planet.coord_x + planet.hitbox_x or rocket.rocket_x + rocket.hitbox_x > planet.coord_x and rocket.rocket_x + rocket.hitbox_x < planet.coord_x + planet.hitbox_x:
                crash("Rocket got crashed!")
    # fuel
        if rocket.rocket_y < fuel.coord_y + fuel.hitbox_y and rocket.rocket_y > fuel.coord_y or rocket.rocket_y + rocket.hitbox_y > fuel.coord_y and rocket.rocket_y + rocket.hitbox_y < fuel.coord_y + fuel.hitbox_y:
            if rocket.rocket_x > fuel.coord_x and rocket.rocket_x < fuel.coord_x + fuel.hitbox_x or rocket.rocket_x + rocket.hitbox_x > fuel.coord_x and rocket.rocket_x + rocket.hitbox_x < fuel.coord_x + fuel.hitbox_x:
                fuel.coord_y = -10
                fuel.coord_x = random.randrange(0, display_width - 25)
                score += 1
                print(score)

        pygame.display.update()
        clock.tick(60)

mainmenu()
selectScreen()
game_loop()
pygame.QUIT()
quit()
