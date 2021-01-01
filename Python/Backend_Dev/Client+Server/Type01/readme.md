Käyttäjä voi käyttää useita sovelluksia esim. <b> VsCode </b> tai muu kaltaista on ok, koska nykyään useissa ladatuissa sovelluksissa on terminal eli komentorivi kuin cmd tyyppinen.  
tässä on käytetty client - :ssa tarvittavan ip-osoite ja portti protokolla, koska se yhdistää kuin tyyppillisen methodi/parametrin funktion

saman aikaisesti serveri kuuntelee tai lukaisee tulevien ip-osoiteen tai muun tekijänssä, että client voi olla useita käytettäviä tekijöitä mm. cmd tai oman sovelluksen Vscoden sisäisen terminal cmd. <b>
Ensinnäkin käynnistä serveri, vasta sen jälkeen käynnistät useamman client.py. Tässä tulostuu siten, että näkee tämän ip-osoitten ja käyttäjän käytetävän työaklun eli läppäri tai pöytäkone, ja sisältyen pieni id-tunnus. id tunnus muuttuu kokoajan, paitsi mikäli on yksi ja sama henkilö. <br>
tässä esityksesä ip-osoite on vale, kannattaa käyttää oman tietokoneen varsinaisen ip-osoite minkä voit tarkistaa komentoriviltä syötät - ipconfig (IPV4 address). <br>

Tässä esityksessä client voi syöttää haluamansa viestin, koska tässä automaatisesti luotu viesti, jos käyttäjä näppytää näppäimistöstä vain "Enter" niin se automaatinen viesti lähtee eteenpäin. <br>
Myös tähän vaikuttaa se def send (funktio) + ja oletus viestit eli print <br>
Kunnes päättyy !DISCONNECT, voidaan käynnistää useita client.py, mutta ip-osoitteen perään se id tunnus muuttuu kuitenkin ja serveri voi pyöriä niin kauan, kunnes sammutettaan se terminal


*output from server* <br>
C:\Users\NAME->C:/Python/Python36/Python.exe c:/Python/Python36/ClientServer/Server.py <br>
[STARTING] Server is starting... <br>
[LISTENING] Server is connecting to.. 127.0.0.1 <br>
[NEW CONNECTION] ('127.0.0.1', 52287) connected. <br>
[ACTIVE CONNECTIONS] 1 <br>
[('127.0.0.1', 52287)] From client <br>
[('127.0.0.1', 52287)] Tänään on : Friday , 2021 , 19:34:28 <br>
[('127.0.0.1', 52287)] qwer <br>
[('127.0.0.1', 52287)] Connection end <br>
[('127.0.0.1', 52287)] !DISCONNECT <br>


*output from client* <br>
C:\Python\Python36\ClientServer>python Client.py <br>
Welcome today is: 01 Jan 2021 <br>
SMS received <br>
SMS received <br>
message here:: <br>
qwer <br>
SMS received <br>
<br>
SMS received <br>
SMS received <br>
<br>
C:\Python\Python36\ClientServer> <br>
