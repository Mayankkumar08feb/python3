try:
    if (3 + 1 - 5) > 0:
        a = 3
        a.append("hello")  #throws Attribute Error
    else:
        print("Heelo" + 4) #throws typeError
except(AttributeError, TypeError) as e:
    print("Error occurred:",e)
finally:
    print("Finally block will always execute")
