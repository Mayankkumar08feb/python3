'''
List can be modified...
mylist=["apple","banana","mango","strawberry",100]

'''
mylist=["apple","banana","mango","strawberry",100]
print(mylist)
print(mylist[3])
mylist[3] = "blueberry"
print(mylist)
print(len(mylist))
#mylist.append("orange")

#print(mylist)
#a = mylist
#print(a)
mylist.append(300)
mylist.extend([500,'Name',400])
print(mylist)

print(mylist.count(100))
#print(a)
'''
if i am making any changes to list "a" same will be repilicate in "mylist"
for example 
'''
#a.append("vegitable")
#print(a)
#print(mylist)
'''
to avoid upper case, need to use copy function for copy a list.
for example
'''

a = mylist.copy()
print(a)
a.append("vegitable1")
print(a)
print(mylist)
print(mylist.index(100))
