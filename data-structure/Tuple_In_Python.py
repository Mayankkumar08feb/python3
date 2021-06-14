'''
DATA Structure
(i)Tuple :- it is inmuteable data set or structure with simple braket.
My_tuple =(1,"Hello",3.4)
My_tup=1,2,3,"asdf"

If u try 

My_tup[0] = 5  ---- it will throught an error
we can do :-

tup3 = my_tuple + my_tup


(ii)List
my_list = [1,"Hello",3.4]

(iii)Dictionary
my_dict = {'name': 'English','pages':120,'price': 23.9 }

(iv) Set
my_set = {1,3,5,120}
'''

tup1 = (123,'hello', 32,'how are you',1)
print (tup1[0])

tup2 = 2,1,3,4,5
tup3 = tup1 + tup2
print (tup3)

print("Lenght of tup2",len(tup2))
if 3 in tup2:
    print("present in tup2")
else:
    print("absent in tup2")

tup4 = (3,4,5,6,7,8)
tup5 = (3,4,5,6,7,8)
tup6 = (3,4,5,6,9,8)

if tup4 == tup5:
    print("t4&t5 is Equal")
else:
    print("t4 & t5 is Not Equal")

if tup4 == tup6:
    print("t4&t6 is Equal")
else:
    print("t4 & t6 is Not Equal")
            
print("Maximum number in tup2 is:", max(tup2))
print("Min Number in tip4 is :" , min(tup4))
print("*******************")
print(tup2[0:2])
print(tup3[:-3])

