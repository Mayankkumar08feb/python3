'''
Function programing
'''
print(" Vales you've entered are wrong, please re-enter")
'''
if you are try to print above message multiple times, 
need to write print statment multiple times...but we can avoid it by using function 
'''
def wrong_input():
    print(" Vales you've entered are wrong, please re-enter")

a = int(input("Enter value"))
if a == 0:
    wrong_input()
else:
    if a > 0 and a < 10:
        wrong_input()
    else:
        print(a)
def Addition_function(p,q):
    r = p + q
    print("Addition of {0} + {1} = {2}".format(p,q,r))
def add(p,q):
    r = p + q
    return r

def add_mul(p,q):
    add = p + q
    mul = p*q
    return add, mul


b = int(input("Enter the 1st Number"))
c = int(input("Enter the 2nd Number"))
Addition_function(b,c)
c = add(b,c)
print("sume of second method",c)

Addition1, Multiple1 = add_mul(b,c)
print("Addition of num", Addition1)
print("Multiplication of Num", Multiple1)

'''
 Golbal variable

'''
global temp
temp = 45

def print_temp():
    global temp
    temp = 50
    print(temp)

def inc_temp():
    global temp
    temp = temp + 5
    print(temp)

print("Actual value of temp",temp)
print_temp()
inc_temp()
inc_temp()

global result

def Addition2(h,k):
    global result
    result = h + k

def Multiple2(h,k):
    global result
    result = h * k

u = int(input("enter global vale"))
v = int(input("enter global vale"))

Addition2(u,v)
print("Addition2 is", result)

Multiple2(u,v)
print("Multipl2 is ", result)

def welcome(name, msg = "Hello"):
    print(msg, name)

welcome("Mayank")