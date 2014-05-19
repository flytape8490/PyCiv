class deck:
	master=[ # number,circle,square,hex,gold,friendly,events
	#should set up each event as its own object to make the math for certain event functions easier
		card(1,1,7,6,0,True,{
			1:['tribalWar',0,0,0],
			2:['epidemic',0,0,1],
			3:['famine',0,0,0],
			4:['uprising',0,0,0],
			6:['visitationFloren',0,0,2],
			8:['corruption',0,0,1]}),
		card(2,2,4,7,2,False,{
			1:['volcano',0,0,0],
			2:['tribalWar',0,0,0],
			3:['corruption',1,0,0],
			5:['civilWar',0,0,1],
			6:['visitationGilda',1,1,1],
			7:['earthquake',2,1,0],
			8:['visitationAtlantea',0,0,3]})
		card(3,3,5,8,1,True,{
			2:['bandits',0,1,1],
			4:['epidemic',1,1,1],
			5:['visitationAtlantea',0,3,0]
			7:['visitationGilda',1,1,1],
			8:['civilWar',0,0,1]})
		card(4,4,7,7,2,False,{
			1:['earthquake',1,0,0],
			3:['visitationFloren',0,0,2],
			4:['superstition',1,0,0],
			6:['famine',0,0,0],
			7:['uprising',0,0,0],
			8:['visitationNordic',0,0,0]})
		card(5,5,3,9,1,True,{
			3:['epidemic',0,0,1],
			4:['visitationGilda',0,0,2],
			5:['corruption',0,1,0],
			6:['tribalWar',0,0,0],
			7:['corruption',0,1,0],
			8:['flood',0,2,0]})
		card(6,6,4,6,0,True,{
			1:['flood',1,0,0],
			3:['visitationAtlantea',0,0,2],
			4:['civilWar',0,0,1],
			5:['sandstorm',0,0,0],
			6:['epidemic',1,0,1]})
		# ...
		]
	discard=[]
	def reset():
		deck.deck=deck.master
		shuffle(deck.deck)
		# deck.discard=[]
	def draw(update=True):
		# add a try to push end-of-era
		deck.discard+=[deck.deck.pop(0)]
		if update: deck.active=deck.discard[-1]
		