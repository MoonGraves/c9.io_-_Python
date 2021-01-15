import os
from PIL import Image

def image_pdf(image_path):
  
  file_name = str(image_path.split("\\")[-1])

  new_file = os.path.join(image_path.replace(file_name.split(".")[-1], "pdf"))

  image_file = Image.open(image_path)
  parsed = image_file.convert("RGB")
  return parsed.save(new_file)

if __name__ == "__main__":
  image_path = input(r"Drag the exist image here>> ")
  image_pdf(image_path)

#Eli toiminassa siirrät kuin klikkatun kuva missäkin kansiossa ja polussa se sijaitseekaan, jonka jälkeen muuttaa käyttäjän puolesta sen pdf tiedostoiksi.
#Tokihan jos on samassa kansion sisällä ja näppyttää käsin sen kuvan nimi ja tiedoston tyyppi mikäli png/jpg.
