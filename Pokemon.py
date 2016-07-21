class Pokemon:
	def __init__(self,species, hp, Type, attack, defense, special_attack, special_defense,attack1,attack2):
		#stats
		self.species = species
		self.hp = hp
		self.Type = Type
		self.attack = attack
		self.defense = defense
		#self.special_attack = special_attack
		#self.special_defense = special_defense
		#self.speed = speed
		self.attack1 = attack1
		self.attack2 = attack2

		#Stat get/set
	def species(self):
		return(self.species)

	def species(self,new_species):
		self.species = new_species
		return(self.species)

	def get_hp(self):
		return(self.hp)

	def set_hp(self,new_hp):
		return

	def get_Type(self):
		return(self.Type)

	def get_attack(self):
		return(self.attack)

	def get_defense(self):
		return(self.defense)

	def get_special_attack(self):
		return(self.special_attack)

	def get_special_defense(self):
		return(special_defense)

	def get_speed(self):
		return(speed)

#		Attacks
	def take_damage(self, amount):
		self.hp = self.hp - amount
		return(self.hp)

	def give_damage(victim, amount):
		victim.hp = victim.hp - amount
		return(victim.hp)


	def attack1(self, victim):				#think about doing one defintion with a dictionary or list So no repeat of attack functions
		victim_hp = victim.takedamage(self.attack1.get_damage())
		print("Victim's new hp is {}, it went down by {}".format(victim_hp, self.attack1_damage))

	def attack2(self,victim):
		victim_hp = victim.takedamage(self.attack1_damage)
		print("Victim's new hp is {}, it went down by {}".format(victim_hp, self.attack2_damage))



class AttackMechanics:
	def __init__(self,damage,pp,accuracy):
		#stats
		self.damage = damage
		self.pp = pp
		self.accuracy = accuracy

	def get_damage(self):
		return(self.damage)


	def get_pp(self):
		return(self.pp)

	def set_pp(self,new_pp):
		self.pp = (self.pp - 1)
		return(self.pp)


	def get_accuracy(self):
		return(accuracy)

	def set_damage(self,new_damage):
		self.damage = new_damage
		return(self.damage)





tackle = AttackMechanics(35,40,100)
flamethrower = AttackMechanics(75,25,89)

print(tackle.get_damage())



infernape = Pokemon("infernape",207, "Fire", 150,75,tackle,flamethrower)
mewtwo = Pokemon("Mewtwo",300, "Psychic", 150,100,tackle,flamethrower)


infernape.attack1(mewtwo)