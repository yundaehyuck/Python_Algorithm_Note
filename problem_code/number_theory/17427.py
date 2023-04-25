from sys import stdin

def get_spf(n):
    
    spf = [i for i in range(n+1)]

    for i in range(4,n+1,2):
        
        spf[i] = 2
    
    for i in range(3,int((n+1)**(1/2))+1):
        
        if spf[i] == i:
            
            for j in range(i*i,n+1,i):
                
                if spf[j] == j:
                    
                    spf[j] = i
    
    return spf

def factorization(n,spf):
    
    summation = {}

    answer = 1

    while n != 1:
        
        summation[spf[n]] = summation.get(spf[n],0) + 1

        n = n//spf[n]
    
    for a,b in summation.items():
        
        answer *= (a**(b+1)-1)//(a-1)

    return answer

n = int(stdin.readline())

spf = get_spf(n)

answer = 0

for i in range(1,n+1):
    
    if i == 1:
        
        answer += 1
    
    elif spf[i] == i:
        
        answer += (i+1)
    
    else:
        
        answer += factorization(i,spf)

print(answer)