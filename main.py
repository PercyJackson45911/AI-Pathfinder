#imports
import pygame
from queue import PriorityQueue

#display
WIDTH = 1200
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('A* Route finding algorithm')


#colours
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY = (128,128,128)
TURQUOISE = (64,224, 208)

class Spot:  # the main class tht deals with drawing inside the window.
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = BLACK
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED
    def is_open(self):
        return self.colour == GREEN
    def is_barrier(self):
        return self.colour == BLACK
    def is_start(self):
        return self.colour == ORANGE
    def is_end(self):
        return self.colour == PURPLE

    def reset(self):
        self.colour = BLACK
    def make_closed(self):
        self.colour = RED
    def make_open(self):
        self.colour = GREEN
    def make_path(self):
        self.colour = WHITE
    def make_end(self):
        self.colour = PURPLE
    def make_start(self):
        self.colour = ORANGE
    def make_path_redraw(self):
        self.colour = TURQUOISE
    def draw(self, win):
        pygame.draw.rect(win, self.colour,(self.x, self.y, self.width,self.width))
    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col+1].is_barrier(): # RIGHT
            self.neighbours.append(grid[self.row][self.col+1])

        if self.col > 0 and not  grid[self.row][self.col - 1].is_barrier(): # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])
    def __lt__(self, other):
        return False

def h(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def make_grid(rows, width):
    grid = []
    gap = width//rows
    for x in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(x, j, gap, rows)
            grid[x].append(spot)

    return grid

def draw_grid(win, rows, width):
    gap = width //rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j*gap, 0), (j*gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win,grid,ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]: # left button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end: # drawing the start point
                    start = spot
                    start.make_start()


                elif not end and spot != start: # drawing the end point
                    end = spot
                    end.make_end()

                elif spot != start and spot != end: # drawing the barriers
                    spot.make_path()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)

                    algo(lambda: draw(win, grid, ROWS, width), grid, start, end)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path_redraw()
        draw()



def algo(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float('inf') for row in grid for spot in row}  # track of the shortest distance from start node to current node
    g_score[start] = 0
    f_score = {spot: float('inf') for row in grid for spot in row}  # track of a node to the end distance
    f_score[start] = h(start.get_pos(), end.get_pos())  # guess of distance from start to end node

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]  # learn heap sort algo
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbour in current.neighbours:  # Corrected spelling of neighbours
            temp_g_score = g_score[current] + 1  # Increment g_score for the neighbour

            if temp_g_score < g_score[neighbour]:  # If the new g_score is better, update
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())  # Add missing () to get_pos()
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))  # Add neighbour to the priority queue
                    open_set_hash.add(neighbour)
                    neighbour.make_open()  # Visual representation of open nodes

        draw()  # Call the draw function to update the window

        if current != start:
            current.make_closed()  # Visual representation of closed nodes

    return False  # No path found


main(WIN, WIDTH)
