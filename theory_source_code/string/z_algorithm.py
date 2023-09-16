#z algorithm
#문자열 s와 s의 i번째 접미사 s[i,i+1,...]의 가장 긴 공통 접두사의 길이 z[i]
def z_function(s):
    
    n = len(s)

    z = [0]*n
    
    #z[0] = n #문제에 따라 필요하다면 정의
    
    #지금까지 접두사와 일치한 구간 중 오른쪽 끝점이 가장 오른쪽에 있는 구간 [left,right]
    left = 0
    right = 0

    for i in range(1,n):
        
        if i < right: #현재 인덱스 i가 [left,right]안에 있다면....
            
            #z[i]의 시작점은 0이 아니라 right-i, z[i-left]중 작은 것에서 시작할 수 있다.
            z[i] = min(right - i, z[i - left])
        
        #현재 인덱스 i가 [left,right]밖에 있다면 z[i]는 0에서 시작한다.
        
        #z[i]부터 시작해서 s[z[i]]와 s[i+z[i]]가 같으면 z[i]를 1씩 증가
        while i + z[i] < n and s[z[i]] == s[i+z[i]]:
            
            z[i] += 1
        
        #새로 일치하는 구간을 구했는데, 오른쪽 점 i+z[i]가 기존 right보다 크다면 새로 갱신
        if i+z[i] > right:
            
            left = i
            right = i + z[i]
    
    return z

print(z_function('abacaba'))
[0, 0, 1, 0, 3, 0, 1]