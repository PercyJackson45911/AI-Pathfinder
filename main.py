# imports

import pygame
from queue import PriorityQueue

# display
WIDTH = 1200
WIN = pygame.display.set_mode((1920, 1080),)
pygame.display.set_caption('Advaith is eppy')

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

# road weights
road_weights = {
    "road": 1.0,
    "highway": 0.5,
    "dirt": 2.0,
    "mountain": 3.0,
    "grass": 1.5,
    "gravel": 3.0}

#weater system
weather = ['clear', 'drizzle', 'storm', 'fog', 'snow']
clear= {
    'road': 0,
    'highway': 0,
    'dirt': 0,
    'mountain': 0,
    'grass': 0,
    'gravel':0
}
drizzle = {
    'road':0,
    'highway':0,
    'dirt':1,
    'mountain':1,
    'gravel':1
}
storm = {
    'road': 2,
    'highway':1,
    'dirt' : 5,
    'mountain': 9,
    'gravel': 4
}
fog = {
    'road': 5,
    'highway': 7,
    'dirt' : 3,
    'mountain':10,
    'gravel': 3
}
snow = {
    'road': 3,
    'highway': 1,
    'dirt': 7,
    'mountain': 999999999999999999999999999999999999999999999999999999999,
    'gravel': 7
}
# index counters
weather_index = 0
current_weather = clear
road_type = 'road'

class Spot:  # the main class tht deals with drawing inside the window.
    def __init__(self, row, col, width, total_rows, road_type):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.colour = WHITE
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows
        self.road_type=road_type

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

    def is_grassyroad(self):
        return self.colour == OLIVE_GREEN

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

    def make_road(self):
        self.colour = BLACK
        self.road_type = 'road'

    def make_highway(self):
        self.colour = BLUE
        self.road_type = 'highway'

    def make_end(self):
        self.colour = PURPLE

    def make_start(self):
        self.colour = ORANGE

    def make_path_redraw(self):
        self.colour = TURQUOISE

    def make_grassroad(self):
        self.colour = OLIVE_GREEN
        self.road_type = 'grass'

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


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance * road_weights[road_type] * current_weather[road_type]

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for x in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(x, j, gap, rows, road_type='road')
            grid[x].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


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
    global weather_index
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    index = ['start', 'road', 'highway', 'dirt road', 'mountain pass', 'gravel road', 'grass road', 'end']
    index_counter = 0
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if index_counter >= len(index) - 1:
                        index_counter = 0
                    else:
                        index_counter = index_counter + 1

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked(pos, ROWS, width)
                spot = grid[row][col]
                if index[index_counter] == 'start' and not start and spot != end:
                    start = spot
                    spot.make_start()
                elif index[index_counter] == 'road' and spot != start:
                    spot.make_road()
                elif index[index_counter] == 'highway':
                    spot.make_highway()
                elif index[index_counter] == 'dirt road':
                    spot.make_dirt_road()
                elif index[index_counter] == 'mountain pass':
                    spot.make_mountainpass()
                elif index[index_counter] == 'gravel road':
                    spot.make_gravel_road()
                elif index[index_counter] == 'grass road':
                    spot.make_grassroad()
                elif index[index_counter] == 'end' and not end and spot != start:
                    end = spot
                    end.make_end()
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
                    algo(lambda: draw(win, grid, ROWS, width), grid, start, end, current_weather
                         )

                elif event.key == pygame.K_w:
                    if weather_index >= len(weather) -1:
                        weather_index = 0
                    else:
                        weather_index = weather_index + 1
                    if weather[weather_index] == 'clear':
                        current_weather = clear
                    elif weather[weather_index] == 'drizzle':
                        current_weather = drizzle
                    elif weather[weather_index] == 'storm':
                        current_weather = storm
                    elif weather[weather_index] == 'fog':
                        current_weather = fog
                    elif weather[weather_index] == 'snow':
                        current_weather = snow
                    print(current_weather)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path_redraw()
        draw()


def algo(draw, grid, start, end, current_weather):  # Added current_weather as a parameter
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float('inf') for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float('inf') for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
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
            weather_penalty = current_weather.get(neighbour.road_type, 1)  # Using current_weather here
            print(f"Weather: {weather_index}, Weather Penalty: {weather_penalty}")
            temp_g_score = g_score[current] + road_weight + weather_penalty
        

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



main(WIN, WIDTH)
