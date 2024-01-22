#x1^x2^...xk = y1^y2^...y(n-k)일때, x1+x2+..xk의 최댓값
n = int(input())

A = list(map(int,input().split()))

v = A[0]

#양변에 y1^y2^..y(n-k)를 xor한다면 a1^a2^...an = 0이 된다.
for i in range(1,n):
    
    v ^= A[i]

#따라서 모든 원소를 xor했을때 0이 안된다면 불가능하다.
if v != 0:
    
    print(0)

#모든 원소를 xor했을때 0이 된다면..
else:
    
    #a1 <= a2 <= ... an이라고 가정할때..
    #a1^a2^..^an=0에서 a1을 xor하면
    #(a1^a2^..^an)^a1 = 0^a1
    #a2^a3^...an = a1
    #따라서, x집합으로 a2,a3,...,an을 선택하면 최대가 된다.
    print(sum(A) - min(A))