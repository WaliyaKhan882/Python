var3 = 4
var4 = 7
print("Enter the number")
num = int(input())

if num>var3 and num>var4:
    print("Greater")
elif num>var3 and num<var4:
    print("mid value between var3 and var4")
elif num<var3 and num<var4:
    print("smaller")
elif num==var3:
    print("It is var3")
else:
    print("It is var4")