# Implement a class to hold room information. This should have name and
# description attributes.
#


class Room:
    def __init__(self, name, description, is_light, n_to=None, s_to=None, e_to=None, w_to=None, *items):
        self.name = name
        self.description = description
        self.is_light = is_light
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []
        for item in items:
            self.items.append(items)

    def remove_item(self, item):
        self.item = item
        self.items.remove(item)


    def add_item(self, item):
        self.item = item
        self.items.append(item)

    # def __str__(self):
    # return (f"Name: {self.name}\n Description: {self.description}\n")
