# Functions/mouse.py # 
def mouse_to_cell(pos, cellsize):
    x, y = pos
    return y // cellsize, x // cellsize
