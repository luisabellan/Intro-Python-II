from Room import Room
from Player import Player
from Item import Item

# Declare all the rooms


outside =  Room("Outside Cave Entrance",
                 "North of you, the cave mount beckons")

foyer = Room(
"Foyer",
"Dim light filters in from the south. Dusty passages run north and east.")

overlook = Room(
"Grand Overlook",
"A steep cliff appears before you, falling the darkness. Ahead to the north, a light flickers in distance, but there is no way across the chasm.")

narrow =   Room(
"Narrow Passage",
"The narrow passage bends here from west north. The smell of gold permeates the air.")

treasure = Room(
"Treasure Chamber",
"You've found the long-lost treasure! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.")



# Link rooms together

outside.n_to = foyer
outside.s_to = None
outside.e_to = None
outside.w_to = None
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
foyer.w_to = None
overlook.s_to = foyer
overlook.n_to = None
overlook.e_to = None
overlook.w_to = None
narrow.w_to = foyer
narrow.n_to = treasure
narrow.s_to = None
narrow.e_to = None
treasure.s_to = narrow
treasure.n_to = None
treasure.e_to = None
treasure.w_to = None

# Rooms items


tomato = Item("tomato","A delicious red tomato")
glass_of_water = Item("glass_of_water","A refreshing glass of water")
knife = Item("knife","A sharp knife")
napkin = Item("napkin","Just a normal napkin")
muffin = Item("muffin","A chocolate muffin")
toothbrush = Item("toothbrush","A used toothbrush")
coins = Item("coins","A bunch of coins")
key = Item("key","A rusty key")

outside.items = []
foyer.items = [glass_of_water.name, knife.name, tomato.name]
overlook.items = [napkin.name, muffin.name]
narrow.items = [toothbrush.name]
treasure.items = [coins.name, key.name]


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("Luis", outside)
player.current_room.name = outside.name
player.current_room.description = outside.description


choice = -1
while choice != 0:


    # print(player)
    print(f"player current room name is {player.current_room.name}")
    print(f"player current room description is {player.current_room.description}")
    print(f" Items in this room: {player.current_room.items}")

    #print(f"the room north of this one is {player.current_room.n_to.name}")
    print("Instructions:\n")
    print("Press:\n - n for north\n - s for south\n - e for east\n - w for west\n - 0 to quit\n\n")
    print("Type:\n - take or get followed by the name of an item to pick up an item\n\n")

    # REPL

    # Read
    choice = input(
        "Where do you want to go?: ")

    no_room_msg = 'There is no room in that direction'

    choices = choice.split(' ')
    print(choices)
    print(len(choices))

    print(choice)
    if len(choices) == 1:

        # Evaluate
        if choice == 'n' and player.current_room.n_to != None:

                # this method isn't working player.set_current_room(player.current_room.n_to.name)
                # player.set_current_room(player.current_room.n_to.name)
                player = Player("Luis", player.current_room.n_to)
                #player.current_room = player.current_room.n_to
                continue
        elif choice == 'n' and player.current_room.n_to == None:
            print(no_room_msg)


        if choice == 's' and player.current_room.s_to != None:
                player = Player("Luis", player.current_room.s_to)
                #player.current_room = player.current_room.s_to
                continue
        elif choice == 's' and player.current_room.s_to == None:
            print(no_room_msg)


        if choice == 'e' and player.current_room.e_to != None:
                player = Player("Luis", player.current_room.e_to)
                #player.current_room = player.current_room.e_to
                continue
        elif choice == 'e'and player.current_room.e_to == None:
            print(no_room_msg)




        if choice == 'w' and player.current_room.w_to != None:
                player = Player("Luis", player.current_room.w_to)
                #player.current_room = player.current_room.w_to
                continue
        elif choice == 'w' and player.current_room.w_to == None:
            print(no_room_msg)


        if choice == '0':
            break
    if len(choices) == 2:
        first_word = choices[0]
        second_word = choices[1]
        print("two word command input by player:")
        print(f"first word: {first_word}")
        print(f"second word: {second_word}")

        if first_word == 'get' or first_word == 'take':
            for item in player.current_room.items:
                if item == second_word:
                    player.add_item(item)
                    print(f"You have picked up {player.current_room.items[-1]}")
                    player.current_room.remove_item(item)
                else:
                    print(f"there is no {second_word} in this room")








    # Print

    print(f"{player.name} chose {choice}")
