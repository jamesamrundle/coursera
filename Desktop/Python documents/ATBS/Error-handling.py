
print ("How many kitties do you have!?")

kittycount = input()

def kCounter(userInput):
	global kittycount
	try:
		if int(kittycount) >= 4:
			print("WOWSERS, that is A LOT of kitties")
		elif int(kittycount) == 0:
				print("You should get a kitty!")
		elif int(kittycount) < 0:
			print("Come on! you cant have negative kitties!")
			print("Please enter a POSITIVE number :)")
			kittycount = input()
			kCounter(kittycount)
		else:
			print("Step up the kitty game bruh")
	except (ValueError):
		print("Please enter a numeral")
		kittycount = input()
		kCounter(kittycount)
		
kCounter(kittycount)
