#Try Except ERROR Handling---> to skip the error and continue the program
print("Enter the numbers")
a=input()
b=input()
try:
    print("the sum is",int(a)+int(b))
except Exception as e:
    print(e)

print("This is very important line")

#output be like
#bcz e is not an integer but the program will not stop and prints the below line
"""
Enter the numbers
e
4
invalid literal for int() with base 10: 'e' 
This is very important line
"""
