from sys import stdin

s = stdin.readline().rstrip()
burst = stdin.readline().rstrip()

len_b = len(burst)

stack = []

for char in s:
    
    stack.append(char)
    
    if char == burst[-1]:
        
        if burst == ''.join(stack[-len_b:]):
            

            del stack[-len_b:]

            # for _ in range(len_b):
            
            #     stack.pop()
            
if stack == []:
    
    print('FRULA')

else:
    
    print(''.join(stack))