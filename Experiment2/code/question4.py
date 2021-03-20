print("\n===============Sort Alphabetically Order===============\n")

userInput = input("Please enter a few strings: ")
userInput = userInput.split()
userInput.sort()
for word in userInput:
    print(word, end=" "),

print("\n\n=======================================================\n")


print("\n===============Palindrome check===============\n")

userInput = input("Please enter a string: ")
print(f"Entered word: {userInput}")
print(f"Reversed word: {userInput[::-1]}")
if userInput == userInput[::-1]:
    print(f"{userInput} is a palindrome.")
else:
    print(f"{userInput} is not a palindrome.")

print("\n==============================================\n")
