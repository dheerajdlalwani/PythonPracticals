n = int(input("Enter the number of fibonacci terms you want: "))

a, b = 0, 1
for i in range(n):
    print(a, end=", ")
    a, b = b, a + b

print("\n\n\n")