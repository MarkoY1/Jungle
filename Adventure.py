from Room import Room
from Inventory import Inventory
print 'JUNGLE'
print 'You wake up on a dirt jungle floor.'
JungleFloor = Room('JungleFloor', 'Start', 'J')
Cave = Room('Entrance to Cave', 'You are inside the cave but it is too dark to see.', 'c')
CliffSide = Room('CliffSide', 'You see the Cliff-side in front of you and can not climb it.', 'cs')
DenseJungle = Room('Dense Jungle', 'You are in front of a Dense jungle.', 'j')
Tribe = Room('Tribe', 'You see a tribe that is about a mile away.', 't')
InsideCave = Room('Inside cave', 'You are inside the cave and you see...', 'ic')
InsideJungle = Room('Inside Jungle', 'You are inside a wild jungle.', 'ij')
TallTree = Room('Tall Tree', 'You climb the tall tree and find a torch.', 'tt')
Trail = Room('Trail', 'You start walking down a trail towards the tribe.', 'tr')

JungleFloor.add_connection(Cave, "Cave entrance", ["north", "n"])
Cave.add_connection(JungleFloor, 'trail to the exit', ["south", "s"])
InsideCave.add_connection(InsideCave, "passage", ["west", "w"])

JungleFloor.add_connection(CliffSide, "CliffSide", ["west", "w"])
CliffSide.add_connection(JungleFloor, "YES", ["east", "e"])

JungleFloor.add_connection(DenseJungle, "Dense Jungle", ["south", "s"])
DenseJungle.add_connection(Cave, "YeS", ["north", "n"])
DenseJungle.add_connection(InsideJungle, "Wild Jungle you see tall trees all around and one very tall tree to the", ["west", "w"])
InsideJungle.add_connection(TallTree, "You climb the tree and find a flashlight on top of the tree", ["north", "n"])


JungleFloor.add_connection(Tribe, "Tribe", ["east", "e"])
Tribe.add_connection(JungleFloor, "YES", ["west", "w"])

inventory = Inventory()
current_room = JungleFloor
current_room.enter_room(inventory)

while True:
    command = raw_input("what would you like to do?")
    if command in ["exit", "x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        result.enter_room(inventory)
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
        print "I don't know what you mean."

while True:
    direction = raw_input("What direction do you want to go?")
    if (current_room.is_valid_direction(direction)):
        current_room = current_room.next_room(direction)
        current_room.enter_room()
    elif direction == 'x':
        break
    else:
        print "Ouch! You ran into a wall."


        pass
