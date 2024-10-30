# imports
import pygame
from queue import PriorityQueue
import ui
import threading

# display
WIDTH = 1200
WIN = pygame.display.set_mode((1550, 800))
pygame.init()
pygame.display.set_caption('Everyone if fuckin eppy')

# colours
RED = (255, 0, 0)  # closed paths
GREEN = (0, 255, 0)  # open paths
YELLOW = (255, 255, 0)  #
WHITE = (255, 255, 255)  # background
BLACK = (0, 0, 0)  # roads
PURPLE = (128, 0, 128)  # end
ORANGE = (255, 165, 0)  # start
GREY = (128, 128, 128)  # grid lines
TURQUOISE = (64, 224, 208)  # redraw
BLUE = (0, 0, 255)  # highway
NAVY_BLUE = (0, 0, 128)  # mountain pass
BROWN = (122, 75, 4)  # dirt road
OLIVE_GREEN = (18, 107, 15)  # grass road

# weight dictionaries
# road types
road_weights = {
    "road": 1.0,
    "highway": 0.5,
    "dirt": 2.0,
    "mountain": 3.0,
    "grass": 1.5,
    "gravel": 3.0}
# weather
clear = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 10,
    'gravel': 2
}
drizzle = {
    'road': 5,
    'highway': 0,
    'dirt': 10,
    'mountain': 15,
    'gravel': 10
}
storm = {
    'road': 50,
    'highway': 40,
    'dirt': 75,
    'mountain': 95,
    'gravel': 9999999999999999 # it was 74
}
fog = {
    'road': 60,
    'highway': 50,
    'dirt': 75,
    'mountain': 99,
    'gravel': 70
}
snow = {
    'road': 60,
    'highway': 40,
    'dirt': 75,
    'mountain': 99,
    'gravel': 85
}
# Time
# One Am
one_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
one_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
one_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
one_am_fog = {
    'road': 25,
    'highway': 20,
    'dirt': 30,
    'mountain': 35,
    'gravel': 28
}
one_am_snow = {
    'road': 20,
    'highway': 20,
    'dirt': 18,
    'mountain': 25,
    'gravel': 18
}
# Two Am
two_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
two_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
two_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
two_am_fog = {
    'road': 25,
    'highway': 20,
    'dirt': 30,
    'mountain': 35,
    'gravel': 28
}
two_am_snow = {
    'road': 20,
    'highway': 20,
    'dirt': 18,
    'mountain': 25,
    'gravel': 18
}
# Three Am
three_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
three_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
three_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
three_am_fog = {
    'road': 25,
    'highway': 20,
    'dirt': 30,
    'mountain': 35,
    'gravel': 28
}
three_am_snow = {
    'road': 20,
    'highway': 20,
    'dirt': 18,
    'mountain': 25,
    'gravel': 18
}
# Four Am
four_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
four_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
four_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
four_am_fog = {
    'road': 25,
    'highway': 20,
    'dirt': 30,
    'mountain': 35,
    'gravel': 28
}
four_am_snow = {
    'road': 20,
    'highway': 20,
    'dirt': 18,
    'mountain': 25,
    'gravel': 18
}
# Five Am
five_am_clear = {
    'road': 2,
    'highway': 1,
    'dirt': 3,
    'mountain': 2,
    'gravel': 2
}
five_am_drizzle = {
    'road': 2,
    'highway': 1,
    'dirt': 4,
    'mountain': 2,
    'gravel': 3
}
five_am_storm = {
    'road': 20,
    'highway': 15,
    'dirt': 28,
    'mountain': 40,
    'gravel': 22
}
five_am_fog = {
    'road': 35,
    'highway': 27,
    'dirt': 40,
    'mountain': 45,
    'gravel': 38
}
five_am_snow = {
    'road': 40,
    'highway': 33,
    'dirt': 45,
    'mountain': 55,
    'gravel': 43
}
# Six Am
six_am_clear = {
    'road': 2,
    'highway': 1,
    'dirt': 3,
    'mountain': 2,
    'gravel': 2
}
six_am_drizzle = {
    'road': 2,
    'highway': 1,
    'dirt': 4,
    'mountain': 2,
    'gravel': 3
}
six_am_storm = {
    'road': 20,
    'highway': 15,
    'dirt': 28,
    'mountain': 40,
    'gravel': 22
}
six_am_fog = {
    'road': 35,
    'highway': 27,
    'dirt': 40,
    'mountain': 0,
    'gravel': 0
}
six_am_snow = {
    'road': 40,
    'highway': 33,
    'dirt': 45,
    'mountain': 55,
    'gravel': 43
}
# Seven Am
seven_am_clear = {
    'road': 10,
    'highway': 6,
    'dirt': 15,
    'mountain': 18,
    'gravel': 12
}
seven_am_drizzle = {
    'road': 10,
    'highway': 6,
    'dirt': 20,
    'mountain': 18,
    'gravel': 12
}
seven_am_storm = {
    'road': 30,
    'highway': 25,
    'dirt': 40,
    'mountain': 50,
    'gravel': 33
}
seven_am_fog = {
    'road': 45,
    'highway': 40,
    'dirt': 60,
    'mountain': 80,
    'gravel': 52
}
seven_am_snow = {
    'road': 50,
    'highway': 40,
    'dirt': 57,
    'mountain': 70,
    'gravel': 53
}
# Eight Am
eight_am_clear = {
    'road': 10,
    'highway': 6,
    'dirt': 15,
    'mountain': 18,
    'gravel': 12
}
eight_am_drizzle = {
    'road': 10,
    'highway': 6,
    'dirt': 20,
    'mountain': 19,
    'gravel': 12
}
eight_am_storm = {
    'road': 30,
    'highway': 25,
    'dirt': 40,
    'mountain': 5,
    'gravel': 33
}
eight_am_fog = {
    'road': 45,
    'highway': 40,
    'dirt': 60,
    'mountain': 80,
    'gravel': 52
}
eight_am_snow = {
    'road': 50,
    'highway': 40,
    'dirt': 57,
    'mountain': 70,
    'gravel': 53
}
# Nine Am
nine_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
nine_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
nine_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
nine_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
nine_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82
}
# Ten Am
ten_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
ten_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
ten_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
ten_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
ten_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82,
}
# Eleven Am
eleven_am_clear = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 53
}
eleven_am_drizzle = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 55
}
eleven_am_storm = {
    'road': 75,
    'highway': 70,
    'dirt': 85,
    'mountain': 95,
    'gravel': 78
}
eleven_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
eleven_am_snow = {
    'road': 70,
    'highway': 65,
    'dirt': 80,
    'mountain': 95,
    'gravel': 73,
}
# Twelve Pm
twelve_pm_clear = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 999999999999999999999, # it was 54
}
twelve_pm_drizzle = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 56,
}
twelve_pm_storm = {
    'road': 75,
    'highway': 70,
    'dirt': 85,
    'mountain': 95,
    'gravel': 78,
}
twelve_pm_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
twelve_pm_snow = {
    'road': 70,
    'highway': 65,
    'dirt': 80,
    'mountain': 95,
    'gravel': 73,
}
# One Pm
thirteen_am_clear = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 54,
}
thirteen_am_drizzle = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 56,
}
thirteen_am_storm = {
    'road': 75,
    'highway': 70,
    'dirt': 85,
    'mountain': 95,
    'gravel': 78,
}
thirteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
thirteen_am_snow = {
    'road': 70,
    'highway': 65,
    'dirt': 80,
    'mountain': 95,
    'gravel': 73,
}
# Two Pm
fourteen_am_clear = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 54,
}
fourteen_am_drizzle = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 56,
}
fourteen_am_storm = {
    'road': 75,
    'highway': 70,
    'dirt': 85,
    'mountain': 95,
    'gravel': 78,
}
fourteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
fourteen_am_snow = {
    'road': 70,
    'highway': 65,
    'dirt': 80,
    'mountain': 95,
    'gravel': 73,
}
# Three Pm
fifteen_am_clear = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 54,
}
fifteen_am_drizzle = {
    'road': 50,
    'highway': 45,
    'dirt': 60,
    'mountain': 80,
    'gravel': 56,
}
fifteen_am_storm = {
    'road': 75,
    'highway': 70,
    'dirt': 85,
    'mountain': 95,
    'gravel': 78,
}
fifteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0,
}
fifteen_am_snow = {
    'road': 70,
    'highway': 65,
    'dirt': 80,
    'mountain': 95,
    'gravel': 73,
}
sixteen_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
# Four Pm
sixteen_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
sixteen_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
sixteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
sixteen_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82
}
# Five Pm
seventeen_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
seventeen_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
seventeen_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
seventeen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
seventeen_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82
}
# Six Pm
eighteen_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
eighteen_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
eighteen_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
eighteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
eighteen_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82
}
# Seven Pm
nineteen_am_clear = {
    'road': 60,
    'highway': 45,
    'dirt': 75,
    'mountain': 90,
    'gravel': 65
}
nineteen_am_drizzle = {
    'road': 60,
    'highway': 45,
    'dirt': 80,
    'mountain': 90,
    'gravel': 67
}
nineteen_am_storm = {
    'road': 85,
    'highway': 80,
    'dirt': 90,
    'mountain': 99,
    'gravel': 87
}
nineteen_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
nineteen_am_snow = {
    'road': 80,
    'highway': 75,
    'dirt': 85,
    'mountain': 99,
    'gravel': 82
}
# Eight Pm
twenty_am_clear = {
    'road': 10,
    'highway': 6,
    'dirt': 15,
    'mountain': 18,
    'gravel': 12
}
twenty_am_drizzle = {
    'road': 10,
    'highway': 6,
    'dirt': 20,
    'mountain': 19,
    'gravel': 12
}
twenty_am_storm = {
    'road': 30,
    'highway': 25,
    'dirt': 40,
    'mountain': 5,
    'gravel': 33
}
twenty_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
twenty_am_snow = {
    'road': 50,
    'highway': 40,
    'dirt': 57,
    'mountain': 70,
    'gravel': 53
}
# Nine Pm
twenty_one_am_clear = {
    'road': 10,
    'highway': 6,
    'dirt': 15,
    'mountain': 18,
    'gravel': 12
}
twenty_one_am_drizzle = {
    'road': 10,
    'highway': 6,
    'dirt': 20,
    'mountain': 19,
    'gravel': 12
}
twenty_one_am_storm = {
    'road': 30,
    'highway': 25,
    'dirt': 40,
    'mountain': 5,
    'gravel': 33
}
twenty_one_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
twenty_one_am_snow = {
    'road': 50,
    'highway': 40,
    'dirt': 57,
    'mountain': 70,
    'gravel': 53
}
# Ten Pm
twenty_two_am_clear = {
    'road': 2,
    'highway': 1,
    'dirt': 3,
    'mountain': 2,
    'gravel': 2
}
twenty_two_am_drizzle = {
    'road': 2,
    'highway': 1,
    'dirt': 4,
    'mountain': 2,
    'gravel': 3
}
twenty_two_am_storm = {
    'road': 20,
    'highway': 15,
    'dirt': 28,
    'mountain': 40,
    'gravel': 22
}
twenty_two_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
twenty_two_am_snow = {
    'road': 40,
    'highway': 33,
    'dirt': 45,
    'mountain': 55,
    'gravel': 43
}
# Eleven Pm
twenty_three_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
twenty_three_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
twenty_three_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
twenty_three_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
twenty_three_am_snow = {
    'road': 40,
    'highway': 33,
    'dirt': 45,
    'mountain': 55,
    'gravel': 43
}
# Twelve Pm
twenty_four_am_clear = {
    'road': 0,
    'highway': 0,
    'dirt': 3,
    'mountain': 2,
    'gravel': 1
}
twenty_four_am_drizzle = {
    'road': 0,
    'highway': 0,
    'dirt': 5,
    'mountain': 2,
    'gravel': 1
}
twenty_four_am_storm = {
    'road': 15,
    'highway': 10,
    'dirt': 22,
    'mountain': 35,
    'gravel': 20
}
twenty_four_am_fog = {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'gravel': 0
}
twenty_four_am_snow = {
    'road': 20,
    'highway': 20,
    'dirt': 18,
    'mountain': 25,
    'gravel': 18
}

# random variable def
weather_index = 0
current_weather = {}
time_weight = {}
road_type = 'road'
index = ['start', 'road', 'highway', 'dirt road', 'mountain pass', 'gravel road', 'end']
weather = ['clear', 'drizzle', 'storm', 'fog', 'snow']
clock = pygame.time.Clock()
# Spot class which handles the road types used and the position of said roads.
# It also notes the types of the road the neighbours are
class Spot:
    def __init__(self, row, col, width, total_rows, road_type):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows
        self.road_type = road_type

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.colour == RED

    def is_open(self):
        return self.colour == GREEN

    def is_barrier(self):
        return self.colour == WHITE

    def is_start(self):
        return self.colour == ORANGE

    def is_end(self):
        return self.colour == PURPLE

    def is_highway(self):
        return self.colour == BLACK

    def is_mountainpass(self):
        return self.colour == OLIVE_GREEN

    def gravel_road(self):
        return self.colour == GREY

    def dirt_road(self):
        return self.colour == BROWN

    def reset(self):
        self.colour = WHITE

    def make_closed(self):
        self.colour = RED

    def make_open(self):
        self.colour = GREEN

    def make_end(self):
        self.colour = PURPLE

    def make_start(self):
        self.colour = ORANGE

    def make_road(self):
        self.colour = BLACK
        self.road_type = 'road'

    def make_highway(self):
        self.colour = BLUE
        self.road_type = 'highway'

    def make_path_redraw(self):
        self.colour = TURQUOISE

    def make_mountainpass(self):
        self.colour = NAVY_BLUE
        self.road_type = 'mountain'

    def make_dirt_road(self):
        self.colour = BROWN
        self.road_type = 'dirt'

    def make_gravel_road(self):
        self.colour = GREY
        self.road_type = 'gravel'

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():  # DOWN
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # UP
            self.neighbours.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():  # RIGHT
            self.neighbours.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():  # LEFT
            self.neighbours.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# Calculates the distance or base cost of traveling down a path.
# This cost and is then added to others to get the final cost of traveling down the path
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance


# This one makes and stores the grid positions in such a way that you can actually use them
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for x in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(x, j, gap, rows, road_type='road')
            grid[x].append(spot)

    return grid


# This function does the drawing of the grids
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# this is the main draw function.. Here the draw_grid function is called and also fills in clicked spots
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


# This function gives you the position where you click the boxes
def get_clicked(pos, rows, width):
    gap = width // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def start_tkinter():
    ui.open_ui()

tk_thread = threading.Thread(target=start_tkinter)
tk_thread.start()

# This is the main function. Here all the other functions are called. It also has the game loop that deals in displaying
# button presses and so on.
def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    index_counter = 0

    while run:
        current_selections = ui.get_selections()
        road_selection = current_selections['road_type']
        weather_selection = current_selections['weather']
        time = current_selections['time']
        # global calls these variables so that they can be much more easily accessed
        global current_weather, time_weight, weather_index
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue

            # checks for mouse button presses
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, width)
                spot = grid[row][col]
                if road_selection == 'Start' and not start and spot != end:
                    start = spot
                    spot.make_start()
                elif road_selection == 'Road' and spot != start:
                    spot.make_road()
                elif road_selection == 'Highway':
                    spot.make_highway()
                elif road_selection == 'Dirt road':
                    spot.make_dirt_road()
                elif road_selection == 'Mountain pass':
                    spot.make_mountainpass()
                elif road_selection == 'Gravel road':
                    spot.make_gravel_road()
                elif road_selection == 'End' and not end and spot != start:
                    end = spot
                    spot.make_end()

            # this one resets the clicked tiles to barrier blocks that the algorithm cannot pass
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None


                # runs the algorithm(and also does the time)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                            # weather
                            if weather_selection == 'Clear':
                                current_weather = clear
                            elif weather_selection == 'Drizzle':
                                current_weather = drizzle
                            elif weather_selection == 'Storm':
                                current_weather = storm
                            elif weather_selection == 'Fog':
                                current_weather = fog
                            elif weather_selection == 'Snow':
                                current_weather = snow

                            # time
                            # Clear weather
                            if current_weather == clear:
                                if time == '01':
                                    time_weight = one_am_clear
                                elif time == '02':
                                    time_weight = two_am_clear
                                elif time == '03':
                                    time_weight = three_am_clear
                                elif time == '04':
                                    time_weight = four_am_clear
                                elif time == '05':
                                    time_weight = five_am_clear
                                elif time == '06':
                                    time_weight = six_am_clear
                                elif time == '07':
                                    time_weight = seven_am_clear
                                elif time == '08':
                                    time_weight = eight_am_clear
                                elif time == '09':
                                    time_weight = nine_am_clear
                                elif time == '10':
                                    time_weight = ten_am_clear
                                elif time == '11':
                                    time_weight = eleven_am_clear
                                elif time == '12':
                                    time = twelve_pm_clear
                                elif time == '13':
                                    time = thirteen_am_clear
                                elif time == '14':
                                    time = fourteen_am_clear
                                elif time == '15':
                                    time = fifteen_am_clear
                                elif time == '16':
                                    time = sixteen_am_clear
                                elif time == '17':
                                    time = seventeen_am_clear
                                elif time == '18':
                                    time = eighteen_am_clear
                                elif time == '19':
                                    time = nineteen_am_clear
                                elif time == '20':
                                    time = twenty_am_clear
                                elif time == '21':
                                    time = twenty_one_am_clear
                                elif time == '22':
                                    time = twenty_two_am_clear
                                elif time == '23':
                                    time = twenty_three_am_clear
                                elif time == '24':
                                    time = twenty_four_am_clear
                            # drizzle weather
                            # Drizzle weather
                            print(time)
                            if current_weather == drizzle:
                                if time == '00':
                                    time_weight = twelve_pm_drizzle
                                elif time == '01':
                                    time_weight = one_am_drizzle
                                elif time == '02':
                                    time_weight = two_am_drizzle
                                elif time == '03':
                                    time_weight = three_am_drizzle
                                elif time == '04':
                                    time_weight = four_am_drizzle
                                elif time == '05':
                                    time_weight = five_am_drizzle
                                elif time == '06':
                                    time_weight = six_am_drizzle
                                elif time == '07':
                                    time_weight = seven_am_drizzle
                                elif time == '08':
                                    time_weight = eight_am_drizzle
                                elif time == '09':
                                    time_weight = nine_am_drizzle
                                elif time == '10':
                                    time_weight = ten_am_drizzle
                                elif time == '11':
                                    time_weight = eleven_am_drizzle
                                elif time == '12':
                                    time = twelve_pm_drizzle
                                elif time == '13':
                                    time = thirteen_am_drizzle
                                elif time == '14':
                                    time = fourteen_am_drizzle
                                elif time == '15':
                                    time = fifteen_am_drizzle
                                elif time == '16':
                                    time = sixteen_am_drizzle
                                elif time == '17':
                                    time = seventeen_am_drizzle
                                elif time == '18':
                                    time = eighteen_am_drizzle
                                elif time == '19':
                                    time = nineteen_am_drizzle
                                elif time == '20':
                                    time = twenty_am_drizzle
                                elif time == '21':
                                    time = twenty_one_am_drizzle
                                elif time == '22':
                                    time = twenty_two_am_drizzle
                                elif time == '23':
                                    time = twenty_three_am_drizzle
                                elif time == '24':
                                    time = twenty_four_am_drizzle
                            # storm weather
                            if current_weather == storm:
                                if time == '00':
                                    time_weight = twelve_pm_storm
                                elif time == '01':
                                    time_weight = one_am_storm
                                elif time == '02':
                                    time_weight = two_am_storm
                                elif time == '03':
                                    time_weight = three_am_storm
                                elif time == '04':
                                    time_weight = four_am_storm
                                elif time == '05':
                                    time_weight = five_am_storm
                                elif time == '06':
                                    time_weight = six_am_storm
                                elif time == '07':
                                    time_weight = seven_am_storm
                                elif time == '08':
                                    time_weight = eight_am_storm
                                elif time == '09':
                                    time_weight = nine_am_storm
                                elif time == '10':
                                    time_weight = ten_am_storm
                                elif time == '11':
                                    time_weight = eleven_am_storm
                                elif time == '12':
                                    time = twelve_pm_storm
                                elif time == '13':
                                    time = thirteen_am_storm
                                elif time == '14':
                                    time = fourteen_am_storm
                                elif time == '15':
                                    time = fifteen_am_storm
                                elif time == '16':
                                    time = sixteen_am_storm
                                elif time == '17':
                                    time = seventeen_am_storm
                                elif time == '18':
                                    time = eighteen_am_storm
                                elif time == '19':
                                    time = nineteen_am_storm
                                elif time == '20':
                                    time = twenty_am_storm
                                elif time == '21':
                                    time = twenty_one_am_storm
                                elif time == '22':
                                    time = twenty_two_am_storm
                                elif time == '23':
                                    time = twenty_three_am_storm
                                elif time == '24':
                                    time = twenty_four_am_storm
                            # Fog weather
                            if current_weather == fog:
                                if time == '00':
                                    time_weight = twelve_pm_fog
                                elif time == '01':
                                    time_weight = one_am_fog
                                elif time == '02':
                                    time_weight = two_am_fog
                                elif time == '03':
                                    time_weight = three_am_fog
                                elif time == '04':
                                    time_weight = four_am_fog
                                elif time == '05':
                                    time_weight = five_am_fog
                                elif time == '06':
                                    time_weight = six_am_fog
                                elif time == '07':
                                    time_weight = seven_am_fog
                                elif time == '08':
                                    time_weight = eight_am_fog
                                elif time == '09':
                                    time_weight = nine_am_fog
                                elif time == '10':
                                    time_weight = ten_am_fog
                                elif time == '11':
                                    time_weight = eleven_am_fog
                                elif time == '12':
                                    time_weight = twelve_pm_fog
                                elif time == '13':
                                    time_weight = thirteen_am_fog
                                elif time == '14':
                                    time_weight = fourteen_am_fog
                                elif time == '15':
                                    time_weight = fifteen_am_fog
                                elif time == '16':
                                    time_weight = sixteen_am_fog
                                elif time == '17':
                                    time_weight = seventeen_am_fog
                                elif time == '18':
                                    time_weight = eighteen_am_fog
                                elif time == '19':
                                    time_weight = nineteen_am_fog
                                elif time == '20':
                                    time_weight = twenty_am_fog
                                elif time == '21':
                                    time_weight = twenty_one_am_fog
                                elif time == '22':
                                    time_weight = twenty_two_am_fog
                                elif time == '23':
                                    time_weight = twenty_three_am_fog
                                elif time == '24':
                                    time_weight = twelve_pm_fog
                            # Snow weather
                            if current_weather == snow:
                                if time == '00':
                                    time_weight = twelve_pm_snow
                                elif time == '01':
                                    time_weight = one_am_snow
                                elif time == '02':
                                    time_weight = two_am_snow
                                elif time == '03':
                                    time_weight = three_am_snow
                                elif time == '04':
                                    time_weight = four_am_snow
                                elif time == '05':
                                    time_weight = five_am_snow
                                elif time == '06':
                                    time_weight = six_am_snow
                                elif time == '07':
                                    time_weight = seven_am_snow
                                elif time == '08':
                                    time_weight = eight_am_snow
                                elif time == '09':
                                    time_weight = nine_am_snow
                                elif time == '10':
                                    time_weight = ten_am_snow
                                elif time == '11':
                                    time_weight = eleven_am_snow
                                elif time == '12':
                                    time_weight = twelve_pm_snow
                                elif time == '13':
                                    time_weight = thirteen_am_snow
                                elif time == '14':
                                    time_weight = fourteen_am_snow
                                elif time == '15':
                                    time_weight = fifteen_am_snow
                                elif time == '16':
                                    time_weight = sixteen_am_snow
                                elif time == '17':
                                    time_weight = seventeen_am_snow
                                elif time == '18':
                                    time_weight = eighteen_am_snow
                                elif time == '19':
                                    time_weight = nineteen_am_snow
                                elif time == '20':
                                    time_weight = twenty_am_snow
                                elif time == '21':
                                    time_weight = twenty_one_am_snow
                                elif time == '22':
                                    time_weight = twenty_two_am_snow
                                elif time == '23':
                                    time_weight = twenty_three_am_snow
                                elif time == '24':
                                    time_weight = twelve_pm_snow
                    algo(lambda: draw(win, grid, ROWS, width), grid, start, end, time_weight, current_weather)


# redraws the best path in a cyan colour for easy viewing
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path_redraw()
        draw()


# the heart of the program. This is the A* algorithm function that does the computing
def algo(draw, grid, start, end, time_weight, current_weather):  # Added current_weather as a parameter
    count = 0
    open_set = PriorityQueue()  # makes an open set where the nearby nodes are added
    open_set.put((0, count, start))  # adds said nodes
    came_from = {}  # dictionary that stores the current nodes in the open set and what the node that they came form was
    g_score = {spot: float('inf') for row in grid for spot in row}
    g_score[start] = 0  # tells you the approx cost of traveling down the path. Path with the lowest value is chosen
    f_score = {spot: float('inf') for row in grid for spot in row}
    f_score[start] = h(start.get_pos(),
                       end.get_pos())  # total score of the g and h score (which approx distance form end)
    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbour in current.neighbours:
            road_weight = road_weights.get(neighbour.road_type, 1.0)
            weather_penalty = current_weather.get(neighbour.road_type, 1)
            time_penalty = time_weight.get(neighbour.road_type, 1)
            temp_g_score = g_score[current] + road_weight + weather_penalty + time_penalty
            print(time_penalty)

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


if __name__ == "__main__":
    main(WIN, WIDTH)
