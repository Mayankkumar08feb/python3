'''
Exceptions:
i) IO Error:- if the file cannot be opened or (called as Module Error)

eg:- if runing program like mention below, you will get IO or Module error.
    
    import Mayankkumar
    -----This will throuh Error because there is no such module called as Mayankkumar 


ii) Import Error:-
        If Python cannot find the the module

iii) Value Error: Raised When a built-in operation or
        function receives an argument that has the right type
        but an inappropriate value.
eg:-
    print("Hello worl")
    sleep(-859) ------ This will throuh Error, Wan't accept -ve value

iv) KeyboardInterrupt:-
        Raised When the user hits the interrupt key(Normally control-c or Delete)

eg:- Consider below program

    a = 0
    while true:
        print("Value of a is ",a)
        a = a + 1
        sleep(2)

Above programe is in infinite loop and to stop it, Need to hit control-c..
correct program for above case to avaiod infinite loop. Try-except:

a = 0
try:
    while true:
        print("Value of a is ",a)
        a = a + 1
        sleep(2)
except keyboardInterrupt:
    print("I am exiting from Program")



v) EOF Error:-
        Raised when one of the built-in functions(input() or raw_input()) hits an end-of-file condition(EOF) without reading any data.
vi) Zero Division Error: Division by zero

################################################
Let's do some hands-on "try"
syntax will be:
try:
    print(X)
    -----
    -----
    task(n)
except keyboardInterrupt:
    print(Y)
    task(n)
'''
import time
a = 0
myfile = open('log.txt','w')
try:
    while a < 10:
        print(a)
        myfile.write(str(a))
        myfile.write("\n")
        time.sleep(1)
        a = a + 1
    myfile.close()
except KeyboardInterrupt:
    ''' we can give or mention "except:" --This will accept all kind of interruption(This not recommandated) '''
    myfile.close()
    '''--- If you missed to mention close then a blank file will be store '''
    
    print("\n", "exiting....")



