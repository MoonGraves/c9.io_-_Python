try: 
  file = open("file.txt")
  print(file.read())
  #print(1 / 0)

finally:
  file.close
