class Item:
	def __init__(self, name, short, skill_bonus, will_bonus): #Initialises an item.
		self.name = name
		self.short = short
		self.skill_bonus = skill_bonus
		self.will_bonus = will_bonus

	def get_name(self): #Returns an item's name.
		return self.name

	def get_short(self): #Returns an item's short name.
		return self.short

	def get_info(self): #Prints information about the item.
		print(self.get_name())
		print("Grants a bonus of " + str(self.get_skill()) + " to SKILL.")
		print("Grants a bonus of " + str(self.get_will()) + " to WILL.")

	def get_skill(self): #Returns the item's skill bonus.
		return int(self.skill_bonus)

	def get_will(self): #Returns the item's will bonus.
		return int(self.will_bonus)
