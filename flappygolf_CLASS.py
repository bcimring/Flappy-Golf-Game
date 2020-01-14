################################
# Name: Barry Cimring
# Date: 19/11/2019
# File Name: flappygolf_CLASS.py
################################
import pygame
pygame.init()
import math
WIDTH = 1020
LENGTH = 750
screen = pygame.display.set_mode((WIDTH,LENGTH))

# images for bird sprite
birdsRight = [pygame.image.load('bird-01.png'),pygame.image.load('bird-02.png'),pygame.image.load('bird-03.png'),pygame.image.load('bird-04.png')]
birdsLeft = [pygame.image.load('bird-01.png'),pygame.image.load('bird-02.png'),pygame.image.load('bird-03.png'),pygame.image.load('bird-04.png')]


birdLength = 40 # length and width of bird image
birdHeight = 27 #
for i in range(len(birdsRight)):                                                    # for loop for loading images
    birdsRight[i] = birdsRight[i].convert_alpha()                                   # 
    birdsRight[i] = pygame.transform.scale(birdsRight[i],(birdLength,birdHeight))   # transform, convert alpha
    birdsLeft[i] = birdsLeft[i].convert_alpha()                                     #
    birdsLeft[i] = pygame.transform.scale(birdsLeft[i],(birdLength,birdHeight))     # transform, rotate convert alpha
    birdsLeft[i] = pygame.transform.flip(birdsLeft[i],True,False)                   #
    
def blit_alpha(target, source, location, opacity):                                  # function for blitting translucent images
        x = location[0]                                                             # x value
        y = location[1]                                                             # y value
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()  # make temporary surface for image
        temp.blit(target, (-x, -y))                                                 # inverse of x,y
        temp.blit(source, (0, 0))                                                   # source at 0,0
        temp.set_alpha(opacity)                                                     # set alpha translucency
        target.blit(temp, location)                                                 # blit on real surface
    
class Bird(object):                                                         # creat bird object
    def __init__(self,x,y,skin = 0):                                        # init at x,y value
        self.x = x                                                          # x variable
        self.y = y                                                          # y variable
        self.skin = skin                                                    # skin, speedx,y rollcount, bouncecount, rolling, initial pic
        self.speed_x = 2                                                    #
        self.speed_y = -4                                                   #
        self.acceleration_y = 0.008                                         #
        self.move_y = True                                                  #
        self.move_x = True                                                  #
        self.rollCount = 0                                                  #
        self.bounceCount = 0                                                #
        self.rolling = False                                                #
        self.picNum = 1                                                     #

    def __str__(self):                                                      # string method
        return str(self.speed_x)+"m/s at ("+str(self.x)+","+str(self.y)+")" # print speed and x,y
        
    def draw(self,screen,direction,count):                                  # drawing methof
        if count < 8:                                                       # if less than 8 count
            self.picNum = 1                                                 # picnum is 1
        if 8 <= count < 16:                                                 # if greater than 8
            self.picNum = 2                                                 # pic is 2
        if 16 <= count < 24:                                                # if greater than 16
            self.picNum = 3                                                 # picnum is 3
        else:                                                               # or picnum is 0
            self.picNum = 0
            
        if direction == 'left':                                             # if left facing
            screen.blit(birdsLeft[self.picNum],(self.x,self.y))             # choose from left lift
        else:                                                               # if right choose from right list
            screen.blit(birdsRight[self.picNum],(self.x,self.y))            # 

    def move_hor(self):                                      # moving horizontally function
        if self.rolling == False:                            # if not rolling
            self.x += self.speed_x                           # add speed to x 
        if self.rolling == True:                             # if rolling
            if self.rollCount < 200:                         #
                self.speed_x *= (149/150)**self.rollCount    # frictional exponential expression
                self.x += self.speed_x                       # add to speedx
                self.rollCount += 1                          # add to rollcount
        self.x = int(self.x)                                 # make an integer

    def choose_direc(self,mouse_x,WIDTH,Vix = 0):   # function choosing direction of speed
        if mouse_x < WIDTH//2:                      # if mouse clicked left side of screen
            self.speed_x -= 1.2                     # make speed more negative
            if Vix != 0:                            # if initial speed is not 0
                self.speed_x = Vix*-1               # multiply speed by -1
        
        if mouse_x > WIDTH//2:                      # if on right side
            self.speed_x += 1.2                     # make speed more positive
            if Vix != 0:                            # if initial soeed is not 0
                self.speed_x = Vix                  # speed is inital
        self.acceleration_y = 0.01                  # acceleration set
        self.bounceCount = 0                        # bouncecount becomes 0
        self.speed_y = -6                           # speed y is upward s
        self.y -= 10                                # bird is moved 10 up
        self.rollCount = 0                          # rolling false, move is true
        self.rolling = False                        #
        self.move_y = True                          #
        self.move_x = True                          #
        
    def move_ver(self,count):                       # funciton to move bird vertically
        self.speed_y += self.acceleration_y*count   # add accelertation times count to spee d
        self.y += int(self.speed_y)                 # add to y, follow trajectory
    
    def bounce_back(self):                          # function for bouncing
        self.speed_x *= -0.65                       # reverse direction, account for energy loss
        
def distance(x2,x1,y2,y1):                          # find distance between two object  s
    return ((x1-x2)**2+(y1-y2)**2)**0.5             # pythagorean theorum

class Obstacle(object):                             # obstacle class
    def __init__(self,startx,starty,length,height): # take top left coord, and length/width
        self.x = startx                             # x,y,length,height,horizontal pieces,vertical pieces, and filler attricbutes
        self.y = starty                             #
        self.length = length                        #
        self.height = height                        #
        
        self.pieces_horx = []                       #
        self.pieces_hory = []                       #
        self.filler = []                            #
        for i in range(length):                     # for loop for horiozontal pieces
            for j in range(2):                      #
                self.pieces_horx.append(startx+i*25)# add top and bottom sides of rectangle to list
        for i in range(length):                     # 
            self.pieces_hory.append(starty)         #
            self.pieces_hory.append(starty+height*25)
            
        self.pieces_verx = []                       #
        self.pieces_very = []                       #
        for i in range(height):                     # for loop for vertical pieces
            for j in range(2):                      # 
                self.pieces_very.append(starty+i*25)# add left and right sides of rectangle to list
        for i in range(height):                     #
            self.pieces_verx.append(startx)         #
            self.pieces_verx.append(startx+(length-1)*25)

        for i in range(length-2):                   # for loop for fill
            for j in range(height - 1):             # add all coordinates between sides to list
                self.filler.append([startx+25+i*25,starty+25+j*25])


    def __str__(self):                              # print method returning top irght coord and length and height of obstacles
        return "Block at ("+str(self.x)+","+str(self.y)+") of length "+str(self.length)+" and height "+str(self.height)

    def CollidesSideBottom(self,other):                                                             # function for colliding with bottom and side of block
        if (other.x <= self.x) and (other.y > self.y) and (other.y < (self.pieces_hory[-1])):       # if to the left of block
            for i in range(0,len(self.pieces_verx),2):                                              # check distance of bird to vertical pieces
                if distance(self.pieces_verx[i],other.x,self.pieces_very[i],other.y) < birdLength:  # if less than bird
                    other.bounce_back()                                                             # bounce bird
                    other.x =self.pieces_verx[i]-birdLength                                         # push to the left
        
        if (other.x >= (self.x)) and (other.y > self.y):                                            # if to the right of block
            for i in range(1,len(self.pieces_verx),2):                                              # check distance to right of block
                if distance(other.x,self.pieces_verx[i],other.y,self.pieces_very[i]) <= 25:         # check distance to vertical pieces
                    other.bounce_back()                                                             # bounce back
                    other.x = self.pieces_verx[i]+25                                                # push to the right
                    if other.x <= 149:                                                              # if rolling
                        other.x = 150                                                               # make it not roll
                        
        if other.y > self.y:                                                                        # if below roof
            for i in range(1,len(self.pieces_horx),2):                                              # check horizontal pieces
                if distance(self.pieces_horx[i],other.x,self.pieces_hory[i],other.y) < 25:          # distance between them
                    other.speed_y *= -0.65                                                          # bounce down
                    other.y +=5                                                                     # push down

    def CollidesTop(self,other,count):                                                              # function for top collision
        if other.y <= self.y:                                                                       # if above block
            for i in range(0,len(self.pieces_horx),2):                                              # check vertical distance
                if distance(self.pieces_horx[i],other.x,self.pieces_hory[i],other.y) < birdHeight:  # if less than bird height
                    if other.bounceCount < 1:                                                       # if bounce less than twice
                        other.bounceCount += 1                                                      # add 1
                        other.speed_y = -5*(1/2)**other.bounceCount                                 # multiply speed by exponential
                        other.y = self.y-birdHeight                                                 # push up
                        count = 0                                                                   # count restarts
                        other.move_y = True                                                         # move y is true
                            
                    else:                                                                           # if bounce more than twice
                        other.move_y = False                                                        # dont move y
                        other.rolling = True                                                        # bird is rolling
                        other.y = self.y-birdHeight                                                 # keep atop the block
                        
        if other.rolling:                                                                           # if rolling
            if ((other.x < self.pieces_horx[0]) and (distance(self.pieces_horx[0],other.x,self.pieces_hory[0],other.y) > 40)):  # if rolls of left corner
                other.move_y = True                                                                 # move y
                other.rolling = False                                                               # stop rolling
                other.x -= 5                                                                        # shift left
                other.speed_x = -1*abs(other.speed_x*0.8)                                           # speed x decreases
                other.speed_y = 0.4                                                                 # speed y is slightly down
            elif ((other.x > self.pieces_horx[-2]) and distance(self.pieces_horx[-2],other.x,self.pieces_hory[-2],other.y) > 30):# if rolls of right corner
                other.move_y = True                                                                 # move y
                other.rolling = False                                                               # stop rolling
                other.x += 5                                                                        # shift left
                other.speed_x = abs(other.speed_x*0.8)                                              # speed x decreases
                other.speed_y = 0.4                                                                 # speed y is slightly down
            
        other.move_x = True                                                                         # always move x
        return count                                                                                # return altered count
        
class Grass(Obstacle):                                                      # class grass
    def draw(self,screen,dirt,grass):                                       # function for drawing grass
        for i in range(len(self.pieces_verx)):                              # draw side as dirt
            screen.blit(dirt,(self.pieces_verx[i],self.pieces_very[i]))     #
        for i in range(0,len(self.pieces_horx),2):                          # draw top as grass
            screen.blit(grass,(self.pieces_horx[i],self.pieces_hory[i]))    # 
        for i in range(1,len(self.pieces_horx),2):                          # draw bottom as dirt
            screen.blit(dirt,(self.pieces_horx[i],self.pieces_hory[i]))     #
        for i in range(len(self.filler)):                                   # fill with dirt
            screen.blit(dirt,(self.filler[i][0],self.filler[i][1]))         #

class Sand(Obstacle):                                                       # sand class
    def draw(self,screen,sand,dirt):                                        # draw sand
        for i in range(len(self.pieces_verx)):                              # draw top half of sand as sand
            if self.pieces_very[i] <= (self.y + self.y + self.height*25)/2: #
                screen.blit(sand,(self.pieces_verx[i],self.pieces_very[i])) #
            else:                                                           # draw bottom as dirt
                screen.blit(dirt,(self.pieces_verx[i],self.pieces_very[i])) #
        for i in range(0,len(self.pieces_horx),2):                          # draw top as sand
            screen.blit(sand,(self.pieces_horx[i],self.pieces_hory[i]))     #
        for i in range(1,len(self.pieces_horx),2):                          # draw bottom as dirt
            screen.blit(dirt,(self.pieces_horx[i],self.pieces_hory[i]))     #
        for i in range(len(self.filler)):                                   # draw top half of fill as sand
            if self.filler[i][1] <= (self.y + self.y+self.height*25)/2:     #
                screen.blit(sand,(self.filler[i][0],self.filler[i][1]))     #
            else:                                                           #
                screen.blit(dirt,(self.filler[i][0],self.filler[i][1]))     # draw bottom as dirt
                
    def CollidesTop(self,other):                                            # function for sand top collision   s
        if other.y <= self.y:                                               # if bird above sand
            for i in range(0,len(self.pieces_horx),2):                      # check distance between top
                if distance(other.x,self.pieces_horx[i],other.y,self.pieces_hory[i]) <= birdHeight:
                    other.y = self.y-birdHeight                             # sit bird on top
                    other.move_x = False                                    # make it not move
                    other.move_y = False                                    #
                    other.speed_x = 0                                       #
                    break                                                   # exit loop

class Water(Obstacle):                                                                      # water class
    def draw(self,screen,water,dirt,level):                                                 # drawing water function
        if level != 9:                                                                      # if not bonus level
            for i in range(len(self.pieces_verx)):                                          #
                if self.pieces_very[i] <= (self.y + self.y + self.height*25)/2:             # draw top as transparent water
                    blit_alpha(screen,water,(self.pieces_verx[i],self.pieces_very[i]),128)  #
                else:                                                                       #
                    screen.blit(dirt,(self.pieces_verx[i],self.pieces_very[i]))             # draw bottom as dirt
            for i in range(0,len(self.pieces_horx),2):                                      # draw top as transparent water
                blit_alpha(screen,water,(self.pieces_horx[i],self.pieces_hory[i]),128)      #
            for i in range(1,len(self.pieces_horx),2):                                      #
                screen.blit(dirt,(self.pieces_horx[i],self.pieces_hory[i]))                 # draw bottom as dirt
            for i in range(len(self.filler)):                                               #
                if self.filler[i][1] <= (self.y + self.y+self.height*25)/2:                 #
                    blit_alpha(screen,water,(self.filler[i][0],self.filler[i][1]),128)      #
                else:                                                                       #
                    screen.blit(dirt,(self.filler[i][0],self.filler[i][1]))                 #
        else:
            for i in range(len(self.pieces_verx)):                                          # if bonus leve l
                if self.pieces_very[i] <= (self.y + self.y + self.height*25)/2:             # do everything the same
                    screen.blit(water,(self.pieces_verx[i],self.pieces_very[i]))            # except
                else:                                                                       # dont draw water as translucent
                    screen.blit(dirt,(self.pieces_verx[i],self.pieces_very[i]))             #
            for i in range(0,len(self.pieces_horx),2):                                      #
                screen.blit(water,(self.pieces_horx[i],self.pieces_hory[i]))                #
            for i in range(1,len(self.pieces_horx),2):                                      #
                screen.blit(dirt,(self.pieces_horx[i],self.pieces_hory[i]))                 #
            for i in range(len(self.filler)):                                               #
                if self.filler[i][1] <= (self.y + self.y+self.height*25)/2:                 #
                    screen.blit(water,(self.filler[i][0],self.filler[i][1]))                #
                else:                                                                       #
                    screen.blit(dirt,(self.filler[i][0],self.filler[i][1]))                 #
    
    def Collides(self,other,count,delay,fellInWater):                                                               # water collision
        if (other.x <= self.x) and (other.y > (self.y + self.height*25/2)) and (other.y < (self.pieces_hory[-1])):
            for i in range(0,len(self.pieces_verx),2):                                                              # if to the left (^) and below water check distance to left side
                if distance(self.pieces_verx[i],other.x,self.pieces_very[i],other.y) < birdLength:                  # if less than bird length
                    other.bounce_back()                                                                             # bounce bird
                    other.x =self.pieces_verx[i]-birdLength                                                         # push left
                                    
        if (other.x >= self.x) and (other.y > (self.y + self.height*25/2)) and (other.y < (self.pieces_hory[-1] + self.y+25)):# if to the left and below water
            for i in range(len(self.pieces_verx)):                                                                  # check collision
                if distance(other.x,self.pieces_verx[i],other.y,self.pieces_very[i]) <= 25:                         #
                    other.bounce_back()                                                                             # bounce bird
                    other.x =self.pieces_verx[i]+birdLength                                                         # push left
                
        if other.y <= (self.y+self.height*25//2) and (self.x <= other.x <= (self.x + (self.length-1)*25)) and other.y > (self.y+self.height*25//2)-35:
            other.y = self.y+self.height*25//2-25                                                                   # if bird below water
            other.move_x = False                                                                                    # stop moving put count to 0
            other.move_y = False
            other.speed_x = 0

        if self.y <= other.y <= self.y+self.height*25//2 and self.x <= other.x <= self.x+self.length*25:            # if bird in water
            delay = 25                                                                                              # large delay
            fellInWater = True                                                                                      # true bool                                                                                    # false bool
        
        if other.y > self.y:                                                                                        # if bird below dirt
            for i in range(1,len(self.pieces_horx),2):                                                              # check collision with bottom
                if distance(self.pieces_horx[i],other.x,self.pieces_hory[i],other.y) < 25:                          # if lower han bird height
                    other.speed_y *= -0.65                                                                          # bounce down
                    other.y +=5                                                                                     # puch down
                    count = 1                                                                                       # add to speed
            
        return count,delay,fellInWater                                                                              # return altered count, delay and bool

class Hole(Obstacle):                                           # Hole class
    def __init__(self,startx,starty,length,height,holePos):     # init
        Obstacle.__init__(self,startx,starty,length,height)     # explicit evoking
        self.x = startx                                         # same variables, plus holex
        self.y = starty                                         #
        self.length = length                                    #
        self.height = height                                    #
        self.holex = holePos*25 + self.x                        #
        self.pieces_horx = []                                   #
        self.pieces_hory = []                                   #
        self.filler = []                                        #
        for i in range(length):                                 # same horizontal block list, excluding hole position
            if i != holePos and i != holePos+1:                 #
                for j in range(2):                              #
                    self.pieces_horx.append(startx+i*25)        #
            else:                                               #
                self.pieces_horx.append(startx+i*25)            #
        
        for i in range(length):                                 # same horizontal block list, excluding hole position 
            if i != holePos and i != holePos+1:                 #
                self.pieces_hory.append(starty)                 #
                self.pieces_hory.append(starty+height*25)       #
            else:                                               #
                self.pieces_hory.append(starty+height*25)       #
                
        self.pieces_verx = []                                   #
        self.pieces_very = []                                   #
        for i in range(height):                                 # same vertical block list, excluding hole posittion
            for j in range(2):                                  #
                self.pieces_very.append(starty+i*25)            #
        for i in range(height):                                 #
            self.pieces_verx.append(startx)                     #
            self.pieces_verx.append(startx+(length-1)*25)       #

        for i in range(length-2):                               # same vertical block list, excluding hole position
            for j in range(height - 1):                         #
                self.filler.append([startx+25+i*25,starty+25+j*25])

    def draw(self,screen,dirt,grass,hole1,hole2,flag):                      # function for drawing hole
        screen.blit(flag,(self.holex,self.y-60))                            # draw flag above hole
        for i in range(len(self.pieces_verx)):                              # draw dirt one sides
            screen.blit(dirt,(self.pieces_verx[i],self.pieces_very[i]))     #
        for i in range(len(self.pieces_horx)):                              # draw grass on top, dirt on bottom
            if self.y == self.pieces_hory[i]:                               #
                screen.blit(grass,(self.pieces_horx[i],self.pieces_hory[i]))#
            else:                                                           #
                screen.blit(dirt,(self.pieces_horx[i],self.pieces_hory[i])) #
                                            
        for i in range(len(self.filler)):                                   # draw dirt as a fill
            screen.blit(dirt,(self.filler[i][0],self.filler[i][1]))         #
        screen.blit(hole1,(self.holex,self.y))                              # draw left hole at hole 1
        screen.blit(hole2,(self.holex+25,self.y))                           # draw right hole at hole 2

    def fallInHole(self,other):                          # function for checking if bird has fallen in
        if other.rolling and self.y == other.y-40:       # if bird rolling
            if self.holex-10 < other.x < self.holex+15:  # if between hole
                other.rolling,other.move_x = False,False # stop rolling and moving the x
                other.move_y = True                      # drop in hole
                return True                              # funciton it true
                
        elif ((self.holex-10 < other.x < self.holex+30)) and (other.speed_y > 0) and (other.y >= self.y-birdHeight):
            other.rolling,other.move_x = False,False     # if bird is not rolling and falls in stop moving
            other.move_y = True                          # drop in hole
            return True                                  # funciton it true
        return False                                     # otherwise, return false

    
