import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS


# game window
window = tkinter.Tk()
window.title("snake")
# we dont want that the user expend the size of the window
# hieght-false, width- false
window.resizable(False, False)

# canvas to draw
canvas = tkinter.Canvas()


window.mainloop()