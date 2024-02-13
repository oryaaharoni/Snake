import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# game window
window = tkinter.Tk()
window.title("snake")
# we dont want that the user expend the size of the window hieght-false, width- false
window.resizable(False, False)

# canvas to draw
# canvas- master prop is window, backgroundColor is black, height and width , borderwidth and highlightthickness remove the white border
canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

# center the window on our computer screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# format string+objects
window.geometry(f"{window_width}x{window_width}+{window_x}+{window_y}")

# initial game 
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE) #single tile for the snake's head
food = Tile(10 * TILE_SIZE, 10 * TILE_SIZE)

# velocity- the change of the snake every time- event
velocityX = 0
velocityY = 0

def change_direction(e):   #e= event
    # print(e)      
    # print(e.keysym) #wich key i pressed
    global velocityX, velocityY

    if (e.keysym=="Up"):
        velocityX = 0
        velocityY = -1
    elif (e.keysym=="Down"):
        velocityX = 0
        velocityY = 1
    elif (e.keysym=="Left"):
        velocityX = -1
        velocityY = 0
    elif (e.keysym=="Right"):
        velocityX = 1
        velocityY = 0


def move():
    global snake

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


def draw():
    global snake
    move()

    canvas.delete("all")  #clear the other frame
    # draw snake
    # fill- the color on the snake, and the other is the position top, botton, left , right
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "lime green" )
    
    # draw the food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE , fill = 'red')



    window.after(100, draw)  #after 100 millseconds i will call draw() again

draw()

# key listener- every time the key click the func is called
window.bind("<KeyRelease>", change_direction)
window.mainloop()