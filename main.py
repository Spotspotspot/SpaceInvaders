# Simple demo of Object Oriented Programming
# added use of lists of objects

# Note - this is written for simplicity, not for the neatest, best or cleverest use of Python

# don't need to look at graphics.py now
from graphics import *

# draws a circle (don't need to understand this now)
def drawCircle(x, y, radius, colour):
    cir = Circle(Point(x, y), radius)   # create circle object
    cir.setOutline(colour)              # set its colour property to what we want
    cir.setWidth(4)                     # set its line width to what we want
    cir.draw(displayArea)               # tell it to draw itself on the graphical window object


# definition of Location "Class"
class Location:

    # these are "Properties"
    x = 10
    y = 10
    # no methods here

#definition of gameItem "Class"
class GameItem(Location): # inherits locations properties
    def draw(self):     # any child class (eg Alien below) should override this by having its own "draw()" method
        pass            # do nothing

    def erase(self):    # any child class (eg Alien below) should override this by having its own "erase()" method
        pass            # do nothing

    def move(self):     # any child class (eg Alien below) should override this by having its own  "move()" method
        pass            # do nothing


# definition of Alien "Class"
# Alien Class inherits all of the gameItem Classes properties and methods etc
# and overrides "draw()" "erase()" and "move()" methods
class Alien(GameItem):

    # these are "Properties"
    colour = "green"   # these are the default properties
    direction = 1       # 1 = right, -1 = left
    speed = 15

    # these are "Methods"
    def draw(self):
        drawCircle(self.x, self.y, 20, self.colour)

    def erase(self):    # same as draw(self): above except draws in black over the top of the last circle to erase it
        drawCircle(self.x, self.y, 20, "black")

    def move(self):
        if self.direction > 0:                  # if moving right
            if self.x + self.speed < 300:       # and moving right won't take us past the limit
                self.x = self.x + self.speed    # move further right
            else:                               # if at limit
                self.y = self.y + 40            # move down
                self.direction = -1             # and head in left direction

        if self.direction < 0:                  # if moving left
            if self.x - self.speed > 0:         # and moving left won't take us past the limit
                self.x = self.x - self.speed    # move further left
            else:                               # if at limit
                self.y = self.y + 40            # move down
                self.direction = 1              # and head in right direction

        if self.y > 300:                        # check if we have fallen off the bottom
           self.y = 10                          # restart at top (aliens don't really do this)

# end of Alien class definition

# definition of Player "Class"
# Player Class inherits all of the gameItem Classes properties and methods etc
# and overrides "draw()" "erase()" and "move()" methods
class Player(GameItem):

    x = 150
    y = 250

    # these are "Methods"
    def draw(self):
        drawCircle(self.x, self.y, 40, "pink")

    def erase(self):    # same as draw(self): above except draws in black over the top of the last circle to erase it
        drawCircle(self.x, self.y, 40, "black")

    def move(self):
        pass            # the player seems to have gone to sleep

# end of Player class definition



# Start of the Main program

displayArea = GraphWin('Object Invaders', 300, 300)     # create graphical window object

displayArea.setBackground("black")

# choose how many aliens you want
numberOfAliens = 10

items = []      # start with a blank list of game items
                # everthing added to this list must be derived from GameItem class,
                # so it can be more than just aliens


# make a player
myPlayer = Player()

items.append(myPlayer)  # add my player to the list of game items

# create some aliens.
for i in range(numberOfAliens):     # equivalent to "for (i=0; i<numberOfAliens; i++)"
    anotherAlien = Alien()          # make a new alien object
    anotherAlien.x = i * 20         # set its properties
    items.append(anotherAlien)      # add it to the list of game items
    # after this, the alien just created is not forgotten because it's referenced (referred to) in the list
    # however the line "anotherAlien = Alien()" is executed again, it makes "anotherAlien" refer to a new alien,
    # so it doesn't refer to the previous alien anymore

while (1):
    for stuff in items:        # draw ALL items (Note: you can use any name instead of 'stuff' if you want)
        stuff.draw()

    time.sleep(0.1)

    for stuff in items:        # erase ALL items
        stuff.erase()

    for stuff in items:        # move ALL items
        stuff.move()

    # and do it all again forever!


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
