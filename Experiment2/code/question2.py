import array as x
 
n = int(input("Enter number of elements: ")) 

nums = map(int, input(f"Enter {n} numbers in a single line with spaces in between: ").split())

a = x.array('i', nums)

print("Array after removing primes:", end=" ")

b = x.array('i', [])
for s in a:
    for i in range(2, s):
        if(s % i==0):
            break;
        if(i==s-1):
            b.append(s)
for ss in b:
    while ss in a:
        a.remove(ss)

print(a)