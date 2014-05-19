#COULD WRITE A DECIMATION SCRIPT FOR FARMS THAT HAS BUILT-IN CHECK FOR IRRIGATION

def anarchy():
	if world.advance.literacy: rate=5
	else: rate=3
	if world.advance.religion:
		print('Select four regions.')
		actvList=[int(input('?>>')) for i in range(4)]
	else: actvList=world.city
	for i in actvList:
		actvRgn=regionList[i]
		while actvRgn.tribes>=actvRgn.city or actvRgn.city>1:
			actvRgn.tribes-=rate
			if not world.advance.law: actvRgn.city-=1
		if actvRgn.tribes<0:actvRgn.tribes=0
	if world.advance.slaveLabor:
		deck.draw()
		#reduce tribes thruout empire by the red circle
	if world.advance.machining and not world.advance.law:
		pass
		# pick a city or two
		# if one, reduce by two AV
		# if two, reduce each by one AV
		
# def attack

def bandits():
	deck.draw()
	actvRgn=deck.active.circle
	#if active or neighbor to active contains desert: bandits
	deck.draw(False)
	# determine attacking force by adding shapes spec'd on original card
	# split this out into a function that returns a value so i can 
	# assign it to a variable. Could then eliminate the need for an 
	# update flag
	if world.advance.law:atkForce-=deck.discard[-1].hex
	if world.advance.democracy:atkForce-=atkForce-=deck.discard[-1].hex
	if world.advance.equestrian:atkForce+=deck.discard[-1].hex
	if world.advance.slaveLabor:atkForce+=deck.discard[-1].hex
	attack(atkForce,actvRgn)
	#else disregard
	
def civilWar():
	deck.draw()
	actvRgn=deck.active.circle
	if world.advance.military: nRate=3
	else: nRate=2
	if world.advance.mythology: aRate=3
	else: aRate=2
	if world.advance.civilService: minCity=1
	else: minCity=0
	if world.advance.architecture:
		nRate-=1
		aRate-=1
	deck.draw()
	if world.advance.law: cDmg=deck.active.square
	else: cDmg=deck.active.hex
	if world.advance.arts: cDmg-=2
	if world.advance.theater: cDmg-=2
	if world.advance.meditation: cDmg//=2
	# if sum of tribes in all affected areas>cDmg: pick which affected regions to spend damage in, and how much in each
	# else damage as much as possible in each region
	# if world.advance.medicine: +1 tribe in each of the affected regions
	
def corruption():
	# corruption=the shape multiplier fucntion thing
	if world.advance.government: corruption+=3
	if world.advance.literacy: corruption//=2
	# pick any and all cities, reduce cities until either all 
	# corruption is spent or tere are no more cities left to reduce
	if not world.advance.law: world.gold=0
	
#def earthquake
#def epidemic

def famine():
	deck.draw()
	activeRgn=regionList[deck.active.circle]
	actvRgn.tribes=0
	if world.advance.irrigation: actvRgn.cityDown(1)
	else:
		actvRgn.cityDown(2)
		actvRgn.farm=False

#flood
#tsunami
def sandstorm():
	deck.draw()
	actvRgn=regionList[deck.active.circle]
	if actvRgn.desert:
		pass
		#select 2 neighboring regions
		#decimate forests in neighbor region
		#if not world.advance.irrigation:decimate  farm in neighbor
		#create desert in neighbors
	else:
		actvRgn.forest=False
		if not world.advance.irrigation:actvRgn.farm=False
		actvRgn.desert=True
#superstition
	#superstition=draw, shape adder things with value modifier
	#if world.advance.astronomy: superstition+=deck.active
def tribal war():
	if not world.advance.government:
		actvRgn=regionList[deck.active.circle]
		if actvRgn.tribes>0:
			warTribe=actvRgn.tribes
			if not world.advance.senseOfCommunity: warTribe*=2
			# if you have music, select one neighbor with tribes if 
			# possible, if you don't have music - select two if possible
			#reduce neighboring tribes by warTribe
			if world.advance.music: actvRgn.tribes-=1
			else: actvRgn.tribes-=3
#uprisisng	
#volcano
#visitation
#trade