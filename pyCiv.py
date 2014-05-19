# Python 3.x
# PyCiv -- PyCiv.py
# v 0.1

# An attempt at implementing PocketCiv into Python. PocketCiv can be
# found at http://www.backglass.org/scotts/games/PocketCiv/html/index.htm

from random import getrandbits as rbit, randint, sameple, shuffle
import deck
# CLASS SETUP
class card:
	def __init__(self,number,circle,square,hex,gold,friendly,events):
		self.number=number
		self.circle=circle
		self.square=square
		self.hex=hex
		self.gold=gold
		self.friendly=friendly # friendly is either True or False, and is signalled by the presence of a handshake on the card
		self.events={} # is a dictionary because there's the era (key) and event (value)
class region:
	def __init__(self, number):
		self.number=i
		self.tribes=0
		self.city=0
		self.mountain=0 # 1 is mountain, 2 is volcano
		self.forest=False
		self.farm=False
		self.desert=False
		self.fault=False
		self.fronteir=False # borders frontier
		self.water=False # borders sea
	def tribeUp(self,n):
		self.tribes+=n
	def tribeDown(self,n):
		if n>self.tribes:self.tribes=0
		else:self.tribes-=n
	def cityUp(self,n):
		self.city+=n
	def cityDown(self,n):
		self.city-=n
		if self.city<0:self.city=0
		if self.city=0: print("City in region %s has been decimated."%self.number)
	def maxSupport(self):
		pass
# CLASS-DRAWER SETUP
class world:
	import advance
	glory=0
	gold=0
	era=0
	mountain=[] #list of region with mountains/volcanoes
	forest=[] # list of region with forest
	desert=[] # list of regions with desert
	city=[] # list of regions with a city
# UNION FUNCTIONS
def antiunion(a,b,c=range(8)) # find if an element not in a and b but is in c
	antiunion=[]
	for i in c:
		if i not in a and i not in b: antiunion+=[i]
	return antiunion
def parunion(a,b): # find items in a but not b
	parunion=[]
	for i in a:
		if i not in b: parunion+=[i]
	return parunion
def union(a,b): # intersect of lists a,b
	union=[]
	for i in a: if i in b: union.append(i)
	return union

	# INITIALIZE THINGS
# SET blank regions
regionList=[region(i) for i in range(8)]
# SET mountains
for i in sample(range(8),5):
	regionList[i].mountain=1
	world.mountain+=[i]
# SET forests
for i in sample(range(8),5):
	regionList[i].forest=True
	world.forest+=[i]
# SET deserts
world.desert=antiunion(world.mountain,world.forest) # finds region without forest or mtn
if world.desert==[]: # if none found, pick 1 region with mountain but no forest
	world.desert=sample(parunion(world.mountain,world.forest),1)
for i in world.desert: # applies desert to region
	regionList[i].desert=True
# SET tribes
	# place 3 tribes in the whole world.
# SET deck
deck.reset()