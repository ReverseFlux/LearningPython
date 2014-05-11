people = 30
cars = 40
buses = 15


if people > cars:
	print "We should take the car"
elif cars <people:
	print "we should not take the car"
else:
	print "We can't decide"

if buses >cars:
	print "That's too many buses"
elif buses < cars:
	print "maybe we could take the buses."
else:
	print "We still can' decide"
	
if people > buses:
	print "alright, let's just take the buses"
else:
	print "fine, let's stay home then"