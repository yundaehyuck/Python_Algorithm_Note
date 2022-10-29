#다이나믹 프로그래밍으로 최장 증가 부분수열 찾기

s = [3,2,6,4,5,1]

n = len(s)

dp = [0] * n ##현재 위치의 최장 증가부분수열의 길이를 저장

#-1은 없다고 가정
p = [(-1,-1)] * n ##최장증가부분수열에서 해당 위치 이전에 나타날 수 있는 수

for i in range(n):
    
    dp[i] = 1 #시작은 모두 1로 채우고..

    for j in range(i):
        
        #s[i]보다 작은 s[j]를 찾고..

        if s[j] < s[i]:
            
            #그러면 dp[i]는... dp[j]+1중에서 최댓값이.. s[i]가 포함된 최장 증가부분수열의 길이

            if dp[i] < 1 + dp[j]:
                
                dp[i] = 1+dp[j]

                p[i] = (s[j],j) #현재 i번 이전에 나올 수 있는 j번 원소와 추적이 쉽게 인덱스도 같이 저장

###역추적

##max값이 되는 index를 찾는다

max_ind = 0

for i in range(n):
    
    if dp[max_ind] < dp[i]:
        
        max_ind = i

lis_list = [s[max_ind]]

#역추적해서 -1이 나올때까지 반복
while 1:
    
    element,max_ind = p[max_ind] #원소와 해당 원소의 s배열에서의 위치
    
    if element == -1: #원소가 -1이라면 해당 위치가 마지막이라는 뜻
        
        break
    
    lis_list.append(element)


print(lis_list[::-1])
"""
[3,4,5]
"""