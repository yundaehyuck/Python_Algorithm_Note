#x0,x1,..,xn이 주어지고 k > 0 , xi,xi+k에 좌표를 남겼을때 가능한 k를 모두 찾는 방법
n = int(input())

A = list(map(int,input().split()))

#X값들을 미리 저장해두고
h = {}

for i in range(n):
    
    h[A[i]] = 1

answer = []

#i = 1,2,..,n-1에 대해 k = xi - x0에 대하여 x0,xi에 좌표를 남겼다면
#j = 1,2,..,n-1에 대해 xj,xj+k에 좌표를 모두 남길 수 있다면 충분하다
for i in range(1,n):
            
    k = A[i] - A[0]
    
    no = False

    for j in range(1,n):
        
        #[xj,xj+k]가 존재하면 상관없긴한데, 존재하지 않는다면
        if h.get(A[j] + k,0) == 0:
            
            #[xj-k,xj]가 존재한다면 조건을 만족하게 된다
            #이걸 확인하지 않으면
            #[0,5,10,15]의 경우 k = 5에서 [0,5], [5,10], [10,15]까지 보다가
            #[15,20]이 존재하지 않으니 k = 5는 불가능하다!라고 결론내린다
            #[10,15]가 존재하니 k = 5가 가능하다라고 할려면 xj-k를 봐야함
            if h.get(A[j] - k,0) == 0:
                
                no = True
                break
    
    if no == False:
        
        answer.append(k)

print(len(answer))
print(*answer)