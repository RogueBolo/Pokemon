
import random
import time

class Pokemon:
        def __init__(self,species, hp, Type, attack, defense,attack_1,attack_2):
                #stats
                self.species = species
                self.hp = hp
                self.Type = Type
                self.attack = attack
                self.defense = defense
                #self.special_attack = special_attack
                #self.special_defense = special_defense
                #self.speed = speed
                self.attack_1 = attack_1
                self.attack_2 = attack_2

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

#Attacks
        def take_damage(self, amount):
                self.hp = self.hp - amount
                return(self.hp)

        def give_damage(victim, amount):
                victim.hp = victim.hp - amount
                return(victim.hp)


        def attack1(self, victim):                              #think about doing one defintion with a dictionary or list So no repeat of attack functions
                victim_hp = victim.take_damage(self.attack_1.get_damage())
                print("Victim's new hp is {}, it went down by {}".format(victim_hp, self.attack_1.get_damage()))

        def attack2(self,victim):
                victim_hp = victim.take_damage(self.attack_2.get_damage())
                print("Victim's new hp is {}, it went down by {}".format(victim_hp, self.attack_2.get_damage()))



class AttackMechanics:
        def __init__(self,damage,pp,accuracy):
                #stats
                self.damage = damage
                self.pp = pp
                self.accuracy = accuracy

        def get_damage(self):
                return(self.damage)

        def set_damage(self,new_damage):
                self.damage = new_damage
                return(self.damage)



        def get_pp(self):
                return(self.pp)

        def set_pp(self,new_pp):
                self.pp = (self.pp - 1)
                return(self.pp)


        def get_accuracy(self):
                return(self.accuracy)


        def set_accuracy(self, new_accuracy):
                self.accuracy = new_accuracy
                return(self.accuracy)

 

        
#ATTACK ACCURACIES SET TO 100 FOR TESTING
tackle = AttackMechanics(35,40,100)
flamethrower = AttackMechanics(75,25,100)


#hits or misses based on the accuracy of the attacks, set at 40
attack_1 = tackle
attack_2 = flamethrower




p = input("What pokemon would you like to use?(infernape or mewto)\n")


z = input("What attack to use?(tackle or flamethrower)\n")

if z == "tackle":
        accuracy = tackle.get_accuracy()
       

elif z == "flamethrower":
        accuracy = flamethrower.get_accuracy()





a = accuracy
x = random.randint(1,100)



if x >= a:
        print("Miss!")
        y = False

else:
        print("Hit!")
        y = True

        
infernape = Pokemon("infernape",207, "Fire", 150,75,tackle,flamethrower)
mewtwo = Pokemon("Mewtwo",300, "Psychic", 150,100,tackle,flamethrower)


if y == True:
        if z == "tackle":
                print(tackle.get_damage())
                if p == "infernape":
                        print("Infernape attacked with tackle!")
                        time.sleep(1)
                        infernape.attack1(mewtwo)
                        print("ouch.")

                elif p == "mewto":
                        print("Mewto attacked with tackle!")
                        time.sleep(1)
                        mewtwo.attack1(infernape)
                        print("ouch.")

        elif z == "flamethrower":
                print(flamethrower.get_damage())
                if p == "infernape":
                        print("Infernape attacked with flamethrower!")
                        time.sleep(1)
                        infernape.attack2(mewtwo)
                        print("ouch.")

                elif p == "mewto":
                        print("Mewtwo attacked with flamethrower!")
                        time.sleep(1)
                        mewtwo.attack2(infernape)
                        print("ouch.")
                
      
