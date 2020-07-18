from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"
                     ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
[]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
[]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
[]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! The gold is yours! Type "get gold" to get the gold!"""),
}

room['outside'].items = [Item('flower', 'the first thing you can pick up'), Item('book', '"Learn Python", a book that would be helpful to read')]
room['treasure'].items = [Item('gold', 'the treasure you have been looking for')]
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#q

# Make a new player object that is currently in the 'outside' room.
print("Hello\nIn this game you can move in the cardinal directions by inputting 'n' for north, 'e' for east, 's' for south, and 'w' for west")
print("Inputting 'i' will display items in your inventory")
print("Typing 'get' or 'take' and then the name of the item you want to pickup adds the item to your inventory")
print("Explore the cave, and find the gold!")
player = Player(input("Please enter your name: "), room['outside'], inventory=None)

print(player.name, player.current_room)

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
directions = ['n', 'e', 'w', 's']
get_or_take = ['get', 'take']
while True:
    cmd = input("\nINPUT: ").lower()
    cmd_split = cmd.split(" ")
    if cmd_split[0] in get_or_take and len(cmd_split) == 2:
        player.get(cmd_split[1])
    elif cmd_split[0] == "drop"and len(cmd_split) == 2:
        player.drop(cmd_split[1])
    elif cmd == "q":
        print("Goodbye")
        exit()
    elif cmd in directions:
        player.travel(cmd)
    elif cmd == "i":
        print("\nINVENTORY:\n")
        if len(player.inventory) > 0:
            inventory_list = []
            for i in player.inventory:
                print(f'{i.name}, {i.description}\n')
        else:
            print("Nothing in inventory")
    else:
        print("That is not a valid input")