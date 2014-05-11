print "You enter a dark room with two doors. Do you go through door #1, door #2 or door #3?"

door = raw_input ("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. what do you do?"
	print "1. take the cake."
	print "2. scream at the bear."
		
	bear = raw_input ("> ")
		
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Goo job!"
	else:
		print "Well, doing %s is probably better. Bear runs away" % bear
		
elif door == "2":
	print "You stare into the endless abyss at Chtulu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
elif door == "3":
	print "You find the place you have ever desired to be in, what do you do?"
	print "1.You go back to the place you came from through the door in front of you. "
	print "2.You decide to stay there for the rest of your days. "
	decision_3 = raw_input("> ")
	if decision_3 == "1":
		print "The door tricked you and you get trasported in an ethernal abyss. Good job!"
	if decision_3 == "2"
		print "All that perfection annoys you and you kill your self. Good job!"
else:
	print "You stumble around anf fall on a knife and die. good job!"