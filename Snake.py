import os
import random

import readchar
#Constant
POS_X = 0
POS_Y = 1
MAP_WIDTH=20
MAP_HEIGHT=15

NUM_OF_MAP_OBJECTS=1

#Head of the snake
game_running=True


while game_running:

    my_position=[8,10]
    snake_body=[]

    map_objects=[]

#This generates random objects on the map REVIEW THIS TOMORROW
    while len(map_objects)<NUM_OF_MAP_OBJECTS:
        new_position= [random.randint(0, MAP_WIDTH - 1),random.randint(0,MAP_HEIGHT-1)]
        if new_position not in map_objects and new_position !=my_position:
            map_objects.append(new_position)



#Main loop
    while True:
        old_position = my_position.copy()
        #Draw Map
        print("+" + "-" * MAP_WIDTH *3 + "+")


        for coordinate_y in range(MAP_HEIGHT):
            print("|", end="")



            for coordinate_x in range(MAP_WIDTH):

                char_to_draw = " "

            #Snake's food
                for map_object in map_objects:
                    if map_object[POS_X]==coordinate_x and map_object[POS_Y]==coordinate_y:
                        char_to_draw="*"
            #Snake's body
                for segment in snake_body:
                    if segment[POS_X]==coordinate_x and segment[POS_Y]==coordinate_y:
                        char_to_draw="o"
            #Snake's Head
                if my_position[POS_X]==coordinate_x and my_position[POS_Y]==coordinate_y:
                    char_to_draw="O"

                print(" {} ".format(char_to_draw),end="")
            print("|")


        print("+"+"-"*MAP_WIDTH*3+"+")


        #Ask user where to move
        #Direction=input("Where would you like to move?[WASD]:".upper())

        direction= readchar.readchar().upper()

        if direction=="W":
            my_position[POS_Y]-=1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction=="A":
            my_position[POS_X]-=1
            my_position[POS_X] %= MAP_WIDTH
        elif direction=="S":
            my_position[POS_Y]+=1
            my_position[POS_Y] %= MAP_HEIGHT
        elif direction=="D":
            my_position[POS_X]+=1
            my_position[POS_X] %= MAP_WIDTH

        elif direction=="Q":
            game_running=False
            break
    #This adds the previous position to the beginning of the snake's body

        if my_position in snake_body:
            print("GAME OVER")
            input("press Enter to restart the game...")
            break

        snake_body.insert(0,old_position)


        if my_position in map_objects:
            #Snake eats
            map_objects.remove(my_position)

            # This is to create a new object in a random position
            new_position=[random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
            while new_position in map_objects or new_position in snake_body or new_position==my_position:
                new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

            map_objects.append(new_position)



        else:
            snake_body.pop()



        os.system("cls")