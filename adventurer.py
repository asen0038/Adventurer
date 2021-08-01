from item import Item
class Adventurer:
    def __init__(self): #Initialises an adventurer object.
        self.inventory = []
        self.skill = 5
        self.will = 5

    def get_inv(self): #Returns the adventurer's inventory.
        return self.inventory

    def get_skill(self): #Returns the adventurer's skill level.
        if self.skill < 0:
            self.skill = 0 #Skill level never goes below zero
        return self.skill

    def get_will(self): #Returns the adventurer's will power.
        if self.will < 0:
            self.will = 0 #Will power never goes below zero.
        return self.will

    def take(self, item): #Adds an item to the adventurer's inventory.
        self.inventory.append(item)

    def check_self(self): #Shows adventurer stats and all item stats.
        print("You are an adventurer, with a SKILL of 5 and a WILL of 5.")
        print("You are carrying:")
        print("")
        if len(self.inventory) == 0:
            print("Nothing.")
            print("")
        else:
            i = 0
            while i < len(self.inventory): #Loop used so that all the item stats are printed.
                self.inventory[i].get_info() #gets item stats
                print("")
                i += 1
        print("With your items, you have a SKILL level of " + str(self.get_skill()) + " and a WILL power of " + str(self.get_will())+".")
        print("")
