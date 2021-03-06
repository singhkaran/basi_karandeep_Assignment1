import math
import random

random.seed()

class Ship(object):
	shield = 100
	hullStrength = 100
	laserStrength = 50
	destroyed = False

	def __init__(self, name):
		self.name = name
	def attack(self, target):
		print "{0} fired a laser at {1}!".format(self.name, target.name)
		target.handleAttack(self, self.laserStrength)
	def handleAttack(self, attacker, damage):
		if (self.shield > 0):
			self.hitShield(attacker, damage)
		else:
			self.hitHull(attacker, damage)

	def hitShield(self, attacker, damage):
		self.shield -= damage
		print "{0} took {1} shield damage from {2}! Shield is now at {3}".format(self.name, damage, attacker.name, self.shield)
		# carry damage that hit "past" the shield through to the hull
		if (self.shield < 0):
			self.hitHull(attacker, -self.shield)
			self.shield = 0
			

	def hitHull(self, attacker, damage):
		self.hullStrength -= (damage * 0.5)
		print "{0} took {1} hull damage from {2}! Hull Strength is now at {3}".format(self.name, damage * 0.5, attacker.name, self.hullStrength)
		if self.hullStrength <= 0:
			self.destroyed = True
			print "{0} was destroyed!".format(self.name)
		
	def printShipStatus(self):
		print "Name: {0}, Shield: {1}, Hull Strength: {2}, Destroyed?: {3}".format(self.name, self.shield, self.hullStrength, self.destroyed)

class Warship(Ship):
	missleStrength = 100
	def attack(self, target):
		if (random.random() >= 0.3):
			print "{0} fired a missile at {1}!".format(self.name, target.name)
			target.handleAttack(self, self.missleStrength)
		else:
			print "{0} fired a laser at {1}!".format(self.name, target.name)
			target.handleAttack(self, self.laserStrength)

class Speeder(Ship):
	def handleAttack(self, attacker, damage):
		if (random.random() > 0.5):
			Ship.handleAttack(self, attacker, damage)
		else:
			print "{0} dodged {1}'s attack!".format(self.name, attacker.name)

# Simulate a battle

ship = Ship("Standard Ship")
warShip = Warship("Warship")
speeder = Speeder("Speeder")

shipsAlive = [ship, warShip, speeder]

while len(shipsAlive) > 1:
	random.shuffle(shipsAlive)
	for i in shipsAlive:
		target = random.choice([x for x in shipsAlive if x != i])
		i.attack(target)
		if target.destroyed:
			shipsAlive.remove(target)
			break

print shipsAlive[0].name + " is the victor!"
			



