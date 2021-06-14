'''
Opening & closing files in Python
Writing Data to a file
Creating a txt & csv file in python
Mostly use for log files 
"w" == file written
"r" == file read 
"a" == append the data
'''
a = open('log.txt','w')
a.write("textto be written, add some contain  \n")
a.flush()
a.close()
print("file written")





a = open('log.txt','a')
a.write("text toappended to file written, add some contain to old file \n")
a.flush()
a.close()

b = open('log.txt','r')
file_txt = b.read()
b.close()
print("*******************")
print(file_txt)






c= open('log.csv','a')
c.write("2,88,99,808 \n")
c.write("44,66,77,7 \n")
c.write("1,3, 6 ,8 \n")
c.write("1,2,3,4 \n")
c.write("9,0,8,7 \n")
c.flush()
c.close()

d = open('log.csv','r')
file_txt = d.read()
d.close()
