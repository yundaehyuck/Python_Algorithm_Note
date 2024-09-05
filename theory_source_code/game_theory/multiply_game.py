def game(n):

    position = 0

    #n부터 거꾸로 시작해서 반드시 이길려면
    #X = [n//9,n//9+1,...,n-1]

    #다음 사람이 X로 보낼수밖에 없는 위치는...(패배하는 위치)
    #Y = [n//9//2, n//9//2+1,..., n//9-1]

    while n > 1:

        if position == 0: #승리 상태

            x,y = n//9, n%9
            position = 1

        else: #패배 상태

            x,y = n//2, n%2
            position = 0

        if y != 0:

            x += 1

        n = x
    
    #n이 1인 순간 position이 0이라면?
    #position = 1에서 n//2,n%2를 계산하고 n = x로 넘긴 다음 position = 0으로 되었으므로
    #즉 선공이 한번 하면 position = 1(패배상태)로 이동하므로 이 n은 패배 상태에 속한다는 의미
    if position == 0:

        return 'Donghyuk wins.'

    else:

        return 'Baekjoon wins.'

"""
#다이나믹 프로그래밍
def game(p):
    
    #이미 계산된 값이 있으면 바로 return
    if dp.get(p,-1) != -1:
        
        return dp[p]
    
    #p >= n인 p를 받으면 받은 사람은 지게 되므로(넘겨준 사람이 이미 p >= n에 도달했으니까)
    if p >= n:
        
        return 0
        
    dp[p] = 0
    
    #현재 상태 p에서 2~9를 곱해 재귀적으로 넘겨줌
    #지는 상태로 이동할 수 있다면 그 값을 넘겨주면 되므로 
    #현재 상태 p는 이기는 상태 
    for i in range(2,10):
        
        if game(p*i) == 0:
            
            dp[p] = 1
            break
    
    return dp[p]
"""

while 1:
    
    try:

        n = int(input())

        print(game(n))
        
    except:
        
        break