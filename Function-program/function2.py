'''
We are going to see function keyword & variable types of functions...
'''
def keywordArg (name, role):
    print(name, role)
keywordArg( name = "Mayank", role = "manager" )
keywordArg("Amit", "cook")

def variable_fun(*vars):
    for i in vars:
        print(i)
    print("Lenght of vars",len(vars))
    print("Vars value",vars)
variable_fun(1,2,3,55,66,777,88,99)


