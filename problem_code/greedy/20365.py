n = int(input())

s = input()

stack = [s[0]]

for i in range(1,n):
    
    if stack[-1] != s[i]:
        
        stack.append(s[i])

answer = 0

if stack[0] != stack[-1]:
    
    stack.pop()
    answer = 1

if len(stack) % 2 == 0:
    
    print(answer + len(stack)//2)

else:
    
    print(answer + len(stack)//2+1)