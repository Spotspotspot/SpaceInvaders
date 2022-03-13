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


# definition of Alien "Class"
class Alien:

    # these are "Properties"
    colour = "green"   # these are the default properties
    x = 10
    y = 10
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


# Start of the Main program

displayArea = GraphWin('Object Invaders', 300, 300)     # create graphical window object

displayArea.setBackground("black")

# choose how many aliens you want
numberOfAliens = 10

# create some aliens.
aliens = []     # start with a blank list of aliens

for i in range(numberOfAliens):     # equivalent to "for (i=0; i<numberOfAliens; i++)"
    anotherAlien = Alien()          # make a new alien object
    anotherAlien.x = i * 20         # set its properties
    aliens.append(anotherAlien)     # add it to the list of aliens
    # after this, the alien just created is not forgotten because it's referenced (referred to) in the list
    # however the line "anotherAlien = Alien()" is executed again, it makes "anotherAlien" refer to a new alien,
    # so it doesn't refer to the previous alien anymore

while (1):
    for badGuys in aliens:        # draw ALL aliens (Note: you can use any name instead of 'badGuys' if you want)
        badGuys.draw()

    time.sleep(0.1)

    for badGuys in aliens:        # erase ALL aliens
        badGuys.erase()

    for badGuys in aliens:        # move ALL aliens
        badGuys.move()

    # and do it all again forever!


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
