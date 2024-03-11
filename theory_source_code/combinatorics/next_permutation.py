#다음 순열 next permutation을 찾는 알고리즘
n = int(input())

A = list(map(int,input().split()))

find = False

#뒤에서부터 순서대로 읽어서 오름차순인지 확인
#a[n-1] < a[n-2] < a[n-3] < ...
#처음으로 뒤에서부터 오름차순이 깨지는 i번 인덱스를 찾는다.
for i in range(n-2,-1,-1):
    
    if A[i] < A[i+1]:
        
        find = True
        a = A[i] #pivot
        
        #pivot이후인 i+1,i+2,..,n-1중에서 pivot보다 처음으로 한단계 더 큰 원소를 찾는다
        #뒤에서부터 읽어서 처음으로 A[j] > A[i]인 j번을 찾고 둘을 swap한다
        for j in range(n-1,i,-1):
            
            if A[j] > a:
                
                A[i],A[j] = A[j],A[i]
                break
        
        #swap하고 나서 i+1~n-1번을 a[i+1] < a[i+2] < ... < a[n-1]로 정렬시킨다.
        #a[i+1] > a[i+2] > ... > a[n-1]이기 때문에
        #a[i+1] > a[n-1]
        #a[i+2] > a[n-2]
        #...로 서로 swap하기만 하면 된다.
        #i+1 ~ n-1
        
        A[i+1:] = A[i+1:][::-1]
        """
        l = n - (i + 1)

        if l % 2 == 0:
            
            l //= 2
            l -= 1
        
        else:
            
            l //= 2

        for j in range(i+1,i+1+l+1):
            
            #i+1 > n-1
            #i+2 > n-1-1
            #...
            A[j],A[n-1-(j-(i+1))] = A[n-1-(j-(i+1))],A[j]"""
        
        
        break
        
if find == False: #pivot을 찾지 못한 경우
    
    print(-1)

else:

    print(*A)