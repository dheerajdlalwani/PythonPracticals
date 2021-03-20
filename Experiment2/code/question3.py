userInput = input("Please enter a string: ")
ans = ""
cnt = 0
for ch in userInput:
    if(ch == 'a'):
        cnt += 1
        if(cnt > 1):
            ans += '@'
        else:
            ans += ch
    else:
        ans += ch
print(ans)
