#sum((a+b)%mod)
#no (sum((a+b)%mod))%mod

#sum_of_(a+b) = (n-1)sum_of(a)

#counting a+b > 10^8

#sum((a+b)%mod) = (n-1)sum_of(a) - counting(a+b > 10^8)

n = int(input())

A = list(map(int,input().split()))

A.sort()

mod = 10**8

count = 0

j = n

#순서쌍의 합이 10^8보다 큰 경우의 수를 찾는다
#A가 정렬되어 있으므로, 
#왼쪽 포인터가 점점 커지면, 오른쪽 포인터는 계속 작아져야한다

for i in range(n-1):
    
    if j < i+1: #오른쪽 포인터가 계속 작아지므로, 왼쪽 포인터보다 작아지는 경우 초기화
        
        j = i+1
        
    while j-i > 1 and A[j-1]+A[i] >= mod:
        
        j -= 1

    count += (n-j)


v = 0

#모든 순서쌍의 합의 합 = (n-1)sum_of(a)

for i in range(n):
    
    v += ((n-1)*A[i])

#a+b가 10^8보다 작은 경우는 나눠도 그대로
#10^8보다 큰 경우는 나누면 나머지가 생기며, a+b - 10^8과 같다.(a <= 10^8)
#따라서 이 값에, 순서쌍의 합이 10^8보다 큰 경우의 수를 빼주면
print(v - count*mod)