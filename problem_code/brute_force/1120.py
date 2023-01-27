from sys import stdin

a,b = stdin.readline().rstrip().split()

len_a = len(a)
len_b = len(b)

min_value = 51

for i in range(len_b-len_a+1):
    
    new_b = b[i:len_a+i]

    answer = 0

    for x,y in zip(a,new_b):
        
        if x != y:
            
            answer += 1
    
    if min_value > answer:
        
        min_value = answer

print(min_value)