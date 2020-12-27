def pena(sana):
    mitta=len(sana)
    mitta=int(mitta)
    return mitta
    
def main():
    jatka = True
    while jatka:
        sana = input("Anna syöte (Lopeta lopettaa): ")
        if sana == "Lopeta":
                jatka = False
                break
        else:
            pena(sana)
        pituus=pena(sana)

        if pituus==0:
            print("Et antanut syötettä")
        else:    
            print("Antamasi syöte oli", pituus,"merkkiä pitkä.")


if __name__ == "__main__":
    main()
