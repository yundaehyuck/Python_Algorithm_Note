n,a = map(int,input().split())

answer = 0

k = 1

#n!이 가지고 있는 a의 개수는 n이하의 a의 거듭제곱의 배수의 개수와 같다
#n//a + n//a^2 + n//a^3 + ...
while 1:
    
    x = n//(a**k)

    if x == 0:
        
        break

    answer += x
    
    k += 1

print(answer)