Tässä tapahtuu siten, että serveri avaa webbisivuston, mutta tämä sivusto ei varsinaisesti mene index.html mukaan <br>
Toiminnaltaan toimii vain päivietty sivu F5, tai useampi client käy siellä ja näkee sen html koodi pätkän eli avoimelähdekoodin miten ne on kirjoitettu <br>
Varsinaisesti toimii vain perus yksikköt ja tekstit eli paksuus tai italic, ei kuvien lisäämistä, muu linkitys tai videon toistoa. <br>


Localhost porttia voidaan muuttaa satunnaisesti, mutta yleisin käyttö porttit on 8080, 8000 tai 9000 tässä testauksessa. <br>
Eli käynnisteässä pitää olla serveri ensimmäisenä tapahtuu, että hyväksyy porttin ja localhostin <br>
kun sivusto päivittyy tai F5 cmd näkyy GET / HTTP/1.1 , koska se on itsensä kun päivittyy sivusto.

Alempi kuvaa parhaiten, keskellä on serveri & oikea client2 ja vasen client1
Kaikilla toimivat localhost:8080 tai loopback: 127.0.0.1:8080, paitsi client1 ja 2:lla pitää olla lopussa osoittava, että tunnistaa sen kuka on kukakin

###<b> CMD </b> ### <b> Serveri </b> ###
>> python Server.py
>>Access http://localhost:9000
>>GET / HTTP/1.1
>>
>>GET / HTTP/1.1
>>GET / HTTP/1.1
>>
![Alt text](images/img.JPG?raw=true "Title")
<br> 
![Alt text](images/img2.jpg?raw=true "None")
