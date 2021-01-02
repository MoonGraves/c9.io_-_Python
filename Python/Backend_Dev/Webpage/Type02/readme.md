Tässä python file tiedostossa, voidaan käynnistää joko tavallisen cmd:n kommennon avulla tai perus sovelluksen sisäisen alhaalla komento rivin tyyppin

-CMD:: & syötät välilehteen tällaisen kuin: localhost:8080 , koska http.Server(pälä, 8080) on määritetty tällaisena
Python main.py<br>
127.0.0.1 - - [02/Jan/2021 12:39:17] "GET / HTTP/1.1" 200 - <br>
127.0.0.1 - - [02/Jan/2021 12:39:18] "GET /css/style.css HTTP/1.1" 404 - <br>
127.0.0.1 - - [02/Jan/2021 12:39:18] "GET /Sieppaakari.PNG HTTP/1.1" 404 - <br>
127.0.0.1 - - [02/Jan/2021 12:39:25] "GET /index.html HTTP/1.1" 200 - <br>
127.0.0.1 - - [02/Jan/2021 12:39:25] "GET /css/style.css HTTP/1.1" 404 - <br>

Oletuksena se lukaisee ensimmäisenä index.html sivuston ensimmäisenä, jos on muita sivustoja kuin tämä voidaan laittaa: localhost:8080/index2.html <br>
JOS ei ole sellaisia sivustoja olemassa sitten pelkä lukee "File not found".<br>

Onko olemassa muita sivustoja html tyyppejä cmd:n tulee aina päivitys ja pientä huomiota jos on tullut error 404 esim. kuvissa tai sivun tavallinen päivitys F5 <br>
Ja ohjelman lopettaminen riittää cmd kommentoon syötät kerran ctrl + c ja päivität sivuston kerran, niin se lopettaa sen ohjelman samantien <br>
