#f(n)이 n의 10진법 각 자릿수의 제곱합
#kf(n) = n을 만족하는 a <= n <= b의 개수

def f(n):
    
    value = 0

    for i in range(len(n)):
        
        value += (int(n[i])*int(n[i]))
    
    return value

k,a,b = map(int,input().split())

count = 0

#n = a1*10^x1 + a2*10^x2 + ....
#f(n) = a1^2 + a2^2 + ...
#ai <= 9
#n <= 10^18이므로 f(n) <= (9^2)*18 = 1458
#1부터 1458까지 모든 f(n)에 대하여 kf(n)이 [a,b]에 존재해야하고
#kf(n)의 각 자릿수 합이 f(n)인지 체크
for x in range(1,1459):
    
    n = k*x

    if n >= a and n <= b:

        v = f(str(n))

        if v == x:
            
            count += 1

print(count)