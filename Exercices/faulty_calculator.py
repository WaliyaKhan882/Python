#paper calculations that should be made faulty
"""
45*3=555
56+9=77
56/6=4
"""
print("Please enter num1")
num1=int(input())
print("Please Enter num2")
num2=int(input())
print("Enter the operator sign")
operation=input()
if (num1==56 or num2==56) and (operation=="+"):
    print("77")
elif (num1==56 or num2==56) and (operation=="/"):
    print("4")
elif (num1== 45 or num2==45) and (operation=="*"):
    print("555")
elif operation == "+":
    print("Sum is", num1 + num2)
elif operation == "-":
    print("Difference is", num1 - num2)
elif operation == "*":
    print("Multiplication is", num1 * num2)
elif operation == "/":
    print("Division is", num1 / num2)
else:
    print("invalid calculation")



