# Implement a class to hold room information. This should have name and
# description attributes.
#


class Room:
    def __init__(self, name, description, is_light, *items):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []
        self.items.append(items)

    def remove_item(self, item):
        self.item = item
        self.items.remove(item)

    def add_item(self, item):
        self.item = item
        self.items.append(item)

    # def __str__(self):
    # return (f"Name: {self.name}\n Description: {self.description}\n")
