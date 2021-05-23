from graphics import*
from random import*

#HitBox class
class _HitBox:
    """
        Creates the Hit-Box for 2 given coordinates pairs in oposite corners.
        \tParameters:\n
        \t\t1. x1: x-value for top left corner.
        \t\t2. y1: y-value for top left corner.
        \t\t3. x2: x-value for bottom right corner.
        \t\t4. y2: y-value for bottom right corner.
    """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.box = Rectangle(Point(x1, y1), Point(x2, y2))

        self.corner_coords = self.get_coords()
    
    def get_coords(self):
        """Returns the 4 coordinates of the Hit-Box (square)."""

        p1 = (self.box.getP1().getX(), self.box.getP1().getY()) # p1-------p2
        p2 = (self.box.getP2().getX(), self.box.getP1().getY()) # |         |
        p3 = (self.box.getP1().getX(), self.box.getP2().getY()) # |         |
        p4 = (self.box.getP2().getX(), self.box.getP2().getY()) # p3-------p4

        self.corner_coords = [p1, p2, p3, p4]

        return self.corner_coords

    def get_p(self, number): #Added last minute, verify
        """Missing documentation"""
        return self.corner_coords[number]

    def move_box(self, dx):
        """
        Moves box to the left by a given amount.\n
        Parameter:\n
        \t 1. dx: shifts box to the left by given amount.
        """
        self.box.move(-dx, 0)

        self.corner_coords = self.get_coords()
        self.side_coords = self.map_sides()


class Display:
    """
    Generates a user interface for frogger.
    \tParameters:\n
    \t\t1. width: width of the whole GUI. Only accepts ints.
    \t\t2. height: height of the whole GUI. Only accepts ints.
    \t\t3. window: window where game is being drawn. Only accepts GraphWin object.
    """
    def __init__(self, width, height, window):
        self.width = width
        self.height = height

        self.window = window

        self.starts = {}
        self.river = {}
        self.road_lines = {}

    def _generate_starts(self, start_amount):
        """
        Generates starts for each phase.
        \tParameter:\n
        \t\t1. start-amount: amount of breaks between each phase. Only accepts ints.
        
        """
        self.starts[0] = Rectangle(Point(0, 550), Point(self.width, self.height))
        self.starts[0].setFill('Green')
        self.starts[0].setOutline('Green')
        self.starts[0].draw(self.window)

        for i in range(1, start_amount):
            self.starts[i] = self.starts[i - 1].clone()
            
            self.starts[i].move(0, -250)
            
            self.starts[i].draw(self.window)

    def _generate_river(self, goal_amount):
        """
        Generates all river related items (water and bushes between goals).
        \tParameters:\n
        \t\t1. goal-amount: every even number is a bush and every uneven number a goal. Only accepts ints.
        """
        self.river[0] = Rectangle(Point(0, -25), Point(100, 75))
        self.river[0].setFill('Green')
        self.river[0].setOutline('Green')
        self.river[0].draw(self.window)

        for i in range(1, goal_amount):
            self.river[i] = self.river[i - 1].clone()
            self.river[i].move(100, 0)

            if not(i%2 == 0):
                self.river[i].setFill('Blue')
                self.river[i].setOutline('Blue')

            else:
                self.river[i].setFill('Green')
                self.river[i].setOutline('Green')

            self.river[i].draw(self.window)

        water_body = Rectangle(Point(0, 75), Point(self.width, self.height/2))
        water_body.setFill('Blue')
        water_body.setOutline('Blue')
        water_body.draw(self.window)
        print(water_body.config['fill'] == 'Blue')
        
        
    def _generate_lines(self):
        """Generates road division."""
        self.road_lines[0] = Rectangle(Point(0, 435), Point(50, 455))
        self.road_lines[0].setFill('Yellow')
        self.road_lines[0].draw(self.window)

        for j in range(1, 9):
            self.road_lines[j] = self.road_lines[j - 1].clone()
            self.road_lines[j].move(125, 0)
            self.road_lines[j].draw(self.window)

    def generate_field(self):
        """
        Generates all the user interface by calling the following:\n
        \t 1. generate-starts(2).
        \t 2. generate-river(11).
        \t 3. generate-lines().
        """
        self._generate_starts(2)
        self._generate_river(11)
        self._generate_lines()

class Frog:
    def __init__(self, window):
        self.window = window

        self.move_amount = 50

        self.positions = {
            'Up':r'All Frogs\North Frog.gif',
            'Down':r'All Frogs\South Frog.gif',
            'Left':r'All Frogs\West Frog.gif',
            'Right':r'All Frogs\East Frog.gif'
            }

        self.initial = Image(Point(450, 575), self.positions['Up'])
        self.initial.draw(self.window)

        self.hitbox = _HitBox(self.initial.getAnchor().getX() - self.initial.getWidth() / 2, self.initial.getAnchor().getY() - self.initial.getHeight() / 2,
                             self.initial.getAnchor().getX() + self.initial.getWidth() / 2, self.initial.getAnchor().getY() + self.initial.getHeight() / 2)

        self.current = Point(450, 575)

        self.x_dir = {
            'Right': self.move_amount,
            'Left': -self.move_amount,
            }
        self.y_dir = {
            'Up': -self.move_amount,
            'Down': self.move_amount
            }
    
    def movement(self):
        direction = self.window.checkKey()

        if direction in self.positions:
            self.current = self.initial.getAnchor()

            self.initial.undraw()

            if direction in self.x_dir:
                self.initial = Image(self.current, self.positions[direction])
                self.initial.draw(self.window)

                self.initial.move(self.x_dir[direction], 0)

            elif direction in self.y_dir:
                self.initial = Image(self.current, self.positions[direction])
                self.initial.draw(self.window)

                self.initial.move(0, self.y_dir[direction])

            self.hitbox.x1 = self.current.getX() - self.initial.getWidth() / 2
            self.hitbox.x2 = self.current.getX() + self.initial.getWidth() / 2
            self.hitbox.y1 = self.current.getY() - self.initial.getHeight() / 2
            self.hitbox.y2 = self.current.getY() + self.initial.getHeight() / 2
            update(10)

class Turtle:
    def __init__(self, window):
      self.window = window
      
      self.states = {
          'Upper': r'Turtles\FullTurtlesGif.gif',
          'Lower': r'Turtles\FullTurtlesR.gif'
          }

      self.lines = {}
      self.lines[0] = Image(Point(900, 120), self.states['Upper'])
      self.lines[0].draw(self.window)

      self.lines[1] = Image(Point(0, 280), self.states['Lower'])
      self.lines[1].draw(self.window)

      self.moves1 = 0
      self.moves2 = 0

    def turtle_movement(self):
        self.moves1 += 20
        self.moves2 += 10

        if self.moves1 == 960:
            self.lines[0].undraw()
            
            self.lines[0] = Image(Point(900, 120), self.states['Upper'])
            self.lines[0].draw(self.window)

            self.moves1 = 0

        if self.moves2 == 960:
            self.lines[1].undraw()
            
            self.lines[1] = Image(Point(0, 280), self.states['Lower'])
            self.lines[1].draw(self.window)

            self.moves2 = 0


        self.lines[0].move(-20,0)
        update(10)

        self.lines[1].move(10,0)
        update(10)
    
    def turtle_collision1(self, Frog):
        if (Frog.initial.getAnchor().getX() >= self.lines[0].getAnchor().getX() - self.lines[0].getWidth() / 2 and
            Frog.initial.getAnchor().getX() <= self.lines[0].getAnchor().getX() + self.lines[0].getWidth() / 2 and 
            Frog.initial.getAnchor().getY() >= self.lines[0].getAnchor().getY() - self.lines[0].getHeight() / 2 and
            Frog.initial.getAnchor().getY() <= self.lines[0].getAnchor().getY() + self.lines[0].getHeight() / 2):
            return True
        return False

        
class Car:
    def __init__(self, windows):
      self.windows = windows
      
      self.location = {
          'LeftOrange': r'Car\car_left.gif',
          'RightWhite': r'Car\whitecar_right.gif',
          'LeftBlue': r'Car\bluecar_left.gif',
          'RightRed': r'Car\redcar_right.gif',          
          }

      self.lane = {}
      self.lane[0] = Image(Point(900, 375), self.location['LeftOrange'])
      self.lane[0].draw(self.windows)

      self.lane[1] = Image(Point(0, 525), self.location['RightWhite'])
      self.lane[1].draw(self.windows)

      self.lane[2] = Image(Point(900, 475), self.location['LeftBlue'])
      self.lane[2].draw(self.windows)

      self.lane[3] = Image(Point(0, 425), self.location['RightRed'])
      self.lane[3].draw(self.windows)

      self.moves1 = 0
      self.moves2 = 0
      self.moves3 = 0
      self.moves4 = 0

    def car_movement(self):
        self.moves1 += 30
        self.moves2 += 20
        self.moves3 += 40
        self.moves4 += 30        

        if self.moves1 == 960:
            self.lane[0].undraw()
            
            self.lane[0] = Image(Point(900, 375), self.location['LeftOrange'])
            self.lane[0].draw(self.windows)

            self.moves1 = 0

        if self.moves2 == 960:
            self.lane[1].undraw()
            
            self.lane[1] = Image(Point(0, 525), self.location['RightWhite'])
            self.lane[1].draw(self.windows)

            self.moves2 = 0

        if self.moves3 == 960:
            self.lane[2].undraw()
            
            self.lane[2] = Image(Point(900, 475), self.location['LeftBlue'])
            self.lane[2].draw(self.windows)

            self.moves3 = 0

        if self.moves4 == 960:
            self.lane[3].undraw()
            
            self.lane[3] = Image(Point(0, 425), self.location['RightRed'])
            self.lane[3].draw(self.windows)

            self.moves4 = 0

        self.lane[0].move(-30,0)
        update(30)

        self.lane[1].move(20,0)
        update(30)

        self.lane[2].move(-40,0)
        update(30)

        self.lane[3].move(30,0)
        update(30)

class Logs:
    def __init__(self, window, log_image1, log_image2):

        self.window = window

        self.logs = {}

        self.logs[0] = Image(Point(0, 170), log_image1)

        self.logs[1] = Image(Point(900, 220), log_image2)

        self.logs[0].draw(self.window)

        self.log1damage = randint(0, 1)
        self.log2damage = randint(0, 1)

    def get_window(self):
        return self.window

    def get_logs(self):
        return self.logs

    def is_collision1(self, Frog):
        if (Frog.initial.getAnchor().getX() >= self.logs[0].getAnchor().getX() - self.logs[0].getWidth() / 2 and
            Frog.initial.getAnchor().getX() <= self.logs[0].getAnchor().getX() + self.logs[0].getWidth() / 2 and 
            Frog.initial.getAnchor().getY() >= self.logs[0].getAnchor().getY() - self.logs[0].getHeight() / 2 and
            Frog.initial.getAnchor().getY() <= self.logs[0].getAnchor().getY() + self.logs[0].getHeight() / 2):
            return True
        return False     

def main():
    win = GraphWin('Frogger', 900, 600, autoflush=False)
    win.setBackground('Black')
    print(win.getMouse().config)

    ui = Display(900, 600, win)
    ui.generate_field()

    temp = Frog(win)

    tp = Turtle(win)

    car = Car(win)

    logs = Logs(win, r'Car\car_left.gif', r'Car\car_left.gif')

    while True:
        logs.is_collision1(temp)
        if (tp.turtle_collision1(temp)):
            print("hit")
        temp.initial.getAnchor()
        temp.movement()
        tp.turtle_movement()
        car.car_movement()

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

#Might need to make a spawn class to control continuos movements

#Car class to inherit HitBox class (bool expression to determine if it'll kill or not)
    #4 types of cars
        #Could be implemented on a list

#Snake class to inherit HitBox class

#Turtle class to control their behavior (sink and float) inherits HitBox too

#Frog class

#Reward class

#Game class to run frogger
