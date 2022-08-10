#built-in functions
a=4
b=5
c= sum((a,b)) # can get more info about builtin py function by clicking on func name holding ctrl button
print(c)
#User-Defined Functions
def average(a,b):
    #creating a doc string
    """"This is a func that calculates average of two numbers"""
    z=(a+b)/2
    return z
print(average(4,2).__doc__) #this will give the user imp info about the function
v = average(4,2)
print(v)
