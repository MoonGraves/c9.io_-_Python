try:
    file = open("file.txt")
    print(file.read())

finally:
    file.close
