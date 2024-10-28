 # imports

import pygame
from queue import PriorityQueue
import pygame_gui

# display
WIDTH = 1200
WIN = pygame.display.set_mode((1920, 1080),)
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

# road weights
road_weights = {
    "road": 1.0,
    "highway": 0.5,
    "dirt": 2.0,
    "mountain": 3.0,
    "grass": 1.5,
    "gravel": 3.0}

# weather system
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
    'road': 4,
    'highway':2,
    'dirt' : 8,
    'mountain': 9,
    'gravel': 6
}
fog = {
    'road': 5,
    'highway': 3,
    'dirt' : 7,
    'mountain':10,
    'gravel': 6
}
snow = {
    'road': 6,
    'highway': 4,
    'dirt': 7,
    'mountain': 999999999999999999999999999999999999999999999999999999999,
    'gravel': 7
}

# traffic system

one_am_clear = {
    'road':0,
    'highway':0,
    'dirt':3,
    'mountain': 2,
    'gravel': 1
}

one_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':5,
    'mountain':2,
    'gravel':1
}

one_am_storm= {
    'road':15,
    'highway':10,
    'dirt':22,
    'mountain':35,
    'gravel':20
}

one_am_fog= {
    'road':25,
    'highway':20,
    'dirt':30,
    'mountain':35,
    'gravel':28
}

one_am_snow= {
    'road':20,
    'highway':20,
    'dirt':18,
    'mountain':25,
    'gravel':18
}

two_am_clear= {
    'road':0,
    'highway':0,
    'dirt':3,
    'mountain':2,
    'gravel':1
}

two_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':5,
    'mountain':2,
    'gravel':1
}

two_am_storm= {
    'road':15,
    'highway':10,
    'dirt':22,
    'mountain':35,
    'gravel':20
}

two_am_fog= {
    'road':25,
    'highway':20,
    'dirt':30,
    'mountain':35,
    'gravel':28
}

two_am_snow= {
    'road':20,
    'highway':20,
    'dirt':18,
    'mountain':25,
    'gravel':18
}

three_am_clear= {
    'road':0,
    'highway':0,
    'dirt':3,
    'mountain':2,
    'gravel':1
}

three_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':5,
    'mountain':2,
    'gravel':1
}

three_am_storm= {
    'road':15,
    'highway':10,
    'dirt':22,
    'mountain':35,
    'gravel':20
}

three_am_fog= {
    'road':25,
    'highway':20,
    'dirt':30,
    'mountain':35,
    'gravel':28
}

three_am_snow= {
    'road':20,
    'highway':20,
    'dirt':18,
    'mountain':25,
    'gravel':18
}

four_am_clear= {
    'road':0,
    'highway':0,
    'dirt':3,
    'mountain':2,
    'gravel':1
}

four_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':5,
    'mountain':2,
    'gravel':1
}

four_am_storm= {
    'road':15,
    'highway':10,
    'dirt':22,
    'mountain':35,
    'gravel':20
}

four_am_fog= {
    'road':25,
    'highway':20,
    'dirt':30,
    'mountain':35,
    'gravel':28
}

four_am_snow= {
    'road':20,
    'highway':20,
    'dirt':18,
    'mountain':25,
    'gravel':18
}

five_am_clear= {
    'road':2,
    'highway':1,
    'dirt':3,
    'mountain':2,
    'gravel':2
}

five_am_drizzle= {
    'road':2,
    'highway':1,
    'dirt':4,
    'mountain':2,
    'gravel':3
}

five_am_storm= {
    'road':20,
    'highway':15,
    'dirt':28,
    'mountain':40,
    'gravel':22
}

five_am_fog= {
    'road':35,
    'highway':27,
    'dirt':40,
    'mountain':45,
    'gravel':38
}

five_am_snow= {
    'road':40,
    'highway':33,
    'dirt':45,
    'mountain':55,
    'gravel':43
}

six_am_clear= {
    'road':2,
    'highway':1,
    'dirt':3,
    'mountain':2,
    'gravel':2
}

six_am_drizzle= {
    'road':2,
    'highway':1,
    'dirt':4,
    'mountain':2,
    'gravel':3
}

six_am_storm= {
    'road':20,
    'highway':15,
    'dirt':28,
    'mountain':40,
    'gravel':22
}

six_am_fog= {
    'road':35,
    'highway':27,
    'dirt':40,
    'mountain':0,
    'gravel':0
}

six_am_snow= {
    'road':40,
    'highway':33,
    'dirt':45,
    'mountain':55,
    'gravel':43
}

seven_am_clear= {
    'road':10,
    'highway':6,
    'dirt':15,
    'mountain':18,
    'gravel':12
}

seven_am_drizzle= {
    'road':10,
    'highway':6,
    'dirt':20,
    'mountain':18,
    'gravel':12
}

seven_am_storm= {
    'road':30,
    'highway':25,
    'dirt':40,
    'mountain':50,
    'gravel':33
}

seven_am_fog= {
    'road':45,
    'highway':40,
    'dirt':60,
    'mountain':80,
    'gravel':52
}

seven_am_snow= {
    'road':50,
    'highway':40,
    'dirt':57,
    'mountain':70,
    'gravel':53
}

eight_am_clear= {
    'road':10,
    'highway':6,
    'dirt':15,
    'mountain':18,
    'gravel':12
}

eight_am_drizzle= {
    'road':10,
    'highway':6,
    'dirt':20,
    'mountain':19,
    'gravel':12
}

eight_am_storm= {
    'road':30,
    'highway':25,
    'dirt':40,
    'mountain':5,
    'gravel':33
}

eight_am_fog= {
    'road':45,
    'highway':40,
    'dirt':60,
    'mountain':80,
    'gravel':52
}

eight_am_snow= {
    'road':50,
    'highway':40,
    'dirt':57,
    'mountain':70,
    'gravel':53
}

nine_am_clear= {
    'road':60,
    'highway':45,
    'dirt':75,
    'mountain':90,
    'gravel':65
}

nine_am_drizzle= {
    'road':60,
    'highway':45,
    'dirt':80,
    'mountain':90,
    'gravel':67
}

nine_am_storm= {
    'road':85,
    'highway':80,
    'dirt':90,
    'mountain':99,
    'gravel':87
}

nine_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0
}

nine_am_snow= {
    'road':80
    'highway':75
    'dirt':85,
    'mountain':99,
    'gravel':82
}

ten_am_clear= {
    'road':60,
    'highway':45,
    'dirt':75,
    'mountain':90,
    'gravel':65
}

ten_am_drizzle= {
    'road':60
    'highway':45,
    'dirt':80,
    'mountain':90,
    'gravel':67
}

ten_am_storm= {
    'road':85,
    'highway':80,
    'dirt':90,
    'mountain':99,
    'gravel':87
}

ten_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

ten_am_snow= {
    'road':80,
    'highway':75,
    'dirt':85,
    'mountain':99,
    'gravel':82,
}

eleven_am_clear= {
    'road':50,
    'highway':45,
    'dirt':60,
    'mountain':80,
    'gravel':53
}

eleven_am_drizzle= {
    'road':50,
    'highway':45,
    'dirt':60,
    'mountain':80,
    'gravel':55
}

eleven_am_storm= {
    'road':75,
    'highway':70
    'dirt':85,
    'mountain':95,
    'gravel':78
}

eleven_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eleven_am_snow= {
    'road':70,
    'highway':65,
    'dirt':80,
    'mountain':95,
    'gravel':73,
}

twelve_am_clear= {
    'road':50,
    'highway':45,
    'dirt':60,
    'mountain':80,
    'gravel':54,
}

twelve_am_drizzle= {
    'road':50,
    'highway':45,
    'dirt':60,
    'mountain':80,
    'gravel':56,
}

twelve_am_storm= {
    'road':75,
    'highway':70,
    'dirt':85,
    'mountain':95,
    'gravel':78,
}

twelve_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twelve_am_snow= {
    'road':70,
    'highway':65,
    'dirt':80,
    'mountain':95,
    'gravel':73,
}

thirteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

thirteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

thirteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

thirteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

thirteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fourteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fourteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fourteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fourteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fourteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fifteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fifteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fifteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fifteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

fifteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

sixteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

seventeen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

seventeen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

seventeen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

seventeen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

seventeen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eighteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eighteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eighteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eighteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

eighteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

nineteen_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

nineteen_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

nineteen_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

nineteen_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

nineteen_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_one_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_one_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_one_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_one_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_one_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_two_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_two_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_two_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_two_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_two_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_three_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_three_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_three_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_three_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_three_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_four_am_clear= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_four_am_drizzle= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_four_am_storm= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_four_am_fog= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

twenty_four_am_snow= {
    'road':0,
    'highway':0,
    'dirt':0,
    'mountain':0,
    'gravel':0,
}

# random variable defo
weather_index = 0
current_weather = clear
time_dict = twelve_am_clear
road_type = 'road'
index = ['start', 'road', 'highway', 'dirt road', 'mountain pass', 'gravel road', 'end']


# time stuff
time = 0
time_input = input("Enter the time as digits of the hours")

# clear weather
if current_weather == 'clear':
    if time_input == '00' or '12am':
        time_dict = twelve_am_clear
    elif time_input == '01' or '1am':
        time_dict = one_am_clear
    elif time_input == '02' or '2am':
        time_dict = two_am_clear
    elif time_input == '03' or '3am':
        time_dict = three_am_clear
    elif time_input == '04' or '4am':
        time_dict = four_am_clear
    elif time_input == '05' or '5am':
        time_dict = five_am_clear
    elif time_input == '06' or '6am':
        time_dict = six_am_clear
    elif time_input == '07' or '7am':
        time_dict = seven_am_clear
    elif time_input == '08' or '8am':
        time_dict = eight_am_clear
    elif time_input == '09' or '9am':
        time_dict = nine_am_clear
    elif time_input == '10' or '10am':
        time_dict = ten_am_clear
    elif time_input == '11' or '11am':
        time_dict = eleven_am_clear
    elif time_input == '12' or '12am':
        time_input = twelve_am_clear
    elif time_input == '13' or '13am':
        time_input = thirteen_am_clear
    elif time_input == '14' or '14am':
        time_input = fourteen_am_clear
    elif time_input == '15' or '15am':
        time_input = fifteen_am_clear
    elif time_input == '16' or '16am':
        time_input = sixteen_am_clear
    elif time_input == '17' or '17am':
        time_input = seventeen_am_clear
    elif time_input == '18' or '18am':
        time_input = eighteen_am_clear
    elif time_input == '19' or '19am':
        time_input = nineteen_am_clear
    elif time_input == '20' or '20am':
        time_input = twenty_am_clear
    elif time_input == '21' or '21am':
        time_input = twenty_one_am_clear
    elif time_input == '22' or '22am':
        time_input = twenty_two_am_clear
    elif time_input == '23' or '23am':
        time_input = twenty_three_am_clear
    elif time_input == '24' or '24am':
        time_input = twenty_four_am_clear

# drizzle weather
if current_weather == 'drizzle':
    if time_input == '00' or '12am':
        time_dict = twelve_am_drizzle
    elif time_input == '01' or '1am':
        time_dict = one_am_drizzle
    elif time_input == '02' or '2am':
        time_dict = two_am_drizzle
    elif time_input == '03' or '3am':
        time_dict = three_am_drizzle
    elif time_input == '04' or '4am':
        time_dict = four_am_drizzle
    elif time_input == '05' or '5am':
        time_dict = five_am_drizzle
    elif time_input == '06' or '6am':
        time_dict = six_am_drizzle
    elif time_input == '07' or '7am':
        time_dict = seven_am_drizzle
    elif time_input == '08' or '8am':
        time_dict = eight_am_drizzle
    elif time_input == '09' or '9am':
        time_dict = nine_am_drizzle
    elif time_input == '10' or '10am':
        time_dict = ten_am_drizzle
    elif time_input == '11' or '11am':
        time_dict = eleven_am_drizzle
    elif time_input == '12' or '12am':
        time_input = twelve_am_drizzle
    elif time_input == '13' or '13am':
        time_input = thirteen_am_drizzle
    elif time_input == '14' or '14am':
        time_input = fourteen_am_drizzle
    elif time_input == '15' or '15am':
        time_input = fifteen_am_drizzle
    elif time_input == '16' or '16am':
        time_input = sixteen_am_drizzle
    elif time_input == '17' or '17am':
        time_input = seventeen_am_drizzle
    elif time_input == '18' or '18am':
        time_input = eighteen_am_drizzle
    elif time_input == '19' or '19am':
        time_input = nineteen_am_drizzle
    elif time_input == '20' or '20am':
        time_input = twenty_am_drizzle
    elif time_input == '21' or '21am':
        time_input = twenty_one_am_drizzle
    elif time_input == '22' or '22am':
        time_input = twenty_two_am_drizzle
    elif time_input == '23' or '23am':
        time_input = twenty_three_am_drizzle
    elif time_input == '24' or '24am':
        time_input = twenty_four_am_drizzle

# storm weather
if current_weather == 'storm':
    if time_input == '00' or '12am':
        time_dict = twelve_am_storm
    elif time_input == '01' or '1am':
        time_dict = one_am_storm
    elif time_input == '02' or '2am':
        time_dict = two_am_storm
    elif time_input == '03' or '3am':
        time_dict = three_am_storm
    elif time_input == '04' or '4am':
        time_dict = four_am_storm
    elif time_input == '05' or '5am':
        time_dict = five_am_storm
    elif time_input == '06' or '6am':
        time_dict = six_am_storm
    elif time_input == '07' or '7am':
        time_dict = seven_am_storm
    elif time_input == '08' or '8am':
        time_dict = eight_am_storm
    elif time_input == '09' or '9am':
        time_dict = nine_am_storm
    elif time_input == '10' or '10am':
        time_dict = ten_am_storm
    elif time_input == '11' or '11am':
        time_dict = eleven_am_storm
    elif time_input == '12' or '12am':
        time_input = twelve_am_storm
    elif time_input == '13' or '13am':
        time_input = thirteen_am_storm
    elif time_input == '14' or '14am':
        time_input = fourteen_am_storm
    elif time_input == '15' or '15am':
        time_input = fifteen_am_storm
    elif time_input == '16' or '16am':
        time_input = sixteen_am_storm
    elif time_input == '17' or '17am':
        time_input = seventeen_am_storm
    elif time_input == '18' or '18am':
        time_input = eighteen_am_storm
    elif time_input == '19' or '19am':
        time_input = nineteen_am_storm
    elif time_input == '20' or '20am':
        time_input = twenty_am_storm
    elif time_input == '21' or '21am':
        time_input = twenty_one_am_storm
    elif time_input == '22' or '22am':
        time_input = twenty_two_am_storm
    elif time_input == '23' or '23am':
        time_input = twenty_three_am_storm
    elif time_input == '24' or '24am':
        time_input = twenty_four_am_storm

# fog weather
if current_weather == 'fog':
    if time_input == '00' or '12am':
        time_dict = twelve_am_fog
    elif time_input == '01' or '1am':
        time_dict = one_am_fog
    elif time_input == '02' or '2am':
        time_dict = two_am_fog
    elif time_input == '03' or '3am':
        time_dict = three_am_fog
    elif time_input == '04' or '4am':
        time_dict = four_am_fog
    elif time_input == '05' or '5am':
        time_dict = five_am_fog
    elif time_input == '06' or '6am':
        time_dict = six_am_fog
    elif time_input == '07' or '7am':
        time_dict = seven_am_fog
    elif time_input == '08' or '8am':
        time_dict = eight_am_fog
    elif time_input == '09' or '9am':
        time_dict = nine_am_fog
    elif time_input == '10' or '10am':
        time_dict = ten_am_fog
    elif time_input == '11' or '11am':
        time_dict = eleven_am_fog
    elif time_input == '12' or '12am':
        time_input = twelve_am_fog
    elif time_input == '13' or '13am':
        time_input = thirteen_am_fog
    elif time_input == '14' or '14am':
        time_input = fourteen_am_fog
    elif time_input == '15' or '15am':
        time_input = fifteen_am_fog
    elif time_input == '16' or '16am':
        time_input = sixteen_am_fog
    elif time_input == '17' or '17am':
        time_input = seventeen_am_fog
    elif time_input == '18' or '18am':
        time_input = eighteen_am_fog
    elif time_input == '19' or '19am':
        time_input = nineteen_am_fog
    elif time_input == '20' or '20am':
        time_input = twenty_am_fog
    elif time_input == '21' or '21am':
        time_input = twenty_one_am_fog
    elif time_input == '22' or '22am':
        time_input = twenty_two_am_fog
    elif time_input == '23' or '23am':
        time_input = twenty_three_am_fog
    elif time_input == '24' or '24am':
        time_input = twenty_four_am_fog

# snow weather
if current_weather == 'snow':
    if time_input == '00' or '12am':
        time_dict = twelve_am_snow
    elif time_input == '01' or '1am':
        time_dict = one_am_snow
    elif time_input == '02' or '2am':
        time_dict = two_am_snow
    elif time_input == '03' or '3am':
        time_dict = three_am_snow
    elif time_input == '04' or '4am':
        time_dict = four_am_snow
    elif time_input == '05' or '5am':
        time_dict = five_am_snow
    elif time_input == '06' or '6am':
        time_dict = six_am_snow
    elif time_input == '07' or '7am':
        time_dict = seven_am_snow
    elif time_input == '08' or '8am':
        time_dict = eight_am_snow
    elif time_input == '09' or '9am':
        time_dict = nine_am_snow
    elif time_input == '10' or '10am':
        time_dict = ten_am_snow
    elif time_input == '11' or '11am':
        time_dict = eleven_am_snow
    elif time_input == '12' or '12am':
        time_input = twelve_am_snow
    elif time_input == '13' or '13am':
        time_input = thirteen_am_snow
    elif time_input == '14' or '14am':
        time_input = fourteen_am_snow
    elif time_input == '15' or '15am':
        time_input = fifteen_am_snow
    elif time_input == '16' or '16am':
        time_input = sixteen_am_snow
    elif time_input == '17' or '17am':
        time_input = seventeen_am_snow
    elif time_input == '18' or '18am':
        time_input = eighteen_am_snow
    elif time_input == '19' or '19am':
        time_input = nineteen_am_snow
    elif time_input == '20' or '20am':
        time_input = twenty_am_snow
    elif time_input == '21' or '21am':
        time_input = twenty_one_am_snow
    elif time_input == '22' or '22am':
        time_input = twenty_two_am_snow
    elif time_input == '23' or '23am':
        time_input = twenty_three_am_snow
    elif time_input == '24' or '24am':
        time_input = twenty_four_am_snow

# drop down menu
manager = pygame_gui.UIManager((200,200))
dropdown_menu = pygame.gui.element.UIDropDownMenu(
    options_list = index,
    starting_option = 'Road Type',
    reletive_rect = pygame.rect((350, 275), (200, 30)),
    manager = manager
)



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
    return distance * road_weights[road_type] * current_weather[road_type] * time_dict[road_type]

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
                    algo(lambda: draw(win, grid, ROWS, width), grid, start, end, current_weather = clear)

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

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == dropdown_menu:
                    print("Selected option:", event.text)

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
            time_penalty = time_dict.get(neighbour.road_type, 1)
            temp_g_score = g_score[current] + road_weight + weather_penalty + time_penalty
            print(time_dict)
        

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
