a= int(input("Enter the Number for a = "))
rev = 0
while a > 0:
    rem = a % 10
    rev = (rev*10) + rem
    a = a // 10
print(" Your enterted Number is = ", rev)

