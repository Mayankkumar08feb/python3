x = int(input(" Enter the 1st Number "))
y = int(input(" Enter the 2nd Number "))
print(" Please select the opretion which you want to perform ")
print(" 1 for Addition")
print(" 2 for Substraction")
print(" 3 for multiple")
print(" 4 for Division")
a = int(input("Enter you choice = "))
if a == 1:
    print(" You have selected Addition ")
    z=(x+y)
    print(" the sum of two numbers is =",z)
elif a == 2:
    print(" You have selected substraction")
    z=(x-y)
    print(" the substraction of two numbers is =",z)
elif a == 3:
    print(" You have selected multiplication")
    z=(x*y)
    print(" the multiplication  of two numbers is =",z)
elif a == 4:
    print(" You have selected Division")
    z=(x/y)
    print(" the division of two numbers is =",z)


