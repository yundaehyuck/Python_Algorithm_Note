#negative mod

def negative_mod(x,mod):
    
    if x < 0:
        
        return (x+mod)%mod
    
    else:
        
        return x%mod
 
#naive polynomial division
#a/b
def divide(a,b,mod):
    
    q = [0]*(len(a)-len(b)+1) #몫

    for i in range(len(q)-1,-1,-1):
        
        #몫의 최고차항을 결정
        q[i] = a[i+len(b)-1]//b[-1]

        for j in range(len(b)-1,-1,-1):
            
            #몫의 최고차항과 b의 항을 차례대로 곱하면서 a에 빼준다
            a[i+j] -= (q[i]*b[j])
            a[i+j] = negative_mod(a[i+j],mod) #값이 음수 일 수 있음
    
    #나머지 차수 재조정
    while a:
        
        x = a.pop()

        if x != 0:

            a.append(x)
            break
             
    return q,a #몫,나머지

a = [-1,1,-2,3]
b = [-1,-1,1]

print(divide(a,b,10**9+7))
([1, 3], [0, 5])