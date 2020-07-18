# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, starting_room, inventory):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
    
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You can not move in that direction")
    def get(self, item):
        for items in self.current_room.items:
            if item in items.name:
                print(f"{self.name} got {items.name}")
                self.inventory.append(items)
                #delattr(self.current_room.items, items.name)
                self.current_room.items.pop(self.current_room.items.index(items))
            else:
                print("cant get that")
    def drop(self, item):
        for items in self.inventory:
            if item in items.name:
                print(f"dropped {items.name}")
                self.current_room.items.append(items)
                self.inventory.pop(self.inventory.index(items))
            else:
                print("cant drop that")



