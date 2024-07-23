#짝수 위치 자리수들의 곱과 홀수 위치 자리수들의 곱이 서로 같은 14자리 자연수의 개수를 찾는 방법

odd = {}

for x1 in range(1,10):
    
    for x3 in range(10):
        
        for x5 in range(10):
            
            for x7 in range(10):
                
                for x9 in range(10):
                    
                    for x11 in range(10):
                        
                        for x13 in range(10):
                
                            v = x1*x3*x5*x7*x9*x11*x13
                            odd[v] = odd.get(v,0) + 1

even = {}

for x2 in range(10):
    
    for x4 in range(10):
        
        for x6 in range(10):
            
            for x8 in range(10):
                
                for x10 in range(10):
                    
                    for x12 in range(10):
                        
                        for x14 in range(10):
                
                            v = x2*x4*x6*x8*x10*x12*x14
                            even[v] = even.get(v,0) + 1


count = 0

for a in odd:
    
    for b in even:
        
        if a == b:
            
            count += (odd[a]*even[b])

print(count)