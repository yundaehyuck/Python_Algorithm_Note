n,q = map(int,input().split())

s = input()

count = [0]*(n+1)

before = ''

#0~i번 위치까지 존재하는 2번 연속하는 문자의 개수를 count[i]
#누적해서 미리 구해놓는다
for i in range(1,n+1):
    
    if before == s[i-1]:
        
        count[i] += 1
    
    before = s[i-1]
    count[i] += count[i-1]

#[l,r]이 주어질때 해당 부분문자열에서 2번 연속하는 문자의 개수는...
#count[r] - count[l]로 바로 구할 수 있다
for _ in range(q):
    
    l,r = map(int,input().split())

    print(count[r] - count[l])