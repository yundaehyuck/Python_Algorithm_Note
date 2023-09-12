from sys import stdin

#fibonacci representation
def representation(n):
    
    count = 0 #피보나치 수를 사용한 수
    
    while n:
        
        #가장 큰 피보나치 수부터 거꾸로 순회하여...
        for i in range(86,-1,-1):
            
            if f[i] == n: #만약 n과 피보나치 수가 동일하다면 그걸 쓰면 끝이니까 count+1을 바로 return
                
                count += 1

                return count
            
            #처음으로 n보다 작아지는 피보나치 수 f[i]를 구함
            elif f[i] < n:
                
                break
        
        #그러면 f[i+1]은 n보다 크고 f[i]는 n보다 작다
        large = f[i+1]
        small = f[i]
        
        #이때 n과 거리 차이가 작은 수를 사용함
        #여기서 large를 써야한다면, n = n - large로 음수가 아니라 n = large - n으로 양수를 사용
        #제켄도르프 분해에 의하면 모든 양의 정수 n은 연속하지 않은 피보나치 수의 합으로 표현할 수 있다
        if (large - n) >= (n - small):
            
            n -= small
            count += 1
        
        else:
            
            n = large - n
            count += 1
    
    return count

#4*10^17에 가장 가까운 F86 = 420196140727489673
f = [0,1,1]

for i in range(3,87):
    
    f.append(f[i-1]+f[i-2])

p = int(stdin.readline())

for _ in range(p):
    
    n = int(stdin.readline())

    print(representation(n))