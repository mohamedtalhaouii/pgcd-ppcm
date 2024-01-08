A = int(input("Entrer premier nombre : "))
B = int(input("Entrer Second nombre : "))
r = 1
while r > 0: 
    r = A % B
    A = B
    B = r
if A == 0 and B == 0:
    print("Le PGCD est 0")
else:
    if A == 0:
        print("Le PGCD est :", B)
    else:
        if B == 0:
            print("Le PGCD est :", A)
        if B != 0 and A != 0 :  
          print("Le PGCD est : ", r)
