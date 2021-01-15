while True:
  try:
    value = int(input("Anna joku luku 0 ja 15 väliltä: "))
  
  except ValueError:
      print("Sun täytyy antaa joku luku 0 ja 15 väliltä")
  except KeyboardInterrupt:
      print("Ctrl+C")

    
  else:
    if value > 0 and value <= 15:
      print(f"Annoit: {value} ")
      break

    else:
      print("Antamasi merkki/luku on: "")
      break
