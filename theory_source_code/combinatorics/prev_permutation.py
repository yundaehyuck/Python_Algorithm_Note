#주어진 순열의 바로 이전 순열 prev_permutation을 구하는 알고리즘

n = int(input())

A = list(map(int,input().split()))

find = False

#수를 뒤에서부터 읽어가면서 처음으로 내림차순이 깨지는 지점을 찾는다.
#a[n-1] > a[n-2] > a[n-3] > ... a[i+1] < a[i]
for i in range(n-2,-1,-1):

    if A[i] > A[i+1]:

        a = A[i] #처음으로 내림차순이 깨지는 i번을 pivot으로 삼는다
        
        #i+1~n-1 구간에서 뒤에서부터 읽어서 pivot보다 처음으로 한단계 작은 수를 찾는다
        #그러한 수가 a[j]이면 a[i]와 swap
        for j in range(n-1,i,-1):
            
            if a > A[j]:
                
                A[i],A[j] = A[j],A[i]
                break
        
        #이제 i+1 ~ n-1 구간을 내림차순으로 정렬
        #a[i+1] > a[i+2] > ... a[n-1]로 하면 바로 이전 순열이 된다.
        A[i+1:] = A[i+1:][::-1]
        
        """
        l = n - (i+1)

        if l % 2 == 0:
            
            l //= 2
            l -= 1
        
        else:
            
            l //= 2

        for j in range(i+1,i+1+l+1):
            
            A[j],A[n-1-j+(i+1)] = A[n-1-j+(i+1)],A[j]"""

        find = True
        break

if find:

    print(*A)

else: #pivot을 찾지 못하는 경우

    print(-1)