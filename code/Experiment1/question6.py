# Question: Print the following patterns:

# 1]
# A
# B B
# C C C
# D D D D
# E E E E E


n = int(input("Enter a number between 1 and 26: "))
while(1 > n or n > 26):
    n = int(input("Please enter a number between 1 and 26: "))

char = 'A'
for num in range(1, n + 1):
    print(f"{char} " * num)
    char = chr(ord(char) + 1)


# 2]

# * * * * *
#   * * * *
#     * * *
#       * *
#         *


n = int(input("\nEnter a number: "))
for num in range(n):
    print("  " * (num), "* " * (n - num))


# 3]

#              1
#            1 2 1
#          1 2 3 2 1
#        1 2 3 4 3 2 1
#      1 2 3 4 5 4 3 2 1


n = int(input("\nEnter a number: "))

for num in range(1, n + 1):
    print("  " * (n - num), end="")
    for i in range(1, num + 1):
        print(i, end=" ")
    for i in range(num - 1, 0, -1):
        print(i, end=" ")
    print()


# 4]

#         *
#        * *
#       * * *
#      * * * *
#     * * * * *

n = int(input("\nEnter a number: "))

for num in range(n + 1):
    print(" " * (n - num), "* " * (num))
