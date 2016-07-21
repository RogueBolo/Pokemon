#gotta catch them all

class Pokemon:
    def __int__(self, hp, species, power, defense, attack):
        self.species = species
        self.hp = hp
        self.power = power
        self.defense = defense
        self.attack = attack
 
        


        #Get and Set
    def get_species(self):
        return(self.species)

    def set_species(self, new_species):
        self.species = new_species
        return(self.species)

    def get_hp(self):
        return(self.hp)

    def set_hp(self, new_hp):
        self.hp = new_hp
        return(self.hp)

    def get_power(self):
        return(self.power)

    def set_power(self, new_power):
        self.power = new_power
        return(self.power)

    def get_defense(self):
        return(self.defense)

    def set_defense(self, new_defense):
        self.defense = new_defense
        return(self.defense)

    def get_attack(self):
        return(self.attack)

    def set_attack(self, new_attack):
        self.attack = new_attack
        return(self.attack)

    def take_damage(self, amount):
        victim_hp = victim.take.damage(self.attack1.get_damage())
        print("Victim's new hp is {}. It went down by {}.".format(victim_hp, self.attack1.get_damage()))
infernate = Pokemon(207, "fire", 175, 75, flamethrower)
mewto = Pokemon(500, "fire", 175, 75, flamethrower)

infernate.attack(mewto)

class attack1:
    def __int__(self, damage, duration, style):
        self.damage = damage
        self.duration = duration
        self.style = style

        #set and get
    def get_damage(self):
        return(self.damage)

    def set_damage(self, new_damage):
        self.damage = new_damage
        return(self.damage)

    def get_duration(self):
        return(self.duration)

    def set_duration(self, new_duration):
        self.duration = new_duration
        return(self.duration)

    def get_defense(self):
        return(self.defense)

    def set_defense(self, new_defense):
        self.defense = new_defense
        return(self.defense)

    def get_style(self):
        return(self.style)

    def set_style(self, new_style):
        self.style = new_style
        return(self.style)


flamethrower = attack1(50, 3, "fire")

    

        
        



        



        

    

        

        
        
    
    
