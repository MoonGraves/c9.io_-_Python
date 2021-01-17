import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate

#Skannauksessa tulostuu maa ja teleyhtiön nimi & jossain numeroissa ei vältämättä pysty skannaa ihan kaikkia maita
def number_scanner(phone_number):
  number = phonenumbers.parse(phone_number)
  description = geocoder.description_for_number(number, "en")
  supplier = carrier.name_for_number(number, "en")

  info = [["Country", "Supplier"],
          [description, supplier]]

  #Taulukkon muodostaminen & tablefmt: plain, simple, grid, github, rst
  data = str(tabulate(info, headers="firstrow", tablefmt="rst"))
  return data

if __name__ == "__main__":
  number = input("Phone number is:: ")
  print(number_scanner(number))

###############
###Output::
#Phone number is:: +4588888888
#| Country   | Supplier   |
#|-----------|------------|
#| Denmark   | telenor    |
#
