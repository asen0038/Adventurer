from item import Item
from adventurer import Adventurer
class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		#Initialises a quest.
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.req = req
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.completed = False
		self.skill_req = int
		self.will_req = int

	def requirements(self): #Sets the requirements for the quest.
		ls = self.req.split(" ")
		if ls[0] == "SKILL":
			self.skill_req = ls[1]
			return int(self.skill_req)
		if ls[0] == "WILL":
			self.will_req = ls[1]
			return int(self.will_req)
	
	def get_reward(self): #returns the reward or an item object of the corresponding quest.
		return self.reward
	
	def get_info(self): #Returns the quest's description.
		return self.desc

	def is_complete(self): #Returns whether or not the quest is complete.
		self.completed = True #Function is only called after the quest is complete
		return self.completed

	def get_action(self): #Returns a command that the user can input to attempt the quest.
		return self.action

	def get_room_desc(self): #Returns a description for the room that the quest is currently in.
		if self.completed == True:
			return self.after #Room description when the quest is completed.
		else:
			return self.before #Room description when the quest is yet to be completed.

	def attempt(self, player): #Allows the player to attempt this quest depending on the players skill/will.
		if (player.get_skill() >= self.requirements()) or (player.get_will() >= self.requirements()):
			print(self.pass_msg) #prints if the player is eligible to complete the quest
			player.skill = player.get_skill() + self.reward.get_skill()
			player.will = player.get_will() + self.reward.get_will()
			return True
		else:
			print(self.fail_msg) #prints if the player is unable to complete the quest
			return False
		
