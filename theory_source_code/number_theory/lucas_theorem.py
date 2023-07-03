#lucas theorem
n,k,m = map(int,input().split())

factorial = [0]*m
factorial[0] = 1

#m으로 나눈 나머지인 0,1,..,m-1!을 구해준다.
for i in range(1,m):
    
    factorial[i] = factorial[i-1] * i
    factorial[i] %= m

answer = 1

#n > 0일때까지 반복해나감
while n > 0:
    
    n,r1 = n//m, n%m
    k,r2 = k//m, k%m
    
    #n,k를 m으로 나눈 나머지인 r1,r2에 대해 r1Cr2 mod m을 구해준다.
    #m은 소수이고 r1,r2는 m과 서로소이므로 페르마의 소정리를 이용
    #그런데, r1 < r2이면 r1Cr2 = 0이므로 바로 반복문을 종료
    if r1 >= r2:
        
        answer *= (factorial[r1])*pow(factorial[r1-r2]*factorial[r2],m-2,m)
        answer %= m
    
    else:
        
        answer = 0
        break


print(answer)