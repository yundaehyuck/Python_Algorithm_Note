from sys import stdin

#인접한 원소간 차이의 최댓값이 최소가 되도록 배치하는 방법
#배열을 정렬하고, 가장 작은 원소부터 왼쪽 끝, 오른쪽 끝에 번갈아 배치한다

T = int(stdin.readline())

for _ in range(T):
    
    n = int(stdin.readline())

    A = list(map(int,stdin.readline().split()))

    A.sort()

    B = [0]*n

    left = 0
    right = n-1

    for i in range(n):
        
        if i % 2 == 0:

            B[left] = A[i]
            left += 1

        else:

            B[right] = A[i]
            right -= 1
    
    answer = B[-1] - B[0] #오른쪽이 더 큰 값으로 배치해둠

    for i in range(n):

        k = abs(B[i] - B[i-1]) 

        if k > answer:
            
            answer = k
    
    print(answer)