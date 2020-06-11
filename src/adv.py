from Room import Room
from Player import Player

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

    #print(f"the room north of this one is {player.current_room.n_to.name}")
    print("Instructions:\n")
    print("Press:\n - n for north\n - s for south\n - e for east\n - w for west\n - 0 to quit\n\n")

    # REPL

    # Read
    choice = input(
        "Where do you want to go?: ")

    no_room_msg = 'There is no room in that direction'

    # Evaluate
    if choice == 'n'and player.current_room.n_to != None:

            # this method isn't working player.set_current_room(player.current_room.n_to.name)
            # player.set_current_room(player.current_room.n_to.name)
            player = Player("Luis", player.current_room.n_to)
            #player.current_room = player.current_room.n_to
            continue



    if choice == 's' and player.current_room.s_to != None:
            player = Player("Luis", player.current_room.s_to)
            #player.current_room = player.current_room.s_to
            continue





    if choice == 'e'and player.current_room.e_to != None:
            player = Player("Luis", player.current_room.e_to)
            #player.current_room = player.current_room.e_to
            continue




    if choice == 'w'and player.current_room.w_to != None:
            player = Player("Luis", player.current_room.w_to)
            #player.current_room = player.current_room.w_to
            continue
    

    if choice == '0':
        break


    # Print

    print(f"{player.name} chose {choice}")
