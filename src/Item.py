

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item):
        self.item = item
        print(f"You have picked up {self.item}")


    def on_drop(self, item):
        self.item = item
        print(f"You have dropped {self.item}")
