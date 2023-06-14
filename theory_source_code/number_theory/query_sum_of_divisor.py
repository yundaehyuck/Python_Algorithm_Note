from sys import stdin

T = int(stdin.readline())

n = 1000000

answer = [0]*(n+1)

#1부터 n까지 각 i에 대하여,
for i in range(1,n+1):
    
    #i의 배수인 j는 i를 약수로 가지므로,
    for j in range(i,n+1,i):
        
        answer[j] += i #j부분에 약수 i를 더해준다.
    
    #이전 i-1에 구해놓은 약수들의 합을 다음 i에 누적해준다. 
    answer[i] += answer[i-1]
    
for _ in range(T):
    
    n = int(stdin.readline())

    print(answer[n])