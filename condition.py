a = int(input(" Enter the value of a = "))
b = int(input(" Enter the value of b ="))
if a>b:
    print(" i am printing a > b ")
    print("a is greater than b")
print("i am on main programe")
print("code exit")

###############################################
#Useing if and else condition 
###############################################

if a>b:
    print(" A is greater than B")
else:
    print(" b is greater than A")
print("code exit")

###############################################
#using multiple condition under condition with IF
###############################################

if a>b:
    print(" A is larger")
    if a > 100:
        print(" A is greater than 100")
        if a > 1000:
            print(" A is greater than 1000")
        print("A is only greater than")

###################################################
#using multiple condition under condition with IF & Else
###############################################
if a>b:
    print(" A is larger")
    if a > 100:
        print(" A is greater than 100")
    else:
        print("A is less than 100")
        if a > 1000:
            print(" A is greater than 1000")
        else:
            print("A is only grater than ant not 1000")
    print("Moving out from condition")
print(" i m in main program")

###################################################
#using multiple condition under condition with And & or operator
###############################################

if a>b and a>100 and a >1000:
    print("A is greater than B, 100 & 1000")
else:
    print("All 3condition is not up to mark, pls contact sysadmin") 
if b>a or b >100 or b>50:
    print(" B is having some value")


###################################################
#using multiple condition under condition with IF & Else
###############################################

