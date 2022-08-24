
import sys
import random
import time


'''Connecting additional modules'''
try:
    import bext, colorama
except ImportError:
    print ('The bext and colorama modules are required to run the program.')
    sys.exit ()

class Drop:
    def __init__ (self):
        self.x = random.randint (0, width) # Horizontal start position
        self.y = -1 #initial vertical position - beyond the top of the screen
        '''Type: anti-drop or drop'''
        self.drop_type = random.randint (0, 1) 
        self.timeout = random.randint (0, 3) # Delay until next move
        self.wait_count = random.randint (0, 3) # Pause counter
    def renew (self):
        self.__init__ ()
    def move (self):
        if drop.wait_count < drop.timeout: #As long as you can't move
            drop.wait_count += 1 # Increasing the pause counter
            return False
        else: # Already moveable
            drop.wait_count = 0 # Reset pause counter
            drop.y += 1 # Move the drop or anti drop one step down
            return True
    def draw (self):
        if self.drop_type == 1:
            symbol = str (random.randint (1, 9))
            con_print (self.x, self.y, green, symbol)
            self.zero_draw () # Draw a bright zero
        else:
            con_print (self.x, self.y, green, ' ')
    def zero_draw (self):
        if (self.y < height):
            con_print (self.x, self.y+1, lgreen, '0')

def is_rb_corner (x, y):
    if x == width and y == height:
        return True
    else:
        return False
def con_print (x, y, color, symbol):
    if not is_rb_corner (x, y):
        bext.goto (x, y)
        sys.stdout.write (color)
        print (symbol, end='')

bext.title ('matrix') # Change the title of the console window
bext.clear () # Clearing the console window
bext.hide () # Hiding the cursor in the console window
width, height = bext.size () # Get the size of the console window
window_width = 100
window_height = 100
width -= 1
height -= 1

green = colorama.Fore.GREEN
lgreen = colorama.Fore.LIGHTGREEN_EX

'''Create an array of drops and antidrops'''
drops = []
for i in range (1, width*2//3):
    drop = Drop ()
    drops.append (drop)

while True:
    for drop in drops:
        if drop.move (): # Checking the movement of an element
            drop.draw () # Displaying an element
            if drop.y >= height: # Reached the bottom
                drop.renew () # Update an element
    key = bext.getKey (blocking = False) # Checking if a key is pressed
    if key == 'esc': # If ESC is pressed, then exit the program
        bext.clear ()
        sys.exit ()
    time.sleep (0.02) # Delay