from sys import stdin

def power(a,f,m):
    
    result = 1

    while f >= 1:
        
        if f % 2 == 1:
            
            result *= a
        
        a *= a

        a %= m

        f = f // 2
    
    return result % m

n = int(stdin.readline())

a_list = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

if n == 0:
    
    print(a_list[0] % m)

elif n == 1:
    
    print(power(a_list[1],a_list[0],m))

else:
    
    result = 1

    big = False
    
    #f(1)이 m-1보다 큰가 작은가?
    for _ in range(1,a_list[0]+1):
        
        result *= a_list[1]
        
        if result > m-1:
            
            big = True
            break
    
    f1mod = power(a_list[1],a_list[0],m-1)
    
    #f(1)이 m-1보다 작다.
    if big == False:
        
        print(power(a_list[2],f1mod,m))
    
    #f(1)이 m-1보다 크거나 같다
    else:
        
        #a2가 m보다 크다면?
        if a_list[2] > m:
            
            #a2랑 m이 서로소일려면, 나누어 떨어지지 않는다
            if a_list[2] % m != 0:
                
                print(power(a_list[2],f1mod,m))
            
            #a2랑 m이 서로소가 아님
            #a2는 m으로 나누어 떨어지므로 나머지가 0
            else:
                
                print(0)
        
        #a2가 m보다 작거나 같다면...
        else: 
            
            #a2와 m이 같다면 당연히 나머지가 0이다
            if a_list[2] == m:
                
                print(0)
            
            #m이 소수이므로, a2와 m이 서로소이다.
            else:
            
                print(power(a_list[2],f1mod,m))