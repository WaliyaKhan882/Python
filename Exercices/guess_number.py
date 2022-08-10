print("Welcome to the guess number game")
# let the number is 7
i=0
while(i<10):
    print("Enter the number")
    a=int(input())
    i=i+1
    if i<10:
        if a>7:
            print("Please try a smaller number")
        elif a<7:
            print("Please try a bigger number")
        elif a==7:
            print("You won")
            print("You used",i,"guesses out of 10")
            break
    elif i==10:
        print("You can't use more guesses, try again")
        break