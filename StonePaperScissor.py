import random
lis = ["Stone", "Paper", "Scissor"]

print("Enter 1 for Stone")
print("Enter 2 for Paper")
print("Enter 3 for Scissor")
print("Enter 0 for Exit\n")

while True:    

    a = int(input("Enter your choice : "))

    if a > 0 and a < 4:
        if a == 1:
            print("Your choice is : Stone")
        elif a == 2:
            print("Your choice is : Paper")
        else:
            print("Your choice is : Scissor")

        com_choice = random.choice(lis)
        print("Computer's Choice is : ",com_choice)
        
        if a == 1:
            if com_choice == lis[0]:
                print("Tie")
            elif com_choice == lis[1]:
                print("Computer Won")
            else :
                print("You Won")

        elif a == 2:
            if com_choice == lis[0]:
                print("You Won")
            elif com_choice == lis[1]:
                print("Tie")
            else :
                print("Computer Won")
        
        else:
            if com_choice == lis[0]:
                print("Computer Won")
            elif com_choice == lis[1]:
                print("You Won")
            else :
                print("Tie")

    elif a == 0:
        print("Exiting.....")
        print("EXIT")
        break

    else :
        print("Enter cottect choice")
