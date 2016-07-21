class Pokemon:
	def __init__(self, hp, Type, attack, defense, special_attack, special_defense):
		self.hp = hp
		self.Type = Type
		self.attack = attack
		self.defense = defense
		self.special_attack = special_attack
		self.special_defense = special_defense

	def get_hp(self):
		return(self.hp)

	def get_type(self):
		return(self.Type)

	def get_attack(self):
		return(self.attack)

	def get_defense(self):
		return(self.defense)

	def get_special_attack(self):
		return(self.special_attack)

	def get_special_defense(self):
		return(self.special_defense)

pkmn = Pokemon(100, "Dark", 60, 70, 40, 50)
print(pkmn.get_hp())
print(pkmn.get_type())
print(pkmn.get_attack())
print(pkmn.get_defense())
print(pkmn.get_special_attack())
print(pkmn.get_special_defense())