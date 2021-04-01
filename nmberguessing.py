import numpy as np

no = np.random.randint(1,100)
print("Enter number between 1 to 100")
print("if you corect gussing the no. you mark between 100 ")
print("you will get 10 chance to guess the correct number:")
point = 100
chance = 10
while(True):
    num = int(input("Enter the Gussing number:="))
    if num < no:
        chance = chance - 1
        print("Number must be gretter than a number: your chance left as",chance)
        print("\n")
        point = point - 10
        if point==0:
            print("You Lost, Better Luck Next Time !")
            break

    elif num > no:
        chance = chance - 1
        print("Number must be less than a number : your chance left is:",chance)
        print("\n")
        point = point - 10
        if point == 0:
            print("You Lost, Better Luck Next Time !")
            break
    else:
        print(" your correct guessing no is :",no)
        print(" your score is ",point)
        break




