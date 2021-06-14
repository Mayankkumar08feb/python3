'''
THIS CODE IS FINDING COMMON ITEMS BETWEEN TWO LIST
'''

LIST1 = [1,3,4,5,8,90,21]
LIST2 = [7,8,9,90,21]
LIST1_AS_SET= set(LIST1)
intersection = LIST1_AS_SET.intersection(LIST2)
print(intersection)

intersection_as_list = list(intersection)

print(intersection_as_list)
