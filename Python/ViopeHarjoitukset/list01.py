with open("sanoja.txt", "r") as file:
	lista = [line.strip() for line in file]
print("Sanat laitettuna aakkosjärjestykseen:")
lista.sort()
for a in lista:
	print(a)
