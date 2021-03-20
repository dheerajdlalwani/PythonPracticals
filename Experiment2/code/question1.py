import array as arr

print("\n========== Read and Display an array ==========\n")

x = arr.array('i', [])

n = int(input("Enter number of elements: "))

for i in range(n):
    ele = int(input(f"Enter element array[{i + 1}]: "))
    x.append(ele)
print("The array :", end=" ")
for i in range(n):
    print(x[i], end=" ")

print("\n\n=============================================\n")


print("\n=============== Append new ===============\n")

ip = int(input("Enter an item to be appended: "))
x.append(ip)
for element in x:
    print(element, end=" ")

print("\n==========================================\n")


print("\n=============== Reverse Array ===============\n")

for i in x[::-1]:
    print(i, end=" ")

print("\n=============================================\n")

print("\n========== Length in Bytes of 1 item ==========\n")

print(f"Length in bytes of one array item: {str(x.itemsize)}")

print("\n===============================================\n")

print("\n======== Append items from another array ========\n")

y = arr.array('i', [7, 8, 9])
x.append(y[2])
print(x)

print("\n===============================================\n")

print("\n========== Inserting at a specific location ==========\n")

item = int(input("Enter an item to be appended: "))
pos = int(input(f"Enter the position where {item} is to be appended: "))
x.insert(pos, item)
print(x)

print("\n===============================================\n")

print("\n========== Array to string ==========\n")

print(' '.join(map(str, x)))

print("\n=====================================\n")
