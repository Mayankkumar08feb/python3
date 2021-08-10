print("Please select code \n 1 for add \n 2 for sub \n 3 for div")
a = int(input("Enter d code")

def wrong_input():
    print(" Vales you've entered are wrong, please re-enter")

#a = int(input("Enter value"))
if a == 0:
    wrong_input()
else:
    if a > 0 and a < 10:
        wrong_input()
    else:
        print(a)



def Addition():
    z = (x+y)
    retrun z
    print(z)


 x = int(input("enter 1 st num"))
 y = int(input("enter 2nd num"))
 
 if a == 1:
     Addition(x,y)
