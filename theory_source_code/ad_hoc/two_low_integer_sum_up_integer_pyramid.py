#맨 위의 정수가 x이고, n줄로 구성된 정수 피라미드 만들기
#현재 바로 아래 두 정수의 합이 현재 정수가 된다
n,x = map(int,input().split())

if n == 1:
    
    print(x)

else:
    
    #맨 아래 줄을 1,1,1,1...,1 n개로 구성하고
    #계속 더해가면 맨 위 정수는 2^n-1
    #이것이 최솟값인데, x가 이것보다 작으면 불가능
    if 2**(n-1) > x:
        
        print('impossible')
    
    else:
        
        
        answer = [[1]*n]

        v = 1

        for i in range(n-1,0,-1):

            row = [v*2]*i
            v *= 2
            answer.append(row)
        
        #목표로 하는 x와 2^n-1의 차이를 각 줄의 0번 정수에 더하면 끝
        diff = x - 2**(n-1)
        
        for i in range(n-1,-1,-1):
            
            answer[i][0] += diff
            
            print(*answer[i])