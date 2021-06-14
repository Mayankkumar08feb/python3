a = 1
while a <= 3:
    b = int(input("Enter no:"))
    if b == 0:
        print("Exiting loop with brk command,'else' is notexecuted")
        break
    a+=1

else:
    print("loop exited without executing break command")

    
    
