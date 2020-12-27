jatkuu = True

while jatkuu:
  syote = input("Kirjoita jotain: ")

  if syote == "lopeta":
    print("Lopetit ohjelman.")
    jatkuu = False
  else:
      print(syote)
