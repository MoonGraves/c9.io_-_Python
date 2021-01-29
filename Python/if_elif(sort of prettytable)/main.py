#hieno tietokanta editointi 

#pip install prettytable
import operator
from prettytable import PrettyTable
from prettytable import from_csv

#column names while initalizing the Table
myTable1 = PrettyTable(["names", "class", "Grade", "Percentage", "date"])

myTable1.add_row(["Amy", "A-1", "A", "94.1 %", "12-3-2017"])
myTable1.add_row(["Jacky", "B-2", "B+", "93.4", "09-04-2019"])
myTable1.add_row(["Leon", "A-1", "A-", "95.2", "20-12-2019"])
myTable1.add_row(["Sandy", "B-2", "B", "94.3", "04-07-2018"])
myTable1.add_row(["Ben", "B-2", "C", "93.9", "21-01-2018"])
myTable1.add_row(["Windy", "A-1", "B", "94.6", "29-05-2017"])

print(myTable1)

print("###############")
answer = input("Valitse joku toiminta näistä 1-6 väliltä: \n")


if answer in '1':
   print(myTable1.get_string(sort_key=operator.itemgetter(4, 0), sortby="Grade"))
elif answer in '2':
    print(myTable1.get_string(sortby="Percentage"))

elif answer in '3':
    print(myTable1.get_string(fields=["Grade", "names"]))

#pieni toiminta poistaa vanhan database jonkun riviltä kokonaan, lukaisee vain luvut
elif answer in '4':
    theRow = int(input("Mikä rivit poistettaan?: "))

    myTable1.del_row(theRow)
    print(myTable1)

#array listasta otettaan vain 1-4, koska luvut menee 0,1,2,3,4 ja jne..
elif answer in '5':
    print(myTable1.get_string(start=1, end=4))

#open the exist file, and print it out
elif answer in '6':    
    with open("data.csv", "r") as fp: 
      x_fileCSV = from_csv(fp)

    # print(x_fileCSV)
      print(x_fileCSV.get_string(sortby='Population', sort_key=lambda row: int(row[0])))

else:
    print ('Default answer')
