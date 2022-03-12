from graphics import *

displayArea = GraphWin('Object Invaders', 300, 300)     # create graphical window object

def main():

    displayArea.setBackground("black")

    # make some aliens. Fred, tom and harry are "Objects"
    fred = Alien()          # make fred
    fred.x = 50             # change fred's properties

    tom = Alien()
    tom.x = 200
    tom.colour = "red"

    harry = Alien()
    harry.x = 100
    harry.colour = "blue"

    # do something with them
    while (1):
        tom.draw()
        fred.draw()
        harry.draw()

        time.sleep(0.05)

        tom.erase()
        fred.erase()
        harry.erase()

        tom.move()
        fred.move()
        harry.move()


class Alien: # this is a "Class" (obviously)

    # these are "Properties"
    colour = "green"   # these are all default settings
    x = 10
    y = 10
    direction = 1       # 1 = right, -1 = left
    speed = 15

    # these are "Methods"
    def draw(self):
        cir = Circle(Point(self.x, self.y), 20)     # create circle object
        cir.setOutline(self.colour)                 # set its colour property to what we want
        cir.setWidth(4)                             # set its line width to what we want
        cir.draw(displayArea)                       # tell it to draw itself on the display object

    def erase(self):
        cir = Circle(Point(self.x, self.y), 20)
        cir.setOutline("black")
        cir.setWidth(4)
        cir.draw(displayArea)

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
           self.y = 10                          # restart at top (they dont really do this)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
