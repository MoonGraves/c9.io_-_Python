eka = input("Anna ensimmäinen luku:")
toka = input("Anna toinen luku:")

eka = int(eka)
toka = int(toka)

print("(1) +");
print("(2) -");
print("(3) *");
print("(4) /");

valinta = input("Tee valinta (1-4):")
valinta = int(valinta)

if valinta == 1:
  print("tulos on:", eka+toka)

elif valinta == 2:
  print("tulos on:", eka-toka)

elif valinta  == 3:
  print("tulos on:", eka*toka)

elif valinta == 4:
  print("tulos on:", eka/toka)

else:
  print("Valintaa ei tunnistettu.")

  
