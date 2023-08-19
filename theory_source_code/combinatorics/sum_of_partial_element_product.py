from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    clothes = {}

    for _ in range(n):
        
        a,b = stdin.readline().rstrip().split()

        clothes[b] = clothes.get(b,0) + 1
    
    answer = 1

    #모든 부분집합 원소의 곱의 합
    #Sk = 원소가 k개인 모든 부분집합들의 원소들의 곱의 합
    #(1+a1)(1+a2)...(1+an) = 1+S1+S2+...Sn
    for k,v in clothes.items():
        
        answer *= (v+1)
    
    print(answer - 1)