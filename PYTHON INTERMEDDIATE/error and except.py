#chap 10 errors and exceptions (try,except, else, finally)
try: #catches eroors only
    a= 6/2
    b= a+10 
#except runs if smth in tries go wrong
except ZeroDivisionError as e:
    print("caught the error": e)
except TypeError as e:
    print("caight in type error": e)

#else runs when try works perfectly with no errors
else:
    print("everything is good")

#finally works no matter what, with error without error
finally:
    print("cleaning up")

#CUSTOM ERROR AND PASS

class CustomErrorClass(Exception):
    pass #we cant leave any body of class empty so we ened this





    