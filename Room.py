class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items =[]
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def enter_room(self):
        print self.name
        print
        print self.description
        print
        for direction in self.rooms.keys():
            print "to the " + direction + " is a " + self.rooms[direction].get_name()

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

    def connect_room(self, direction, room):
        opposite_direction = {'n':'s','s': 'n','e': 'w','w': 'e'}
        self.add_room(direction, room)
        room.add_room(opposite_direction[direction], self)

kitchen = Room('kitchen', 'You are in the kitchen.', 'k')
dining = Room('Dining', 'You are in the dining room.', 'd')
hallway = Room('Hallway', 'You are in the hallway.', 'h')
hallway2 = Room('Upstairs Hallway', 'You are in the hallway.', 'uh')
bedroom1 = Room('bedroom', 'You are in a bedroom.', 'b1')
bedroom2 = Room('bedroom', 'You are in a bedroom.', 'b2')
bedroom3 = Room('bedroom', 'You are in a bedroom.', 'b3')
living = Room('Living Room', 'You are in the living room.', 'lr')

kitchen.add_room('n', dining)
dining.add_room('s', kitchen)
dining.add_room('n', hallway)
hallway.add_room('s', dining)
hallway.add_room('u', hallway2)
hallway.add_room('e', living)
living.add_room('w', hallway)
hallway2.add_room('d', hallway)
hallway2.add_room('n', bedroom1)
hallway2.add_room('e', bedroom2)
hallway2.add_room('w', bedroom3)

current_room = dining
current_room.enter_room()

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