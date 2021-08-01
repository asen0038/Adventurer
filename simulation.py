from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

if len(sys.argv) < 4:
	print("Usage: python3 simulation.py <paths> <items> <quests>")
	sys.exit()

def read_paths(source): #Returns a list of pathway lists according to the specifications in a config file.
	
	f = open(source, "r")
	paths = []
	line = None
		
	while line != "":
		line = f.readline()
		line = line.strip("\n")
		paths.append(line.split(" > "))
	del paths[len(paths)-1]
	
	f.close()

	return paths


def create_rooms(paths): #Receives a list of paths and returns a list of rooms based on those paths.
	
	paths = read_paths(paths)
	rooms = []
	rooms_str = []
	all_rooms = []
	directions = []
	i = 0
	j = 0
	x = 0
	room = None
	room_str = ""
	while i < len(paths):
		while j < len(paths[i]):
			if j != 1:
				room_str = paths[i][j]
				if room_str not in rooms_str: #Checks if a room is already in the list.
					rooms_str.append(room_str) #Adds the unique room into another list to avoid duplication.
				while x != len(rooms_str):
					room = Room(rooms_str[x]) #Creates a unique room object.
					rooms.append(room) #List of Room Objects.
					x += 1
				all_rooms.append(Room(room_str)) #List of Room Objects of every single room from the paths list in order.
			if j == 1:
				directions.append(paths[i][j]) #List of the cardinal directions taken from the paths list.
			j += 1
		j = 0
		i += 1
	
	ls = []
	i = 0
	j = 0
	while i < len(all_rooms): #This loop checks if a unique room object is the same as a Room object in a list of ALL the rooms.
		while j < len(rooms):
			if rooms[j].get_name() == all_rooms[i].get_name(): 
				all_rooms[i] = rooms[j] #This sets all the rooms to have their own unique Room type Objects.
				ls.append(all_rooms[i])
			j += 1
		j = 0
		i += 1
	
	i = 0
	j = 0
	while i < len(ls):
		while j < len(directions): #Sets path using the unique Room Object along with the directions list.
			all_rooms[i].set_path(directions[j], all_rooms[i + 1]) 
			j += 1
			i += 2
	
	return rooms

def generate_items(source): #Returns a list of items from the specifications in a config file.

	f = open(source, "r")
	thing = []
	line = None
		
	while line != "":
		line = f.readline()
		line = line.strip("\n")
		thing.append(line.split(" | "))
	f.close()
	
	del thing[len(thing)-1] #Deletes an uneccessary occuring of empty list in the end while reading files.
	
	items = []
	i = 0
	j = 0
	item = None
	while i < len(thing):
		while j < len(thing[i]):
			if j == 0: #Creates Item Objects
				item = Item(thing[i][j], thing[i][j+1], thing[i][j+2], thing[i][j+3])
				items.append(item)
			j += 1
		j = 0
		i += 1

	return items

def generate_quests(source, items, rooms): #Returns a list of quests from the specifications in a config file.
	
	f = open(source, "r")
	read_quest = []
	line = f.readline()
	while line != "":
		line = line.strip("\n")
		read_quest.append(line.split(" | "))
		line = f.readline()
	f.close()

	i = 0
	j = 0
	while i < len(read_quest): #Removes uneccessary empty lists that might have occured during file reading
		while j < len(read_quest[i]):
			if read_quest[i][j] == "":
				del read_quest[i]
			j += 1
		j = 0
		i += 1
	
	quests = []
	quest = None
	item = None
	room = None
	i = 0
	j = 0
	while i < len(read_quest):
		while j < len(read_quest[i]):
			x = 0
			y = 0
			if j == 0:
				y = 0
				while y < len(items): #Sets the Item Object from the items in generate_items for the corresponding Quest Object.
					if read_quest[i][j] == items[y].get_name():
						item = items[y]
					y += 1
			if j == 1:
				action = read_quest[i][j]
			if j == 2:
				description = read_quest[i][j]
			if j == 3:
				before = read_quest[i][j]
			if j == 4:
				after = read_quest[i][j]
			if j == 5:
				req = read_quest[i][j]
			if j == 6:
				fail_msg = read_quest[i][j]
			if j == 7:
				pass_msg = read_quest[i][j]
			if j == 8:
				room = Room(read_quest[i][j])
				x = 0
				while x < len(rooms): 
					if rooms[x].get_name() == room.get_name(): #Creates a Room Object from the creat_rooms for the corresponding Quest Object.
						room = rooms[x]
						quest = Quest(item, action, description, before, after, req, fail_msg, pass_msg, room) #Creates a Quest Object
						room.set_quest(quest)
						quests.append(quest)
					x += 1
			j += 1
		j = 0
		i += 1
		
	return quests

try:
	source_path = sys.argv[1]
	source_item = sys.argv[2]
	source_quest = sys.argv[3]
	
	rooms = create_rooms(source_path)
	items = generate_items(source_item)
	quests = generate_quests(source_quest, items, rooms)
	
except FileNotFoundError:
	print("Please specify a valid configuration file.")
	sys.exit()

if len(rooms) == 0: #No rooms.
	print("No rooms exist! Exiting program...")
	sys.exit()	

current_room = rooms[0]
current_room.draw() #Draws the first room.
print("")
player = Adventurer() #Creates the player or the user for the game.
inventory = player.get_inv() #Creates an inventory for the player to store rewards/items Objects.

while True:
	user_input = input(">>> ")
	
	if user_input.upper() == "QUIT":
		print("Bye!")
		break
	
	if user_input.upper() == "INV":
		print("You are carrying:")
		if len(inventory) == 0: #No items
			print("Nothing.")
		else:
			i = 0
			while i < len(inventory):
				print("- A " + inventory[i].get_name())
				i += 1
		print("")
		continue
	
	if user_input.upper() == "CHECK":
		second_input = input("Check what? ")
		print("")
		
		if second_input.upper() == "ME":
			player.check_self() #Gets item info with player stats.
		
		else:
			i = 0
			while i < len(inventory): #Gets item info
				if second_input.upper() == inventory[i].get_name().upper():
					inventory[i].get_info() 
					print("")
					print("")
				if second_input.upper() == inventory[i].get_short().upper():
					inventory[i].get_info()
					print("")
					print("")
				i += 1
			
			count = 0
			j = 0
			while j < len(inventory): #Checks if the item is not in the inventory.
				if (second_input.upper() != inventory[j].get_name().upper()) and (second_input.upper() != inventory[j].get_short().upper()):
					count += 1
				j += 1
			if count == len(inventory): #If the item does not match any item in the inventory then this will be true.
				print("You don't have that!")
				print("")
		continue
	
	if user_input.upper() == "QUESTS":
		if len(quests) == 0: #No quests
			print("")
			print("=== All quests complete! Congratulations! ===")
			sys.exit()
		
		i = 0
		c = 0
		while i < len(quests):
			if quests[i].completed == True: #Print statement if quest is completed.
				print("#0"+str(i) + ": {:<21}".format(quests[i].get_reward().get_name()) + "- " + quests[i].get_info() + " [COMPLETED]")
				c += 1
			if quests[i].completed == False: #Print statement if quest is yet to be complete.
				print("#0"+str(i) + ": {:<21}".format(quests[i].get_reward().get_name()) + "- " + quests[i].get_info())
			if c == len(quests):
				print("")
				print("=== All quests complete! Congratulations! ===")
				sys.exit()
			i += 1
		print("")
		continue
	
	if user_input.upper() == current_room.get_quest_action(): #Quest Action
		if current_room.get_quest().completed == True: #Ff quest is already completed.
			print("You have already completed this quest.")
			print("")
		if current_room.get_quest().completed == False: #If the quest is yet to be completed.
			if current_room.get_quest().attempt(player) == True: #If the player is eligible to complete the quest.
				player.take(current_room.get_quest().get_reward()) #Collects and adds the rewards from quest to the player's inventory.
				current_room.get_quest().is_complete() #Sets the quest as COMPLETED
			print("")
		continue
				
	if user_input.upper() == "NORTH" or user_input.upper() == "N":
		if current_room.move("NORTH") != None:
			print("You move to the north, arriving at the " + current_room.move("NORTH").get_name() + ".")
			current_room.move("NORTH").draw()
			current_room = current_room.move("NORTH") #Updates the current room of the player
			print("")
		else:
			print("You can't go that way.")
			print("")
		continue
	
	if user_input.upper() == "EAST" or user_input.upper() == "E":
		if current_room.move("EAST") != None:
			print("You move to the east, arriving at the " + current_room.move("EAST").get_name() + ".")
			current_room.move("EAST").draw()
			current_room = current_room.move("EAST") #Updates the current room of the player
			print("")
		else:
			print("You can't go that way.")
			print("")
		continue
	
	if user_input.upper() == "SOUTH" or user_input.upper() == "S":
		if current_room.move("SOUTH") != None:
			print("You move to the south, arriving at the " + current_room.move("SOUTH").get_name() + ".")
			current_room.move("SOUTH").draw()
			current_room = current_room.move("SOUTH") #Updates the current room of the player
			print("")
		else:
			print("You can't go that way.")
			print("")
		continue
	
	if user_input.upper() == "WEST" or user_input.upper() == "W":
		if current_room.move("WEST") != None:
			print("You move to the west, arriving at the " + current_room.move("WEST").get_name() + ".")
			current_room.move("WEST").draw()
			current_room = current_room.move("WEST") #Updates the current room of the player
			print("")
		else:
			print("You can't go that way.")
			print("")
		continue

	if user_input.upper() == "HELP":
		print("{:<11}- Shows some available commands.".format("HELP"))
		print("{:<11}- Lets you see the map/room again.".format("LOOK or L"))
		print("{:<11}- Lists all your active and completed quests.".format("QUESTS"))
		print("{:<11}- Lists all the items in your inventory.".format("INV"))
		print("{:<11}- Lets you see an item (or yourself) in more detail.".format("CHECK"))
		print("{:<11}- Moves you to the north.".format("NORTH or N"))
		print("{:<11}- Moves you to the south.".format("SOUTH or S"))
		print("{:<11}- Moves you to the east.".format("EAST or E"))
		print("{:<11}- Moves you to the west.".format("WEST or W"))
		print("{:<11}- Ends the adventure.".format("QUIT"))
		print("")
		continue
	
	if user_input.upper() == "LOOK" or user_input.upper() == "L":
		current_room.draw() 
		print("")
		continue
		
	else:
		print("You can't do that.")
		print("")
		continue
