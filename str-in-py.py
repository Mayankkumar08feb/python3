#String Operators in python

a = "Hello, World"
#    01234567891011  -----position of strg
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
b = input("Enter some strg here ")
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])

print(b[2:8])    #----------here range 

print(a+b)      #--------- Adding to string

print(a[1] + b[2])   #------Adding two charctor 

#multiple d string

print(a*2)

########################################String Functions:

print(a.lower())
print(a.upper())
print(a.replace('H','M'))

c ="str no,date,time,name,125"
d = c.split(',')
print(d)
f = int(d[4])
print(f)
print(f*100)

