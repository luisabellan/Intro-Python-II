from Room import Room
from Player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = None
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


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


player = Player("Luis", "outside")
# print(player)


choice = -1
while choice != 0:

    print(f"{player.current_room}")
    print("Instructions:\n")
    print("Press:\n - n for north\n - s for south\n - e for east\n - w for west\n - 0 to quit\n\n")

    # REPL

    # Read
    choice = input(
        "Where do you want to go?: ")

    no_room_msg = 'There is no room in that direction'

    # Evaluate
    if choice == 'n':
        chosen_direction = 'north'

        if room[player.current_room].n_to != None:

            # this method isn't working player.set_current_room(room[player.current_room].n_to.name)
            # player.set_current_room(room[player.current_room].n_to.name)
            player.current_room = room[player.current_room].n_to.name
            #print(f"the room north of this one is {room[player.current_room].n_to.name}")

        else:
            chosen_direction = no_room_msg


    elif choice == 's':
        chosen_direction = 'south'

        if room[player.current_room].s_to != None:
            player.current_room = room[player.current_room].s_to.name
        else:
            chosen_direction = no_room_msg



    elif choice == 'e':
        chosen_direction = 'east'
        if room[player.current_room].e_to != None:
            player.current_room = room[player.current_room].e_to.name
        else:
            chosen_direction = no_room_msg



    elif choice == 'w':
        chosen_direction = 'west'
        if room[player.current_room].w_to:
            player.current_room = room[player.current_room].w_to.name
        else:
            print(no_room_msg)
            chosen_direction = no_room_msg
            
    else:
        continue

    # Print

    print(f"{player.name} moved {chosen_direction}")
