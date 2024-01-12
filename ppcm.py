#Find The Lowest Common Multiple
A = int(input("Enter First Number : "))
B = int(input("Enter Second Number : "))

r = 1
ppcm = 1
C = (A * B)
#Compariason between A and B
if A > B :
    while r > 0: 
        r = A % B
        if r != 0:
          A = B
          B = r
          ppcm = C // r
    print(" The Lowest Common Multiple is : " , ppcm)
elif A < B :
    while r > 0: 
        r = B % A
        if r != 0:
           B = A
           A = r
           ppcm = C // r
    print(" The Lowest Common Multiple is : " , ppcm)