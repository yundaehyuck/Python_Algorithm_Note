#정수 i의 홀수인 약수의 합
#i의 모든 배수는 i를 약수로 가진다.
n = 10**6

odd_sigma = [0]*(n+1)

#홀수 i에 대하여...
for i in range(1,n+1,2):
    
    #i의 배수 j는 i를 약수로 가지므로.. 이를 누적합시킨다.
    for j in range(i,n+1,i):
        
        odd_sigma[j] += i

#구간 [L,R]의 누적합을 구해야하므로 prefix sum
for i in range(1,n+1):
    
    odd_sigma[i] += odd_sigma[i-1]

T = int(input())

answer = []

for test_case in range(1, T + 1):
    
    a,b = map(int,input().split())
    
    answer.append(f'#{test_case} {odd_sigma[b] - odd_sigma[a-1]}')

print('\n'.join(answer))