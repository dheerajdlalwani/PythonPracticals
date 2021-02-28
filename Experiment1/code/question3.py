# Question: Program to find leap year

year = int(input("Please enter a year: "))

if year % 400 == 0:
    print(f"{year} is a leap year.\n")
elif year % 100 == 0:
    print(f"{year} is not leap year.\n")
elif year % 4 == 0:
    print(f"{year} is a leap year.\n")
else:
    print(f"{year} is not leap year.\n")
