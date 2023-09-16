#z_function을 구하는 방법을 이용한
#s와 접두사 s[1,2,..,i]의 가장 긴 공통 접미사의 길이 z[i]를 구하는 함수
#기존 z_function 구하는 과정을 반대로 생각
def z_function(s):
    
    n = len(s)

    z = [0]*n

    #z[n-1] = n #문제에 따라 필요하다면 정의
    
    #접미사가 일치하는 구간 중 왼쪽 끝점이 가장 왼쪽에 있는 구간 [left,right]
    left = n-1
    right = n-1
    
    #n-2부터 0으로 역방향으로 순회
    for i in range(n-2,-1,-1):
        
        if i > left: #현재 인덱스 i가 [left,right]안에 있는 경우...
            
            #z[i]를 z[i+n-1-right]와 i-left중 작은 값으로 시작할 수 있다.
            z[i] = min(z[i+n-1-right], i-left)
        
        #마지막 인덱스는 -1이므로, s[-z[i]-1]과 s[i-z[i]]가 일치하면 z[i]를 1씩 증가하는 방식으로
        #가장 긴 접미사의 길이를 찾는다.
        while i-z[i] >= 0 and s[-z[i]-1] == s[i-z[i]]:
            
            z[i] += 1
        
        #왼쪽 점은 i-z[i]이고 오른쪽 점은 i이므로, i-z[i]가 기존 left보다 작다면, 왼쪽으로 더 갔으므로 갱신
        if i-z[i] < left:
            
            left = i-z[i]
            right = i
    
    return z


"""
#혹은 문자열 s를 역으로 배열하고, 원래 z-function을 적용한 다음
#z[-i]가 s와 s[1,2,..,i]의 가장 긴 공통 접미사의 길이가 된다.
from sys import stdin

def z_function(s):
    
    n = len(s)

    z = [0]*n

    z[0] = n

    left = 0
    right = 0

    for i in range(1,n):
        
        if i < right:
            
            z[i] = min(right - i, z[i-left])
        
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            
            z[i] += 1
        
        if i+z[i] > right:
            
            left = i
            right = i+z[i]
    
    return z

s = stdin.readline().rstrip()[::-1]

z = z_function(s)

m = int(stdin.readline())

for _ in range(m):
    
    i = int(stdin.readline())

    print(z[-i])
"""