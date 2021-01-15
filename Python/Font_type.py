import os
from pyfiglet import Figlet

def print_teksti(text):
    #Figlet antaa fonttin asetuksia #esim: slant , rand , 5lineoblique ,doh
    
    #Lisää font tyypejä löytyy linkkistä & Figlet:illä on määritty määrä ei vältämättä sovi kaikki ihan sille kirjastolle
    #https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
    text_type = Figlet(font="doh")

    os.system("cls")
    #Asettaa näyttöön sen hienon tekstin design
    os.system('mode con: cols=75 lines=30')
    return str(text_type.renderText(text))

if __name__ == "__main__":
  print(print_teksti("Tanttax"))
