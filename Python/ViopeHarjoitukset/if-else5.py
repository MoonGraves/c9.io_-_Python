def tulostaja(sana = "Oletustulostus"):
    print(sana)

def main():
    jatka = True
    while jatka:
        sana = input("Anna syöte (Lopeta lopettaa):")
        if sana == "Lopeta":
                jatka = False
                break
        if len(sana) <5:
             tulostaja()
        else:
            tulostaja(sana)


if __name__ == "__main__":
    main()
