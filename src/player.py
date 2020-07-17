# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room, inventory):
        self.name = None
        self.current_room = starting_room
        self.inventory = inventory
    
    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You can not move in that direction")
    
    def get_item(self, current_room, item):
        print(current_room.item)