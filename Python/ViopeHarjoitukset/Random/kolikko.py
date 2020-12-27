import random

heitto = 0
kruunu = 1
klaava = 0
print("Heitetään kolikkoa viidesti:")

while heitto <=4:
	coin = random.randint(1,2)
	if coin == 1:
		print("Kruuna!")
		kruunu +=1
		heitto +=1
	elif coin == 0:
		print("Klaava!")
		klaava +=1
		heitto +=1
