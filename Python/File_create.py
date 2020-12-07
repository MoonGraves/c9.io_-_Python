path = input("Give me a file path:: ")
sumx = 0
try:
    with open(path) as f:
        for line in f:
            try:
                n = float(line.rstrip())
                sumx += n
            except ValueError:
                pass
except OSError as err:
    print("Error:" , err)
else:
    print("sum =" , sumx)
