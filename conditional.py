print("Is the Student is a Freshmen? 1. Yes 2. No")
a = int(input("Enter Here: "))

print("Is the Student eating in Dining hall ? 1. Yes 2. No")
b = int(input("Enter Here: "))

def Prob(a,b):
    if a == 1:
        std = 0.3
        if b == 1:
            dining = 0.75
        else:
            dining = 0.25
    elif a== 2:
        std = 0.7
        if b == 1:
            dining = 0.6
        else:
            dining = 0.4


    result = std**dining
    print(str(result*100)+" %")


Prob(a,b)