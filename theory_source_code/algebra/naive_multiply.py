#naive polynomial multiplication
def multiply(a,b,mod):

    result = [0]*(len(a)+len(b)-1)

    for i in range(len(a)):
        
        for j in range(len(b)):
            
            result[i+j] += (a[i]*b[j]) % mod
    
    return result

a = [1,1,2]
b = [5,1]

print(multiply(a,b,10**9+7))
[5,6,11,2]