n=int(input("enter n value \n "))
if (n==0):
    print("Zero")

if (n>0):
    print("Positive")
else:
    print("negtive")

#Largest among three numbers
a = int(input("Enter value of a= "))
b = int(input("Enter value of b= "))
c = int(input("Enter value of c= "))
if (a>b):
    if (a>c):
        print("a is large")
    else:
        print("c is large")
elif (b>c):
    print("b is large")
else:
    print("c is large")
