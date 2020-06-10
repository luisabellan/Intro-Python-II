# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

   # def __str__(self):
    #    return (f"Name: {self.name}\nCurrent room: {self.current_room}\n")

    # this method isn't working
    def set_current_room(self, room):

        Player.current_room = room
