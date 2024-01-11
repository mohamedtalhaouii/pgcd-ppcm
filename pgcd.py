#find the greatest common divisor
A = int(input("Enter first number : "))
B = int(input("Enter Second number : "))

r = 1
while r > 0: 
    r = A % B
    A = B
    B = r
if A == 0 and B == 0:
    print("Greatest Common Divisor is 0")
elif A == 0:
        print("Greatest Common Divisor is :", B)
elif B == 0:
    print("Greatest Common Divisor is :", A)
elif B != 0 and A != 0 :  
    print("Greatest Common Divisor is : ", r)
