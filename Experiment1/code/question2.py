# Question: Write a python program to show output formatting take two values and display them
# Using only one print function amd % operator

print("\n=============================================================\n")
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print("\nThis is {}.\n{} is {} years old.\n{} does his practicals on his own and \nopen sources it for everyone.\nBe like {}".format(
    name, name, age, name, name))
print("\n==============================================================\n")
questionNumber = 2
experimentNumber = 1
print("This is Experiment Number %d, question number%d" %
      (experimentNumber, questionNumber))
print("\n==============================================================\n")
