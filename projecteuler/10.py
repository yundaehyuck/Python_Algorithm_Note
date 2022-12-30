n = 2000000

result = [1]*(n+1)

answer = 0

for i in range(2,int((n+1)**(1/2))+1):
    
    if result[i] == 1:
        
        for j in range(i+i,n+1,i):
            
            result[j] = 0
    

for i in range(2,n+1):
    
    if result [i] == 1:
        
        answer += i

print(answer)