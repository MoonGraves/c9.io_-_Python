tiedosto = open("merkkijonoja.txt", "r")

for salasana in tiedosto:
	salasana = salasana.rstrip('\n')
	if salasana.isalnum() == False:
		print (salasana.rstrip(), "sisältää virheellisiä merkkejä.")

	else:
		print(salasana.rstrip(), "kelpaa salasanaksi.")

tiedosto.close()
