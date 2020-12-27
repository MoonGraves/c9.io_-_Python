import random
def main():
    voitot=0
    tasapelit=0
    kierrosta=0
    jatkuu = True
    while jatkuu:
        valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
        if valinta=="Lopeta":
            jatkuu=False
        else:    
            arvottu = random.randint(1,3)
            if arvottu==1:
                arvottu="Jalka"
            elif arvottu==2:
                arvottu="Ydinase"
            elif arvottu==3:
                arvottu="Torakka"
            print("Sinä valitsit:",valinta,"\ntietokone valitsi:",arvottu)    
            if valinta==arvottu:
                print("Tasapeli!")
                tasapelit+=1
            elif valinta=="Jalka" and arvottu=="Torakka":
                print("Voitit!")
                voitot+=1
            elif valinta=="Torakka" and arvottu=="Ydinase":
                print("Voitit!")
                voitot+=1
            elif valinta=="Ydinase" and arvottu=="Jalka":
                print("Voitit!")
                voitot+=1
            else:
                print("Hävisit!")
            kierrosta+=1
    print("Pelasit",kierrosta,"kierrosta, joista voitit",voitot,"ja pelasit tasan",tasapelit,"peliä.")
if __name__ == "__main__":
    main()
