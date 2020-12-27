def openf():
    fname=input("Anna tiedoston nimi: ")
    try:
        handler = open(fname, 'r')
        content = handler.read()
        handler.close()
        return content
    except IOError:
        return False

def conversion(fcontent):
    try:
        fcontent=int(fcontent)
        return fcontent
    except Exception:
        return False

def main():
    result=openf()
    if result == False:
        print("Virheellinen tiedostonnimi")
    elif conversion(result) == False:
        print("Tiedoston sisätlö virheellinen.")
    else:
        print("Saatin tulos", 1000/conversion(result))

if __name__=="__main__":
    main()
