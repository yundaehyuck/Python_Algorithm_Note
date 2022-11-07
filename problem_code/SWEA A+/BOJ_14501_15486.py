from sys import stdin

#입력을 받는다
n = int(stdin.readline())

#인덱스 편의를 위해 1~n이 되도록 0은 미리 추가해놓는다. 
t_list = [0]
p_list = [0]

for _ in range(n):
    
    t,p = map(int,stdin.readline().split())

    t_list.append(t)
    p_list.append(p)

#n+1일에 퇴사하므로, n일까지는 상담이 가능하다.
#dp[n+1]을 구하는게 목표
dp = [0]*(n+2)

for i in range(1,n+1):
    
    #매 순회마다, 이전 날에 얻은 이익이 더 크다면 그것을 가져가야한다.
    #이 과정 자체가 어떤 상담은 선택하지 않고, 어떤 상담은 선택하는 효과를 준다.
    if dp[i] < dp[i-1]:
        
        dp[i] = dp[i-1]
    
    #정산받는 날은 t_list[i]+i이고, 이것이 n+1이내여야 상담 선택 가능하다.
    if t_list[i]+i <= n+1:
        
        #i일차의 상담을 선택해봐서, 최대이익이라면 교체해준다.
        dp[t_list[i]+i] = max(dp[t_list[i]+i],dp[i]+p_list[i])

#마지막 n까지 순회하고 나서 n+1일차에 가져가는 돈은...
#n일차 돈과 n+1일차 돈을 비교해서 최대이익 돈을 가져가도록 교체해준다.
#역시 이런 과정 자체가, 어떤 상담은 선택하고 어떤 상담은 선택하지 않는 효과를 준다.
if dp[n] > dp[n+1]:
    
    dp[n+1] = dp[n]

print(dp[n+1])