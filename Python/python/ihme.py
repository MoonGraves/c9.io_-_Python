from gtts import gTTS
import os

#myText = "moikka! Mitä kuuluu"
f=open("ekaLuento.txt")
x=f.read()

language = 'fi'

#output = gTTS(text=myText, lang=language, slow=False)
output = gTTS(text=x, lang=language, slow=False)

output.save("output.mp3")
output.save("test.wav")

os.system("start output.mp3")
