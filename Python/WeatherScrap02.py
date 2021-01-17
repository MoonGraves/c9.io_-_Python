import requests
from bs4 import BeautifulSoup

class Temperature(object):
  def __init__(self, place):
    self.place = place

  def __repr__(self):
    temperature = self.weather()

    return str(f"it's a currently {temperature} in a {self.place}")

    #return str(f"it's a currently %s in a {self.place} " %(temperature))

    #return str(f"it's a currently {temperature} in a {self.place}")

  def weather(self):
    url = f"https://www.google.com/search?&q=weather in {self.place}"
    req = requests.get(url)
    scrape = BeautifulSoup(req.text, "html.parser")
    temperature = scrape.find("div", class_="BNeawe").text
    return temperature

if __name__ == "__main__":

  print(Temperature('Finland'))
 
#############################
####Toiminassa tämä saattaa antaa asteikkona Fahrenheit asteikkon eli *F & tai celius *C
##Toki tästä itse voidaan määrittää se Celsius
###output::
#it's a currently 9°F in a Finland
#
#
#
