
with open('Admin.txt') as tiedosto:
    with open('results.txt', 'w') as outfile:

        for line in tiedosto:
            try:
                total = 0
                num = int(line)
                total += num
                print(num, file=outfile)
            except ValueError:
                print(
                    "'{}' is not a number".format(line.rstrip())
                )

print("Summa:", +total)
