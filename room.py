from quest import Quest
class Room:
	def __init__(self, name): #Initialises a room.
		self.name = name
		self.north = None
		self.east = None
		self.west = None
		self.south = None
		self.quest = None
	
	def get_name(self): #Returns the room's name.
		return self.name

	def get_short_desc(self): #Returns a string containing a short description of the room depending on the completion of a quest.
		return self.quest.get_room_desc()

	def get_quest_action(self): #Returns a command that the user can input to attempt the quest.
		if self.quest != None:
			return self.quest.get_action()

	def set_quest(self, q): #Sets a new quest for this room.
		self.quest = q

	def get_quest(self): #Returns a Quest object that can be completed in this room.
		return self.quest
	
	def set_path(self, dir, dest): #Creates a path leading from this room to another.
		if dir == "NORTH":
			self.north = dest
		if dir == "EAST":
			self.east = dest
		if dir == "WEST":
			self.west = dest
		if dir == "SOUTH":
			self.south = dest
	
	def draw(self): #Creates a drawing depicting the exits in each room.
		def myprint(string):
			print(string, end="")
		
		print("")
		i = 1
		while i <= 11:
			if i == 1: #North
				x = 1
				while x <= 22:
					if (x == 1) or (x == 22):
						myprint("+")
					elif (x == 11) or (x == 12):
						if self.north != None:
							myprint("N")
						else:
							myprint("-")
					else:
						myprint("-")
					x += 1
			elif i == 11: #South
				x = 1
				while x <= 22:
					if (x == 1) or (x == 22):
						myprint("+")
					elif (x == 11) or (x == 12):
						if self.south != None:
							myprint("S")
						else:
							myprint("-")
					else:
						myprint("-")
					x += 1
			
			else:
				y = 1
				while y <= 22:
					if y == 1:
						if i == 6:
							if self.west != None:
								myprint("W")
							else:
								myprint("|")
						else:
							myprint("|")
					elif y == 22:
						if i == 6:
							if self.east != None:
								myprint("E")
							else:
								myprint("|")
						else:
							myprint("|")
					else:
						myprint(" ")
					y += 1
			print()
			i += 1
		print("You are standing at the " + self.get_name() +".")
		if self.quest != None:
			if self.quest.completed == False:
				print(self.get_short_desc())
			if self.quest.completed == True:
				print(self.get_short_desc())
		else:
			print("There is nothing in this room.")
	
	def move(self, dir): #Returns an adjoining Room object based on a direction given.
		if dir == "NORTH":
			return self.north
		if dir == "EAST":
			return self.east
		if dir == "SOUTH":
			return self.south
		if dir == "WEST":
			return self.west
			
