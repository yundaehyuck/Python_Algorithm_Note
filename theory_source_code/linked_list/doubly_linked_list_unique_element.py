#서로 다른 모든 원소에 대하여
#x의 오른쪽에 y를 삽입하고 x를 삭제하는 연산을 수행하는 연결리스트
n = int(input())

A = list(map(int,input().split()))

right = {} #오른쪽 방향
left = {} #왼쪽 방향

for i in range(n-1):
    
    right[A[i]] = A[i+1]

right[A[n-1]] = -1 #꼬리의 오른쪽은 -1
 
for i in range(n-1,0,-1):

    left[A[i]] = A[i-1]

left[A[0]] = -1 #head의 왼쪽은 -1

q = int(input())

for _ in range(q):
    
    query = list(map(int,input().split()))

    if query[0] == 1: #x의 오른쪽에 y를 삽입
        
        x,y = query[1],query[2]

        if right[x] == -1: #x가 꼬리인 경우
            
            #x의 오른쪽을 y로 하고, y의 왼쪽을 x, y의 오른쪽을 -1
            right[x] = y 
            left[y] = x
            right[y] = -1
        
        else: #x가 꼬리가 아닌 경우 x > y > k, x < y < k가 되어야한다.
        
            k = right[x]
            right[x] = y
            right[y] = k #x > y > k
            left[y] = x
            left[k] = y
    
    else:

        x = query[1] #x를 삭제하는 연산

        if right[x] == -1: #x가 꼬리인 경우
            
            y = left[x] #x의 왼쪽을 찾고

            del right[x]
            del left[x]

            right[y] = -1 #x의 왼쪽인 y의 오른쪽을 -1로
        
        elif left[x] == -1: #x가 head인 경우
            
            y = right[x] #x의 오른쪽을 찾고

            del right[x]
            del left[x]

            left[y] = -1 #y의 왼쪽을 -1로 연결시켜
        
        else: #a > x > b, a < x < b 형태인 경우
            
            a = left[x]
            b = right[x] #a > x > b

            del right[x]
            del left[x]
            
            #x의 연결을 삭제하고 a > b, a < b로 연결
            right[a] = b
            left[b] = a

#head를 찾는 과정
#왼쪽이 -1인 원소가 head이다
for k,v in left.items():
    
    if v == -1:
        
        break

A = [k] #head부터 시작해서, 오른쪽이 -1인 원소(꼬리)를 찾을때까지 반복

while 1:
    
    k = right[k]

    if k == -1:
        
        break
    
    A.append(k)

print(*A)