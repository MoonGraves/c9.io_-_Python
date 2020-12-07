Lukaisee linkki.txt tiedoston sisäisen tekstin asiat


import re
linkki = input("Linkkin nimi:: ")

def Find(string): 
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string) 
    return url

print("\nUrls:: ", Find(linkki))


choice = input("\nOpen file y/n:: ")

if choice == "y" or "Y":
  with open("linkki.txt") as file:
    for line in file:
      urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
      print(urls)
      
else:
    print("End")
