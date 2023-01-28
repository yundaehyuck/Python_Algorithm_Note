from sys import stdin

s = stdin.readline().rstrip()
burst = stdin.readline().rstrip()

len_b = len(burst)

stack = []

len_s = 0

for char in s:
    
    stack.append(char)
    len_s += 1
    
    if char == burst[-1] and len_s >= len_b:
        
        temp = []

        for j in range(len_b-1,-1,-1):
            
            boom = stack.pop()
            len_s -= 1

            if boom == burst[j]:
                
                temp.append(boom)
            
            else:
                
                stack.append(boom)
                len_s += 1

                while temp:
                    
                    stack.append(temp.pop())
                    len_s += 1
                
                break
            
if stack == []:
    
    print('FRULA')

else:
    
    print(''.join(stack))