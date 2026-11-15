#decorators are like gift wrapping, main fucn is the gift and u make extra behaviour aroudn it, like printing start and end

def mydecorator(func): #defines a decorator func and takes another fucn as input 
    def wrapper(): # another func that holds the extra wrapped behaviour
        print("---BEFORE---")
        func()
        print("~~~AFTER~~~")
        return wrapper

#we use the @ to automatically wrap the func everytime its called
@mydecorator
def say_hello():
    print("Hello!") #adding decorators to this hello fucntion

