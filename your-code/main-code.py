import random
import time

couch = {
    "name": "couch",
    "type": "furniture",
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
    "name": "outside"
}
# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_b, door_a, door_c],
    "bedroom 2": [dresser, double_bed, door_b],
    "living room": [door_c, dining_table, door_d],
    "outside": [door_d],
    "piano": [key_a],
    "queen bed": [key_b],
    "dresser": [key_d],
    "double bed": [key_c],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [outside]
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

start_time = time.time()
time_limit = start_time + 60*2


def end_time():
    while 1:
        restart = input("Do you want to restart the game? 'yes' or 'no': ")
        linebreak_small()
        if restart == 'yes':
            global start_time,time_limit
            start_time = time.time()
            time_limit = start_time + 60*2
            start_game()
            break
        elif restart == 'no':
            print('Goodbye!')
            exit()
            break
        else:
            print("I dint't understand.")

def math_question():
    while 1:
        num_1 = random.randint(1, 5)
        num_2 = random.randint(1, 5)
        dict = {"{num1} + {num2}? ".format(num1=num_1, num2=num_2): num_1 + num_2,
                "{num1} - {num2}?".format(num1=num_1, num2=num_2): num_1 - num_2,
                "{num1} * {num2}? ".format(num1=num_1, num2=num_2): num_1 * num_2}
        r = random.randrange(len(dict))
        pergunta = list(dict.keys())[r]
        x = input("How much is " + pergunta + " ")
        if int(x) == int(dict[pergunta]):
            print('You got the answer right.\n')
            break
        else:
            print('wrong, try again.')

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def linebreak_small():
    """
    Print a line break
    """
    print("")

def start_game():
    """
    Start the game
    """
    linebreak()
    print(
        "You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.\nYou don't remember why you are here and what had happened before.\n")
    print("You hear a strange voice in the back saying: 'Do you want to play a game, a game of your life. Starting now you have 2 minutes to leave the room.\nIf you can't finish this game, you won't be able to learn code for the rest of your life.'")
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        linebreak_small()
        print("You are now in " + room["name"] + '\n')
        intended_action = input("What would you like to do? Type 'explore' or 'examine'? ").strip()
        linebreak_small()
        if intended_action == "explore":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, you have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, you have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item(input("What would you like to examine?").strip())
            linebreak_small()
        elif intended_action == "examine piano":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("piano")
        elif intended_action == "examine queen bed":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("queen bed")
        elif intended_action == "examine dresser":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("dresser")
        elif intended_action == "examine double bed":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("double bed")
        elif intended_action == "examine door a":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("door a")
        elif intended_action == "examine door b":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("door b")
        elif intended_action == "examine door c":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)))
            examine_item("door c")
        elif intended_action == "examine door d":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("door d")
        elif intended_action == "examine couch":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("couch")
        elif intended_action == "examine dining table":
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, You have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            examine_item("dining table")
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.\n")
            current_time = time.time()
            if current_time > time_limit:
                print('Game over, you have no more time left.')
                linebreak_small()
                end_time()
            else:
                time_left = time_limit - current_time
                print('You still have ' + str(int(time_left)) + " seconds to leave this place. Hurry up!\n")
            play_room(room)
        linebreak()


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    linebreak_small()
    print("Now you must explore the room.\n\nYou are in the " + room["name"] + ". Your options are: " + ", ".join(items) + '\n')

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examined the " + item_name + " and "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key):
                    output += "you unlocked it with the key you have.\n"
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "it is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    print("In order to get this key you need to get it right.\n")
                    math_question()
                    game_state["keys_collected"].append(item_found)
                    output += "found a " + item_found["name"] + "."
                else:
                    output += "there isn't anything interesting about it.\n"
            print(output)
            break

    if (output is None):
        linebreak_small()
        print("The item you requested is not found in the current room.")

    if (next_room and input("Do you want to go to the next room? Enter 'yes' or 'no':").strip() == 'yes'):
        linebreak_small()
        play_room(next_room)
    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

start_game()