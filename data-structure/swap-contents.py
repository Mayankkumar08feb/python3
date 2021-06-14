print("Hello world")
'''
This Program is for swaping contens of a list
'''
a_list = ["a","b","c","d"]
index1 = a_list.index("a")
print(index1)
index2 = a_list.index("c")
print(index2)
print(a_list[index1])
a_list[index1], a_list[index2] = a_list[index2], a_list[index1]
print(a_list)

# second method

def swapPositions(a_lists, pos1, pos2):
     
    a_lists[pos1], a_lists[pos2] = a_lists[pos2], a_lists[pos1]
    return a_lists
 
# Driver function
#a_lists = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(a_list, pos1-1, pos2-1))
