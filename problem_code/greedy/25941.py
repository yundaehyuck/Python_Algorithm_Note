n,b,a = map(int,input().split())

price = list(map(int,input().split()))

#가격 오름차순 정렬
price.sort()

#모든 물건을 다 살 수 있을때..
answer = n

#물건 사기 시도
for i in range(n):
    
    #모든 물건을 무조건 절반가격에 사들인다
    b -= price[i]//2
    
    #물건 할인 횟수 a 이상이 된다면,
    if i >= a:
        
        #가장 싼 물건부터 절반가격을 더 줘서, 정상가격으로 사들인다
        b -= price[i-a]//2
    
    #예산이 음수가 된다면..
    #현재 i+1개의 물건은 살 수 없다는 뜻이므로..(인덱스는 0부터 시작)
    #전체 i개의 물건을 살 수 있다는 뜻이다
    if b < 0:
        
        answer = i
        
        break

print(answer)