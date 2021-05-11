################################
# Name: Barry Cimring
# Date: 19/11/2019
# File Name: flappygolf_C4LASS.py
###############################

import pygame
from flappygolf_CLASS import *
pygame.init()

WIDTH = 1020
LENGTH = 750
screen = pygame.display.set_mode((WIDTH,LENGTH))

# load grass,dirt,sand,lava,hole1,hole2,level 10 imgs

####################################
#   Levels                         #
####################################

# levels list organized by lists within lists
# level = [water objects, grass objects, sand objects, hole objects, level par]
# second item in hole list is where hole is on the object surface

# level 1
level1 = [[Water(1000,550,10,5)],
           [Grass(0,675,61,3),Grass(0,0,60,2),Grass(0,0,2,27),Grass(1475,0,2,27),Grass(50,350,10,13),Grass(650,425,14,16)],
           [Sand(300,500,14,7)],
           [Hole(1225,500,10,7,3),3],
           [5,8,11]]
# level 2
level2 = [[],
          [Grass(0,675,61,3),Grass(0,-75,60,2),Grass(-50,0,2,30),Grass(1475,0,2,27),Grass(0,200,10,22)],
          [Sand(250,625,24,2),Sand(1100,625,15,2)],
          [Hole(850,575,10,10,4),4],
          [5,7,10]]

# level 3
level3 = [[Water(650,600,10,5)],
          [Grass(0,675,56,3),Grass(0,0,55,2),Grass(0,0,2,27),Grass(1350,0,2,27),Grass(50,550,10,5),Grass(550,0,4,12),Grass(550,425,4,10)],
          [],
          [Hole(850,250,20,17,15),15],
          [6,9,12]]

# level 4
level4 = [[],
          [Grass(0,675,61,3),Grass(0,0,60,2),Grass(0,0,2,27),Grass(1475,0,2,27),Grass(50,250,25,18),Grass(875,0,24,16)],
          [Sand(675,650,25,2)],
          [Hole(1225,625,10,3,3),3],
          [5,7,9]]

# level 5
level5 = [[Water(450,625,16,2),Water(200+25*32,625,10,2)],
          [Grass(0,675,60,3),Grass(0,0,59,2),Grass(0,0,2,27),Grass(1450,0,2,27),Grass(50,550,10,5),Grass(300,275,6,17),Grass(600,0,4,17),Grass(200+26*25,250,6,17),Grass(500+26*25,0,13,16)],
          [],
          [Hole(500+30*25,625,8,2,5),5],
          [11,14,18]] 

# level 6
level6 = [[],
          [Grass(40*20,650,46,3),Grass(0,0,45,2),Grass(0,0,2,30),Grass(44*25,0,2,27),Grass(50,300,35,5)],
          [Sand(15*25,650,20,5)],
          [Hole(50,625,13,7,5),5],
          [8,10,13]] 

# level 7
level7 = [[Water(600-5*25,250,5,4),Water(600+11*25,250,5,4)],
          [Grass(0,650,46,3),Grass(0,0,45,2),Grass(0,0,2,27),Grass(44*25,0,2,27),Grass(50,650,42,3),Grass(600-6*25,250,1,4),Grass(600+16*25,250,1,4)],
          [],
          [Hole(600,250,11,4,6),6],
          [6,9,13]] 

# level 8
level8 = [[],
          [Grass(0,650,60,3),Grass(0,-100,60,3),Grass(0,0,2,27),Grass(58*25,0,2,27),Grass(50,650,42,3),Grass(600-5*25,175,4,19),Grass(700-13*25,375,2,12),Grass(50+15*25,675-17*25,2,17),
           Grass(600+6*25,176,4,19),Grass(900,226+6*25,2,12),Grass(850,650-17*25,2,17)],
          [Sand(23*25,225+3*25,7,15)],
          [Hole(43*25,600,15,2,10),6],
          [7,10,14]] 

# level 9
level9 = [[Water(250,600,50,4),Water(25*61,600,14,4)],
          [Grass(0,700,125,3),Grass(0,-100,120,3),Grass(0,0,2,29),Grass(103*25,0,2,29),Grass(50,301,8,26),Grass(50+25*17,-50,6,18),Grass(50+25*17,-50,6,18),
           Grass(50+25*30,-50,6,18),Grass(50+25*43,-50,6,18),Grass(25*63,-50,8,7),Grass(25*63,275,8,6),Grass(25*75,600,5,4),Grass(25*80,300,6,21)],
          [Sand(51*25,600,10,4),Sand(25*86,400,14,14)],
          [Hole(99*25,299,4,19,1),1],
          [11,15,20]] 

# level 10
bonusLevel = [[Water(10*25,575,46,4)],
          [Grass(0,675,61,3),Grass(0,-50,60,2),Grass(-50,-25,2,30),Grass(1500,0,2,27),Grass(0,150,10,24),
           Grass(700,201,5,3),Grass(425,400,6,2),Grass(900,475,5,3),Grass(1200,200,6,6)],
          [],
          [Hole(850+22*25,575,4,10,1),1],
          [5,7,10]]



levels = [level1,level2,level3,level4,level5,level6,level7,level8,level9,bonusLevel] # compiled list of all levels (3-dimensional)
levelData = [None]*10                                                                # list for values of level stars

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
# if one cannot get all gold for bonus, uncomment this line #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

#levelData = ["Gold","Gold","Gold","Gold","Gold","Gold","Gold","Gold","Gold",None]   


####################################
#   Colours                        #
####################################

black = (0,0,0)
white = (255,255,255)
yellow = (244, 223, 66)
beige = (252, 238, 207)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

####################################
#   Sound                          #
####################################
flap = pygame.mixer.Sound('audio\\flap.wav')
flap.set_volume(0.3)
explosionSound = pygame.mixer.Sound('audio\\explosion.wav')
explosionSound.set_volume(0.2)

####################################
#   Images                         #
####################################

intro = pygame.image.load('graphics\\intro.jpg')                              
intro = intro.convert_alpha()
intro = pygame.transform.scale(intro,(1020,750))                    # intro screen background
    
rule_button = pygame.image.load('graphics\\rule_button.jpg')                  
rule_button = rule_button.convert_alpha()
big_rule_button = pygame.transform.scale(rule_button,(620,200))     # rule button for rule screen
rule_button = pygame.transform.scale(rule_button,(200,75))          # rule button for intro screen

levelImg = pygame.image.load('graphics\\levels.jpg')
levelImg = levelImg.convert_alpha()
levelImg = pygame.transform.scale(levelImg,(1020,750))              # background for level screen

level10 = pygame.image.load('graphics\\level10.png')
level10 = level10.convert_alpha()
level10 = pygame.transform.scale(level10,(175,155))                 # additional image for level 10 on level screen

goldStar = pygame.image.load('graphics\\goldStar.png')
goldStar = goldStar.convert_alpha()
goldStar = pygame.transform.scale(goldStar,(200,200))               # image for end game gold star

silverStar = pygame.image.load('graphics\\silverStar.png')
silverStar = silverStar.convert_alpha()
silverStar = pygame.transform.scale(silverStar,(200,200))           # image for end game silver star

bronzeStar = pygame.image.load('graphics\\bronzeStar.png')
bronzeStar = bronzeStar.convert_alpha()
bronzeStar = pygame.transform.scale(bronzeStar,(200,200))           # image for end game bronze star

goldStarInGame = pygame.transform.scale(goldStar,(60,60))           # image for in game gold star
silverStarInGame = pygame.transform.scale(silverStar,(60,60))       # image for in game silver star
bronzeStarInGame = pygame.transform.scale(bronzeStar,(60,60))       # image for in game bronze star
little_goldStar = pygame.transform.scale(goldStar,(40,40))          # image for level screen gold star
little_goldStar = pygame.transform.rotate(little_goldStar,10)       # rotate image 10 degrees cntr clockwise
little_silverStar = pygame.transform.scale(silverStar,(40,40))      # image for level screen silver star
little_silverStar = pygame.transform.rotate(little_silverStar,10)   # rotate image 10 degrees cntr clockwise
little_bronzeStar = pygame.transform.scale(bronzeStar,(40,40))      # image for level screen bronze star
little_bronzeStar = pygame.transform.rotate(little_bronzeStar,10)   # rotate image 10 degrees cntr clockwise

levelButton = pygame.image.load('graphics\\levels.png')
levelButton = levelButton.convert_alpha()
levelButton = pygame.transform.scale(levelButton,(80,80))           # image for level icon on pause and endlevel screens

retryButton = pygame.image.load('graphics\\retry.png')
retryButton = retryButton.convert_alpha()
retryButton = pygame.transform.scale(retryButton,(80,80))           # image for retry icon on pause and endlevel screens

homeButton = pygame.image.load('graphics\\home.png')
homeButton = homeButton.convert_alpha()
homeButton = pygame.transform.scale(homeButton,(80,80))             # image for home icon on pause and endlevel screens

playButton = pygame.image.load('graphics\\play.png')
playButton = playButton.convert_alpha()
playButton = pygame.transform.scale(playButton,(100,100))           # image for play icon on pause and endlevel screens

pauseButton = pygame.image.load('graphics\\pause.png')
pauseButton = pauseButton.convert_alpha()
pauseButton = pygame.transform.scale(pauseButton,(60,60))           # image for pause icon on game screen

endLevelFont = pygame.font.SysFont("Arial Rounded MT Bold",100)     # font for text on end level screen
inGameFont = pygame.font.SysFont("Bauhaus 93",60)                   # font for text in game
ruleFont = pygame.font.SysFont("Eras Light", 70)                    # font for text on rule screen
birdFont = pygame.font.SysFont("Agency FB", 30)                     # font for text on top of bird

sunnyImgs = ['graphics\\grass.png',
             'graphics\\dirt.png',
             'graphics\\sand.png',
             'graphics\\water.jpg',
             'graphics\\hole1.png',
             'graphics\\hole2.png',
             'graphics\\flag.png',
             'graphics\\background.png',
             'graphics\\waterWarning.png']              # images to load for regular levels
darkImgs = ['graphics\\rockDirtTop.png',
            'graphics\\rockDirt.png',
            'graphics\\obsid.png',
            'graphics\\lava.png',
            'graphics\\hole1.png',
            'graphics\\hole2.png',
            'graphics\\flag.png',
            'graphics\\hellBackground.png',
            'graphics\\lavaWarning.png']  # images to load for bonus level

####################################
#   Game Images                    #
####################################
def load_game_imgs(typeImg):                        # function for loading images for level type
    grass = pygame.image.load(typeImg[0])
    grass = grass.convert_alpha()
    grass = pygame.transform.scale(grass,(25,25))   # image for top of grass object
    dirt = pygame.image.load(typeImg[1])
    dirt = dirt.convert_alpha()
    dirt = pygame.transform.scale(dirt,(25,25))     # image for dirt in hole, grass, sand, and water objects
    sand = pygame.image.load(typeImg[2])
    sand = sand.convert_alpha()
    sand = pygame.transform.scale(sand,(25,25))     # image for top half of sand object
    water = pygame.image.load(typeImg[3])
    water = water.convert_alpha()
    water = pygame.transform.scale(water,(25,25))   # image for top half of water object
    hole1 = pygame.image.load(typeImg[4])
    hole1 = hole1.convert_alpha()
    hole1 = pygame.transform.scale(hole1,(25,25))   # image for left half of hole in hole object
    hole2 = pygame.image.load(typeImg[5])
    hole2 = hole2.convert_alpha()
    hole2 = pygame.transform.scale(hole2,(25,25))   # image for right half of hole in hole object
    flag = pygame.image.load(typeImg[6])
    flag = flag.convert_alpha()
    flag = pygame.transform.scale(flag,(60,80))     # image for flag in hole object
    background = pygame.image.load(typeImg[7])
    background = background.convert_alpha()
    background = pygame.transform.scale(background,(1020,750))      # image for in game background
    waterWarning = pygame.image.load(typeImg[8])
    waterWarning = waterWarning.convert_alpha()
    waterWarning = pygame.transform.scale(waterWarning,(420,150))   # image for bird landing in lava/water

    
    return grass,dirt,sand,water,hole1,hole2,flag,background,waterWarning   # return all images to be unpacked

####################################
#   Misc. Values                   #
####################################

explosions = []                                                         # lift for explosion sprite
for i in range(12):                                                     # for loop for loading explosion images
    explosions.append(pygame.image.load('animation_frames\\explosion\\Explosion'+str(i+1)+'.png'))   # load and append image to list
    explosions[i] = explosions[i].convert_alpha()                       
    explosions[i] = pygame.transform.scale(explosions[i],(180,180))     # convert it to pixels and resize it to 180x180 square


####################################
#   Functions                      #
####################################
def drawScreen():                                                       # funciton for redrawing game screen
    screen.blit(background,(background_x,background_y))                 # draw background 1
    screen.blit(background,(background_x2,background_y2))               # draw background 2
    birdHead = birdFont.render(str(flapCount),1,black)                  # render flap count in bird head text
    if not inHole:                                                      # if bird is not in hole
        screen.blit(birdHead,(birdie.x+15,birdie.y-40))                 # draw the flap count text
        birdie.draw(screen,direction,count)                             # draw the bird
                                    
    for i in range(len(grasses)):                                       # for loop for grass objects
        grasses[i].draw(screen,dirt,grass)                              # draw all grass objects
    for i in range(len(waters)):                                        # for loop for water objects
        waters[i].draw(screen,water,dirt,level)                         # draw all water objects
    for i in range(len(sands)):                                         # for loop for sand objects
        sands[i].draw(screen,sand,dirt)                                 # draw all sand objects
    hole.draw(screen,dirt,grass,hole1,hole2,flag)                       # draw the hole
    if 0 < explode < 60:                                                # if explode value is greater than 0 and less than 60
        screen.blit(explosions[explode//5],(hole.holex-65,hole.y-100))  # draw new explosion image above hole every 5 cycles
        
    pygame.draw.rect(screen,yellow,(940,10,60,60))                      # draw square for pause button
    screen.blit(pauseButton,(940,10))                                   # draw pause icon
    
    screen.blit(goldStarInGame,(50,10))                                 # draw in game gold star
    screen.blit(silverStarInGame,(200,10))                              # draw in game silver star
    screen.blit(bronzeStarInGame,(350,10))                              # draw in game bronze star
    goldFlaps = inGameFont.render(str(gold),1,white)                    # render number of flaps for a gold star
    silverFlaps = inGameFont.render(str(silver),1,white)                # render number of flaps for a silver star
    bronzeFlaps = inGameFont.render(str(bronze),1,white)                # render number of flaps for a bronze star
    screen.blit(goldFlaps,(130,10))                                     # draw text for gold star flaps
    screen.blit(silverFlaps,(280,10))                                   # draw text for silver star flaps
    screen.blit(bronzeFlaps,(430,10))                                   # draw text for bronze star flaps
    
    pygame.display.update()                                             # update screen

def intro_screen():                                                     # function for intro screen
    screen.blit(intro,(0,0))                                            # draw intro screen background                  
    screen.blit(rule_button,(410,20))                                   # draw rule button at the top
    pygame.display.update()                                             # update the screen

def rule_screen():                                                      # funciton for rule screen
    screen.blit(levelImg,(0,0))                                         # draw level screen background
    whiteback = pygame.Surface((1020,450))                              # create surface for text background
    whiteback.set_alpha(200)                                            # make 78% transparent
    screen.blit(whiteback,(0,200))                                      # draw translucent background
    screen.blit(big_rule_button,(200,0))                                # draw large rule button title

    rule1 = ruleFont.render("1. Every flap of the bird is counted",1,white)     # render rule 1 in rule font
    rule2 = ruleFont.render("2. Clicking the left and right halves",1,white)    # render rule 2 in rule font
    rule2_cont = ruleFont.render("of screen change speeds",1,white)             # render rule 2.5 in rule font
    rule3 = ruleFont.render("3. Level restarts if bird falls in water.",1,white)# render rule 3 in rule font
    rule4 = ruleFont.render("4. Bird does not bounce on sand.",1,white)         # render rule 4 in rule font
    rule5 = ruleFont.render("5. Level ends when bird falls in hole.",1,white)   # render rule 5 in rule font
    
    screen.blit(rule1,(50,205))                                         # draw rule 1
    screen.blit(rule2,(50,290))                                         # draw rule 2
    screen.blit(rule2_cont,(110,340))                                   # draw rule 2.5
    screen.blit(rule3,(50,420))                                         # draw rule 3
    screen.blit(rule4,(50,500))                                         # draw rule 4
    screen.blit(rule5,(50,580))                                         # draw rule 5
    
    pygame.display.update()                                             # update screen
    
def level_screen():                                         # function for level screen
    screen.blit(levelImg,(0,0))                             # draw level screen background
    rect = pygame.Surface((170,155))                        # create translucent background 
    rect.set_alpha(20)                                      # with 8% transparency
    rect.fill(black)                                        # fill with black
    for i in range(5):                                      # for loop in range of top row levels
        screen.blit(rect,(35+200*i,210))                    # outline each level with square indicating hit point
    for i in range(4):                                      # for loop in range of bottom row levels
        screen.blit(rect,(125+200*i,385))                   # outline each level with square indicating hit point
        
    for i in range(5):                                      # for loop in range of top row levels
        if levelData[i] == "Gold":                          # if player has gotten gold on the level
            screen.blit(little_goldStar,(145 + i*202,310))  # draw gold star in bottom right
        elif levelData[i] == "Silver":                      # if player has gotten silver on the level
            screen.blit(little_silverStar,(145 + i*202,310))# draw silver star in bottom right
        elif levelData[i] == "Bronze":                      # if player has gotten bronze on the level
            screen.blit(little_bronzeStar,(145 + i*202,310))# draw bronze star in bottom right
    for i in range(4):                                      # for loop in range of bottom row levels
        if levelData[i+5] == "Gold":                        # if player has gotten gold on the level
            screen.blit(little_goldStar,(235 + i*202,488))  # draw gold star in bottom right
        elif levelData[i+5] == "Silver":                    # if player has gotten silver on the level
            screen.blit(little_silverStar,(235 + i*202,488))# draw silver star in bottom right
        elif levelData[i+5] == "Bronze":                    # if player has gotten bronze on the level
            screen.blit(little_bronzeStar,(235 + i*202,488))# draw bronze star in bottom right
        
    if levelData.count("Gold") >= 9:                        # if player has gold on all 9 original levels
        screen.blit(level10,(415,560))                      # draw level 10 icon
        bonus = inGameFont.render("Bonus Level!",1,black)   # render bonus level text
        screen.blit(bonus,(65,600))                         # draw bonus level text
    if levelData[9] == "Gold":                              # if player has gold on last level
        screen.blit(little_goldStar,(535,665))              # draw gold star in bottom right corner
    pygame.display.update()                                 # update screen

def water_screen():                                         # function for when bird falls in water
    rect = pygame.Surface((1020,750))                       # create translucent surface
    rect.set_alpha(150)                                     # 60% transparency
    rect.fill(black)                                        # fill black
    screen.blit(rect,(0,0))                                 # draw on entire screen
    screen.blit(waterWarning,(300,300))                     # diplay water warning image in center
    pygame.display.update()                                 # update screen

def end_level(levelData):                                   # function for end of level screen
    rect = pygame.Surface((1020,750))                       # create translucent surface 
    rect.set_alpha(100)                                     # 40% transparency
    rect.fill(black)                                        # fill black
    screen.blit(rect,(0,0))                                 # draw on entire screen
    
    pygame.draw.rect(screen,yellow,(120,150,120,120))       # draw yellow rectangle for level icon
    screen.blit(levelButton,(140,170))                      # draw level icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(780,150,120,120))       # draw yellow rectangle for retry icon
    screen.blit(retryButton,(800,170))                      # draw retry icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(120,510,120,120))       # draw yellow rectangle for home icon
    screen.blit(homeButton,(140,530))                       # draw home icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(780,510,120,120))       # draw yellow rectangle for play icon
    screen.blit(playButton,(790,520))                       # draw play icon on yellow rectangle
    pygame.draw.rect(screen,beige,(310,222,400,325))        # draw beige rectangle for level data and star
    flaps = endLevelFont.render("FLAPS:",1,black)           # render flap count title
    flapCountData = endLevelFont.render(str(flapCount),1,black) # render flap count from level
    screen.blit(flapCountData,(610,242))                    # draw flap count data in beige recatngle
    screen.blit(flaps,(340,242))                            # draw flap title in beige rectangle
    if flapCount <= gold:                                   # if player got gold star
        screen.blit(goldStar,(420,330))                     # draw gold star
        levelData[level] = "Gold"                           # make level data list gold for level screen drawing
    elif gold < flapCount <= silver:                        # if player got silver star
        screen.blit(silverStar,(420,330))                   # draw silver star
        if levelData[level] != "Gold":                      # if player has not already gotten gold on the level
            levelData[level] = "Silver"                     # make level data silver for level screen drawing
    elif silver < flapCount <= bronze:                      # if player got bronze star
        screen.blit(bronzeStar,(420,330))                   # draw gold star
        if levelData[level] != "Gold" and levelData[level] != "Silver": # if player does not already have gold or silve star on the level
            levelData[level] = "Bronze"                     # make level data bronze for level screen drawing
        
    pygame.display.update()                                 # display on screen
    return levelData                                        # return altered level data list

def pause_screen():                                         # function for drawing pause screen
    rect = pygame.Surface((1020,750))                       # create translucent surface 
    rect.set_alpha(100)                                     # 40% transparency
    rect.fill(black)                                        # fill black
    screen.blit(rect,(0,0))                                 # draw on entire screen
    pygame.draw.rect(screen,yellow,(120,150,120,120))       # draw yellow rectangle for level icon
    screen.blit(levelButton,(140,170))                      # draw level icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(780,150,120,120))       # draw yellow rectangle for retry icon
    screen.blit(retryButton,(800,170))                      # draw retry icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(120,510,120,120))       # draw yellow rectangle for home icon
    screen.blit(homeButton,(140,530))                       # draw home icon on yellow rectangle
    pygame.draw.rect(screen,yellow,(780,510,120,120))       # draw yellow rectangle for play icon
    screen.blit(playButton,(790,520))                       # draw play icon on yellow rectangle
    
    pygame.display.update()                                 # display on screen
# STOP
def grassCollisions(count,grasses,hole):                    # function for collisions with grass objects
    for i in range(len(grasses)):                           # for loop with len of grass list
        grasses[i].CollidesSideBottom(birdie)               # check if birdie collided with side or bottom of any grass
    hole.CollidesSideBottom(birdie)                         # check if birdie collided with side or bottom of  hole object
        
    for i in range(len(grasses)):                           # for loop in range of grasses
        if birdie.rolling:                                  # if birdie is rolling
            if birdie.y == grasses[i].y-birdHeight:         # and birdie is on top of one of the grasses
                count = grasses[i].CollidesTop(birdie,count)# check collision with top of that grass object
                break                                       # break loop so it doesnt check the others
            elif birdie.y == hole.y-birdHeight:             # or if birdie is on top of the hole
                count = hole.CollidesTop(birdie,count)      # check collision with top of that hole object
                break                                       # break loop so it doesnt check the others
        else:                                               # if bird is not rolling
            count = hole.CollidesTop(birdie,count)          # check collision with top of hole
            if birdie.rolling:                              # if bird begins to roll
                break                                       # break loop
            count = grasses[i].CollidesTop(birdie,count)    # check collision with top of grass

    return count,grasses,hole                               # return the altered count, grasses and hole objects

def sandCollisions(sands):                                  # function for sand collisions
    for i in range(len(sands)):                             # for loop in range on sand list
        sands[i].CollidesTop(birdie)                        #
        sands[i].CollidesSideBottom(birdie)                 # check forsand collisions
    return sands                                            # return altered sand list, and count

def waterCollisions(count,waters,delay,fellInWater):        # funtion for water collision
    for i in range(len(waters)):                            # for loop in range of water
        count,delay,fellInWater = waters[i].Collides(birdie,count,delay,fellInWater)    # check for water collisions
        if fellInWater == True:                             # if bird fell in water
            return count,waters,delay,fellInWater           # quit funtion
    return count,waters,delay,fellInWater                   # return altered count, water list, delay and fell in water boolean

def move_backgroundx(birdie,background_x,background_x2,grasses,waters,sands,hole,direction):                # funtion to move the background
    if birdie.speed_x > 0:                                                                                  # if bird moving right
        direction = "right"                                                                                 # direction is right
    if birdie.speed_x < 0:                                                                                  # if bird moving left
        direction = "left"                                                                                  # direction is left

    if birdie.x < 150:                                                                                      # if birdie is left of 150
        if birdie.move_y != False or birdie.rolling == True:                                                # and bird is moving y or rolling
            if direction == "left":                                                                         # and direction is left
                if (background_x >= 0) and (background_x2 >= 1020) and (background_x2 > background_x):      # if background1 is to the right of screen and background2 is to the right of background1
                    background_x2 = -1010                                                                   # shift other background to the left side of background 1
                if (background_x2 >= 0) and (background_x >= 1020) and (background_x > background_x2):      # if background2 is to the right of screen and background1 is to the right of background1
                    background_x = -1010                                                                    # shift other background to the left side of background 2

                birdie.move_x = False                                                                       # stop moving bird
                if birdie.rolling == True:                                                                  # if bird is rolling
                    if birdie.rollCount < 200:                                                              # and roll count is less than 200
                        birdie.rollCount += 1                                                               # add to rollcount
                        birdie.speed_x *= (149/150)**birdie.rollCount                                       # multiply by frictional exponential expression
                    else:   
                        return birdie,background_x,background_x2,grasses,waters,sands,hole,direction        # or return items without moving
                        
                background_x += int(abs(birdie.speed_x))                                                    # add absolute integer of speed to all objects from obstacele
                background_x2 += int(abs(birdie.speed_x))                                                   # including background
                for i in range(len(grasses)):                                                               # and update them into new objects
                    grasses[i].x += int(abs(birdie.speed_x))                                                # 
                    grasses[i] = Grass(grasses[i].x,grasses[i].y,grasses[i].length,grasses[i].height)       # 
                for i in range(len(waters)):                                                                #
                    waters[i].x += int(abs(birdie.speed_x))                                                 #
                    waters[i] = Water(waters[i].x,waters[i].y,waters[i].length,waters[i].height)            # 
                for i in range(len(sands)):                                                                 # 
                    sands[i].x += int(abs(birdie.speed_x))                                                  # 
                    sands[i] = Sand(sands[i].x,sands[i].y,sands[i].length,sands[i].height)                  #
                hole.x += int(abs(birdie.speed_x))                                                          #
                hole = Hole(hole.x,hole.y,hole.length,hole.height,holePos)                                  # 
        birdie.x = 149                                                                                      # keep birdie below 150
                
    if birdie.x > 870:                                                                                      # if bird is greater than 870
        if birdie.move_y != False or birdie.rolling == True:                                                # and bird is moving y or rolling
            if direction == "right":                                                                        # andbird moving right
                if (background_x < -1020) and (background_x2 < 0) and (background_x < background_x2):       # if background1 is to the right of screen and background2 is to the right of background1
                    background_x = 1010                                                                     # shift other background to the left side of background 1
                if (background_x2 < -1020) and (background_x < 0) and (background_x > background_x2):       # if background2 is to the right of screen and background1 is to the right of background1
                    background_x2 = 1010                                                                    # shift other background to the left side of background 2
        
                birdie.move_x = False                                                                       # stop moving bird
                if birdie.rolling == True:                                                                  # if bird is rolling
                    if birdie.rollCount < 200:                                                              # and roll count is less than 200
                        birdie.rollCount += 1                                                               # add to rollcount
                        birdie.speed_x *= (149/150)**birdie.rollCount                                       # multiply by frictional exponential expression
                    else:   
                        return birdie,background_x,background_x2,grasses,waters,sands,hole,direction        # or return items without moving
                    
                background_x -= int(abs(birdie.speed_x))                                                    # add absolute integer of speed to all objects from obstacele
                background_x2 -= int(abs(birdie.speed_x))                                                   # including background
                for i in range(len(grasses)):                                                               # and update them into new objects
                    grasses[i].x -= int(abs(birdie.speed_x))                                                # 
                    grasses[i] = Grass(grasses[i].x,grasses[i].y,grasses[i].length,grasses[i].height)       # 
                for i in range(len(waters)):                                                                #
                    waters[i].x -= int(abs(birdie.speed_x))                                                 #
                    waters[i] = Water(waters[i].x,waters[i].y,waters[i].length,waters[i].height)            # 
                for i in range(len(sands)):                                                                 # 
                    sands[i].x -= int(abs(birdie.speed_x))                                                  # 
                    sands[i] = Sand(sands[i].x,sands[i].y,sands[i].length,sands[i].height)                  #
                hole.x -= int(abs(birdie.speed_x))                                                          #
                hole = Hole(hole.x,hole.y,hole.length,hole.height,holePos)                                  # 
        birdie.x = 871                                                                                      # keep bird to the right of barrier
        
    return birdie,background_x,background_x2,grasses,waters,sands,hole,direction                            # return edited objects

####################################
#   Main Variables                 #
####################################
# make all in game loops bools     #
inGame = True
move = False
playingGame = True
restart = True
inHole = False
introScreen = True
jammin = True
beatles = True
####################################
#   Main                           #
####################################

pygame.mixer.Channel(2).play(pygame.mixer.Sound('audio\\ilty.wav'),-1) # start beatles song paused
pygame.mixer.Channel(2).set_volume(0.2)                         # at 20% volume
pygame.mixer.Channel(2).pause()                                 #
pygame.mixer.Channel(1).play(pygame.mixer.Sound('audio\\Jammin.wav'),-1)# start bob marley
pygame.mixer.Channel(1).set_volume(0.12)                        # 12% volume
pygame.mixer.Channel(1).pause()                                 # paused


while inGame:
#-----Play intro music -------#
    if beatles:                                                      # if beatles is true
        pygame.mixer.Channel(2).unpause()                            # unpause beatles channel
        pygame.mixer.Channel(1).pause()                              # pause bob marley
        beatles = False                                              # beatles become false

#-----Show intro Screen ------#
    while introScreen:                                               # intro loop
        intro_screen()                                               # blit intro screen
        for event in pygame.event.get():                             # events
            if event.type == pygame.QUIT:                            # if quit pressed, make all loops false
                introScreen,ruleScreen,playingGame,outroScreen,inPlay = False,False,False,False,False
                
            if event.type == pygame.MOUSEBUTTONDOWN:                 # if button clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()             # and on play button
                if (410 < mouse_x < 610) and (20 < mouse_y < 95):    # if on rule buttom
                    introScreen = False                              # exit intro, enter rules
                    ruleScreen = True
                    
                elif (380 < mouse_x < 650) and (535 < mouse_y < 675):# if  on play button
                    introScreen,ruleScreen = False,False             # exit intro and rule screen, go straight to level loop
                    levelScreen = True

#-----Show rule Screen ------#
    while ruleScreen:                                               # rule screen loop
        rule_screen()                                               # blit rule screen
        for event in pygame.event.get():                            # events
            if event.type == pygame.QUIT:                           # if quit pressed, make all loops false
                introScreen,ruleScreen,playingGame,outroScreen,inPlay = False,False,False,False,False
            if event.type == pygame.MOUSEBUTTONDOWN:                # if button clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()            # and on back button
                if (0 < mouse_x < 120) and (20 < mouse_y < 125):    # make all things false except intro
                    restart,playingGame,introScreen,levelScreen,pause,endLevel,ruleScreen = False,False,True,False,False,False,False
                    beatles = True

#-----Show level Screen -----#
    while levelScreen:                                              # level screen loop
        level_screen()                                              # blit level screen
        for event in pygame.event.get():                            # events
            if event.type == pygame.QUIT:                           # if quit pressed, make all loops false
                introScreen,ruleScreen,playingGame,outroScreen,inPlay = False,False,False,False,False
            if event.type == pygame.MOUSEBUTTONDOWN:                # if button clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()            # and on play button
                for i in range(5):                                  # five loop
                    if ((35 + 200*i) < mouse_x < (205 + 200*i)) and (210 < mouse_y < 365):  # if clicked on level icon
                        levelScreen = False                         # exit level screen
                        restart = True                              # configure level
                        level = i                                   # make level that  icon
                        jammin = True

                for i in range(4):                                  # four loop
                    if ((125+200*i) < mouse_x < (225 + 200*i)) and (385 < mouse_y < 540):   # if clicked on second row icons
                        levelScreen = False                         # exit level screen
                        restart = True                              # configure level
                        level = i + 5                               # make level that  icon
                        jammin = True

                if (0 < mouse_x < 120) and (20 < mouse_y < 125):    # if back button exit everything, entre intro
                    restart,playingGame,introScreen,levelScreen,pause,endLevel = False,False,True,False,False,False
                    beatles = True

                if levelData.count("Gold") >= 9:                    # if 9 gold medals
                    if (415 < mouse_x < 610) and (560 < mouse_y < 735): # and icon is clicked
                        levelScreen = False                         # exit level screen
                        restart = True                              # configure level
                        level = 9                                   # make level 10
                        
#-----Play in game music -----#
    if jammin:                                                      # if jammin true
        pygame.mixer.Channel(1).unpause()                           # unpause bob marley
        pygame.mixer.Channel(2).pause()                             # pause beatles
        jammin = False                                              # jammin becomes false

#-----initiate level -----#
    if restart == True:                                             # if level restarting
        count = 0                                                   # count always begins at 0
        background_x = 0                                            # background 1 starts by filling the screen
        background_y = 0                                            # at 0,0
        background_x2 = 1019                                        # background 2 starts to the right of screen very slightly overlapping for no untouched place             
        background_y2 = 0                                           # at 1019,0
        direction = 'right'                                         # beginning direction of bird is right
        fellInWater = False                                         # bird does not begin by falling in water
        splash = 0                                                  # splash begins at 0
        delay = 4                                                   # delay begins at 2

#-----Load level imgs/play specific level song ----#
        if 0 <= level <= 8:                                         # draw sunny imgs for first 9 levels
            grass,dirt,sand,water,hole1,hole2,flag,background,waterWarning = load_game_imgs(sunnyImgs)

        elif level == 9:                                            # draw dark imgs for last level
            grass,dirt,sand,water,hole1,hole2,flag,background,waterWarning = load_game_imgs(darkImgs)
            pygame.mixer.Channel(2).pause()
            pygame.mixer.Channel(1).pause()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('mop.wav'),-1) # play rock music at level 40%

        if level == 8:                                              # if last original leve l
            delay = 0                                               # low delay

#-----loop and ingame bool-----#
        playingGame = True                                          # make game true
        move = False                                                # bird doesnt begin moving
        flapCount= 0                                                # flap count begins at 0
        explode = 0                                                 # explode begins at 0
        inHole = False                                              # inhole becomes fall
        pause = False                                               # pause is false
        
#-----Take objects from giant level list -----#
        if 0 <= level <= 9:                                         # if level is picked
            waters = levels[level][0][:]                            # make water list from levels
            grasses = levels[level][1][:]                           # make grass list from levels
            sands = levels[level][2][:]                             # make sand list from levels
            holeVar = levels[level][3][:]                           # make hole variables list from levels
            hole = holeVar[0]                                       # first item is hole object
            holePos = holeVar[1]                                    # second item is hole position
            birdie = Bird(grasses[4].x+80,grasses[4].y-27)          # create bird object
            
            gold = levels[level][4][0]                              # gold par
            silver = levels[level][4][1]                            # silver par
            bronze = levels[level][4][2]                            # brinze par
        else:                                                       # if ubntrue go back to level screen
            playingGame,pause,endLevel,introScreen,levelScreen = False,False,False,False,True

#-----in game loop -----#
    while playingGame:                                              # actual game loop
#-----check events and mouse clicks -----#
        for event in pygame.event.get():                            # events
            if event.type == pygame.MOUSEBUTTONDOWN:                # mouse clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()            #
                if (940 < mouse_x < 1000) and (10 < mouse_y < 70):  # if pause button clicked enter pause loop and break this one
                    playingGame,endLevel,introScreen,levelScreen,restart,pause = False,False,False,False,False,True
                    break
                
                flap.play()
                Vix = 0                                             # intital velocity begins at 0
                if move == False:                                   # if move is false
                    Vix = 2                                         # initial velocity is 2 m/s
                    
                mouse_x,mouse_y = pygame.mouse.get_pos()            #
                birdie.choose_direc(mouse_x,WIDTH,Vix)              # choose direction of bird 
                move = True                                         # make move true
                count = 0                                           # count starts at 0
                flapCount += 1                                      # add 1 to flapcount
                
#-----check birdie/object collisions -----#
        if hole.fallInHole(birdie) == False:                        # if bird hasnt fallen in hole
            count,grasses,hole = grassCollisions(count,grasses,hole)# check all collisions
            sands = sandCollisions(sands)                           #
            count,waters,delay,fellInWater = waterCollisions(count,waters,delay,fellInWater)
        else:                                                       # if it has
            inHole = True                                           # in hole is true
            explosionSound.play()

#-----Alter explode/splash and other bariables based on collisions -----#
        if inHole == True and explode < 60:                         # if explode is less than 60
            explode += 1                                            # add 1 to explode
            
        elif explode == 60:                                         # if it is 60
            endLevel = True                                         # enter end level loop
            playingGame = False                                     #
            
        if fellInWater == True:                                     # if bird has fallen in water
            splash += 1                                             # add 1 to splash
            
        if splash == 5:                                             # is bird has been in water for 5 cycles
            restart = True                                          # restart level
            water_screen()                                          # show water screen
            pygame.time.delay(1500)                                 # for 1.5 seconds
            playingGame,pause,endLevel,introScreen,levelScreen = False,False,False,False,False

#---- move background and objects with it-----#
        birdie,background_x,background_x2,grasses,waters,sands,hole,direction = move_backgroundx(birdie,background_x,background_x2,grasses,waters,sands,hole,direction)

#---- move bird-----#
        if move == True:                                            # if bird is moving
            count += 1                                              # add 1 to count
            if birdie.move_x == True:                               # if bird is moving x
                birdie.move_hor()                                   # move horizontally
                if birdie.rollCount >= 200:                         # if bird has been rolling for more than 200 cycles
                    move = False                                    # stop moving 
            
            if birdie.move_y == True:                               # if bird is moving y
                birdie.move_ver(count)                              # move vertically
        else:                                                       # if not moving
            birdie.speed_x = 0                                      # speed x should be 0
        if birdie.y > 675:
            move = False
            
#---- delay game and redraw screen -----#
        pygame.time.delay(delay)                                    # delay game by delay var
        drawScreen()                                                # redraw screen

#-----Show pause Screen -----#
    if pause:                                                       # if pause is true 
        pause_screen()                                              # draw pause screen
    while pause:
        for event in pygame.event.get():                            # events
            if event.type == pygame.QUIT:                           # if quit pressed, make all loops false
                introScreen,ruleScreen,playingGame,outroScreen,inPlay = False,False,False,False,False
                
            if event.type == pygame.MOUSEBUTTONDOWN:                # if button clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()            # and on play button
                if (120 < mouse_x < 240) and (150 < mouse_y < 270):  # if on levels
                    levelScreen,endLevel,introScreen,pause = True,False,False,False # exit intro, enter levels
                    beatles = True
                    
                elif (120 < mouse_x < 240) and (480 < mouse_y < 600):# or on home button
                    endLevel,introScreen,pause = False,True,False    # enter home
                    beatles = True
                    
                if (780 < mouse_x < 900) and (150 < mouse_y < 270):  # or on retry
                    restart,endLevel,introScreen,levelScreen,pause = True,False,False,False,False # restart level
                    
                elif (780 < mouse_x < 900) and (480 < mouse_y < 600):# or on play
                    restart,endLevel,introScreen,levelScreen,pause,playingGame = False,False,False,False,False,True # play game again

#-----Show endlevel Screen -----#
    if endLevel:                                                     # if endlevel is true
        levelData = end_level(levelData)                             # draw endlevel screen
    while endLevel:
        for event in pygame.event.get():                             # events
            if event.type == pygame.QUIT:                            # if quit pressed, make all loops false
                introScreen,ruleScreen,playingGame,outroScreen,inPlay = False,False,False,False,False
            if event.type == pygame.MOUSEBUTTONDOWN:                 # if button clicked
                mouse_x,mouse_y = pygame.mouse.get_pos()             # and on play button
                
                if event.type == pygame.MOUSEBUTTONDOWN:                 # if button clicked
                    mouse_x,mouse_y = pygame.mouse.get_pos()             # and on play button
                    if (120 < mouse_x < 240) and (150 < mouse_y < 270):  # if on levels
                        levelScreen,endLevel,introScreen,pause,restart = True,False,False,False,False # exit intro, enter levels
                        beatles = True
                        
                    elif (120 < mouse_x < 240) and (480 < mouse_y < 600):# and on home button
                        endLevel,introScreen,restart = False,True,False  # enter home
                        beatles = True
                        
                    if (780 < mouse_x < 900) and (150 < mouse_y < 270):  # or on retry
                        restart,endLevel,introScreen,levelScreen = True,False,False,False # restart level
                        
                    elif (780 < mouse_x < 900) and (480 < mouse_y < 600):# or on play
                        restart,endLevel,introScreen,levelScreen = True,False,False,False # play game again
                        
                        if level <8:                                     # if level less than 9
                            level += 1                                   # add1 to level
                        else:                                            # if not
                            levelScreen = True                           # go back to level screen
                            
        if level == 9 and restart == False:                              # when bonus level over
            pygame.mixer.Channel(0).stop()                               # stop master of puppets
            jammin = True                                                # play bpb marley
        

