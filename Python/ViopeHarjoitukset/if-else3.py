luku1 = input("Anna luku:")
luku2 = input("Anna toinen luku:")
luku1 = int(luku1)
luku2 = int(luku2)

if luku1%2==0 and not luku2%2==0:
    print("Toinen luku on parillinen.")
    
if luku2%2==0 and not luku1%2==0:
    print("Toinen luku on parillinen.")
 
if luku1%2==0 and luku2%2==0:
    print("Molemmat luvut ovat parillisia.")
    
if luku1%2==1 and luku2%2==1:
    print("Molemmat luvut ovat parittomia.")
