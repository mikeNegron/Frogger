from graphics import*

#HitBox class
class HitBox:
    """Creates a square Hit-Box for obstacles."""

    def __init__(self, x1, y1, x2, y2):
        """Creates the Hit-Box for 2 given coordinates pairs in oposite corners."""

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.box = Rectangle(Point(x1, y1), Point(x2, y2))

        self.corner_coords = self.get_coords()

        self.side_coords = self.map_sides() #Might not need this
    
    def get_coords(self):
        """Returns the 4 coordinates of the Hit-Box (square)."""

        p1 = (self.x1, self.y1) # p1-------p2
        p2 = (self.x2, self.y1) # |         |
        p3 = (self.x1, self.y2) # |         |
        p4 = (self.x2, self.y2) # p3-------p4

        self.corner_coords = [p1, p2, p3, p4]

        return self.corner_coords

    def map_sides(self):
        """Gets coordinates for all the sides of the box"""

        x_values = [range(self.x1, self.x2)] #One at y1 and one at y2
        y_values = [range(self.y1, self.y2)] #One at x1 and one at x2

        self.side_coords = [x_values, y_values]

        return self.side_coords

    def move_box(self, dx):
        """Moves box to the left by a given amount."""
        self.box.move(-dx, 0)

        self.corner_coords = self.get_coords()
        self.side_coords = self.map_sides()


        


#Car class to inherit HitBox class (bool expression to determine if it'll kill or not)
    #4 types of cars
        #Could be implemented on a list

#Snake class to inherit HitBox class

#Turtle class to control their behavior (sink and float) inherits HitBox too

#Frog class

#Reward class

#Game class to run frogger

def main():
    win = GraphWin('temp', 100, 100, autoflush=False)

    s = HitBox(60, 20, 80, 40)

    s.box.setOutline('Black')
    s.box.setWidth(4)
    s.box.draw(win)

    for i in range(60):
        s.move_box(1)

        update(15)

    win.getMouse()
    win.close()


    
if __name__ == '__main__':
    main()