while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta")
    valinta=int(input("Mitä haluat tehdä?: "))
    if valinta == 1:
        kahva = open("muistio.txt","r")
        sisalto = kahva.readline()
        print(sisalto)
        kahva.close()
    elif valinta == 2:
        kahva = open("muistio.txt","a")
        lisays = input("Kirjoita uusi merkintä: ")
        lisays = lisays +"\n"
        kahva.write(lisays)
        kahva.close()
    elif valinta == 3:
        kahva = open("muistio.txt","w")
        print("Muistio tyhjennetty.")
        kahva.close()
    elif valinta == 4:
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")
