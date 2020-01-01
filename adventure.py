
import time

#sets the users inventory to empty.

inventory = []

#shows which rooms can be access from eachother

rooms = {'barn_attic': {'name': 'barn_attic', 'down': 'barn_ground', 'text': 'a small attic with a door and crowbar', 'contents': ['crowbar'], 'exits': {'down'}, },
        
        'barn_ground': {'name': 'barn_ground', 'up': 'barn_attic', 'east': 'east_field', 'west': 'west_field', 'text': 'you are in a large wooden barn.', 'contents': [], },

        'east_field': {'name': 'east_field', 'west': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field with lots of crops', 'contents': ['crops'], },

        'west_field': {'name': 'west_field', 'east': 'barn_ground', 'south': 'behind_barn', 'text': 'a large, open field with lots of crops', 'contents': ['crops'], },

        'behind_barn':{'name': 'behind_barn', 'east': 'east_field', 'west': 'west_field', 'north': 'staircase', 'text': 'behind the large barn', 'contents': [], },
        
        'staircase':{'name': 'staircase', 'south': 'behind_barn', 'east': 'cell_room', 'text': 'a slim, stone staircase with a single torch.', 'contents': ['torch'], }, 
        
        'cell_room':{'name':'cell_room', 'west': 'staircase', 'north': 'cavern', 'east': 'dining_hall', 'text':  'a large room with many cells, some including skeletons.', 'contents': []},
        
        'cavern': {'name': 'cavern', 'north': 'cavern', 'east': 'chest_room', 'south': 'cell_room', 'text': "it's just a cavern", 'contents': [], },
        
        'chest_room': {'name': 'chest_room', 'east': 'throne_room', 'west': 'cavern', 'text': 'a large hall with a golden encrusted throne sat atop a pedesatl.', 'contents':[], },
        
        'throne_room':{'name': 'Throne_room', 'north': 'Dining_hall', 'east': 'chest_room', 'west': 'Treasure_hall'}}

        

directions = ['north',  'east',  'south',  'west', 'up', 'down']

###################################################################################

#defines an exit from the user
def user_exit():
    print('are you sure')
    command = input(user_input)
    if 'yes' in command:
        print('goodbye')
        exit
    else:
        print(current_room['text'])
        print('_' * len(current_room['text']) + '\n' * 2)


#defines the function used to display room context.
def user_look():
    print('\n' + current_room['name'])
    print('_' * len(current_room['name']) + '\n')
    print(current_room['text'])
    print('_' * len(current_room['text']) + '\n')

#checks for which exits are available in each room.
def exit_check():
        if 'east' in current_room:
            print('east')
            time.sleep(1)
        if 'west' in current_room:
            print('west')
            time.sleep(1)
        if 'north' in current_room:
            print('north')
            time.sleep(1)
        if 'south' in current_room:
            print('south')
            time.sleep(1)
        if 'up' in current_room:
            print('up')
            time.sleep(1)
        if 'down' in current_room:
            print('down')
            time.sleep(1)

###################################################################################

user_input = '\n'':'
print('\n' * 2)

name = str(input("Hi, what's your name? "))
welcome = str('hello, ' + name)

print('\n' * 2)
print(welcome)
print('*' * len(welcome))

print('welcome to my prototype of my text adventure game')
print('enter commands to control your character' + '\n' * 2)
time.sleep(1)

print('you awake upon a bale of hay in a large, wooden barn.')

current_room = rooms['barn_ground']

#main game loop
while True:
    
    rounddone = False
    text = current_room['text']
    
    command = input(user_input)
    command = command.lower()

    if len(command) == 1:
        if  command in 'e':
            command = 'east'
            rounddone = True

        if  command in 'w':
            command = 'west'
            rounddone = True

        if  command in 's':
            command = 'south'
            rounddone = True

        if  command in 'n':
            command = 'north'
            rounddone = True

        if  command in 'u':
            command = 'up'
            rounddone = True

        if  command in 'd':
            command = 'down'
            rounddone = True
        
        if  command in 'i':
            command = 'inventory'
            rounddone = True
    
    if 'look' in command.lower():
        user_look()
        rounddone = True

    elif command.lower() in ('q', 'quit', 'exit'):
        user_exit()
        if command.lower() == 'yes':
            rounddone = True
            break
            
    
    if command.lower() in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
            print(current_room['name'])
            rounddone = True
        else:
            print("You can't go that way.")
            rounddone = True
    
    if len(command) > 0:
        if command.lower().split()[0] in ('get', 'take'):
            item = command.lower().split()[1]
            if item in current_room['contents']:
                current_room['contents'].remove(item)
                inventory.append(item)
                print(item + ' is now in your inventory')
                rounddone = True
            else:
                print(item + ' is not in the room')
                rounddone = True
    
    if len(command) > 0:
        if command.lower().split()[0] == 'drop':
            item = command.lower().split()[1]
            if item in inventory:
                current_room['contents'].append(item)
                inventory.remove(item)
                print(' you have dropped' + item)
                rounddone = True
            else:
                print(item + ' is not in your inventory')
                rounddone = True
    
    if 'inventory' in command.lower():
        print(inventory)
        rounddone = True
    
    if 'exits' in command.lower():
        exit_check()
        rounddone = True
    
    

    #######################
    elif rounddone == False:
        print("sorry, i didn't understand that.")
        rounddone = True