# Question: Find all armstrong numbers between 1 and 1000

def isArmstrong(num):
    num = str(num)
    l = len(num)
    x = 0
    for digit in num:
        x += int(digit) ** l
    if(x == int(num)):
        return True

    return False


for i in range(1, 1001):
    if isArmstrong(i):
        print(f"{i} is an armstrong number.")