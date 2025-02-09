from sys import stdin

#정수 x의 거듭제곱 x^0,x^1,...의 집합의 모든 부분집합 A1,A2,...의 각 집합의 원소들의 합을 오름차순으로 정렬한 수열
#a1,a2,...의 k번째 수

#각 부분집합은 예를 들면 x^3 + x^2 + x^1, x^5, x^4 + x^1 등등이 있다
#이는 잘 보면 이진법 1110, 100000, 10010을 x진법으로 바꾼것이다

#따라서 1,2,3,..을 이진법 1,10,11,..로 나타내고 이를 x진법으로 나타내면 수열 a를 구할 수 있다
#따라서 k를 이진법으로 나타내고 이를 x진법으로 바꾸면 된다

n = int(stdin.readline())

mod = 10**9+7

v = 0

for _ in range(n):
    
    x,k = map(int,stdin.readline().split())

    k = bin(k)[2:]
    
    j = 0

    for i in range(len(k)-1,-1,-1):
        
        if k[i] == '1':
            
            v += pow(x,j,mod)
            v %= mod
        
        j += 1

print(v)