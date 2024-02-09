from collections import deque

def solution(coin, cards):
    answer = 0
    
    A = [] #처음에 뽑은 카드 n/3장 저장해두는 배열
    B = [] #매 시작마다 뽑는 카드 2장을 저장해두는 배열
    cards = deque(cards)
    
    n = len(cards)
    
    #처음에 n/3장을 가지도록 카드 보유
    while len(A) < n//3:
        A.append(cards.popleft())
    
    
    while 1:
        
        answer += 1 #라운드 시작
        
        if len(cards) == 0: #더 이상 뽑을 카드가 없는 경우 게임 종료
            break
        
        #카드 뭉치 위에서 카드 2장을 뽑는다
        a = cards.popleft()
        b = cards.popleft()
        
        #카드 뽑으면 임시 배열 B에 저장
        B.append(a)
        B.append(b)
        
        #n+1을 낼 수 있는지 체크
        find = False
        
        #첫번째, 가지고 있는 카드만으로 n+1을 낼 수 있는 경우
        for i in range(len(A)):
            
            for j in range(i+1,len(A)):
                
                if A[i]+A[j] == n+1:
                
                     #i < j이므로 i번째 원소 제거했으면, j번째 원소는 j-1번째가 된다
                    del A[i]
                    del A[j-1]
                    find = True
                    break
            
            if find:
                break
        
        #첫번째가 불가능한 경우
        if find == False:
            
            #두번째, 동전이 1개 이상일때,
            if coin >= 1:
                
                #가지고 있는 카드 A와 임시로 저장해둔 B에서 1장씩 사용해서 n+1이 되는지 체크
                for i in range(len(A)):
                    for j in range(len(B)):

                        if A[i] + B[j] == n+1:
                            
                            del A[i]
                            del B[j]
                            find = True
                            break
                    
                    if find:
                        break
                
                if find:
                    coin -= 1 #가능하다면 동전 1개 쓰고 다음으로
                
                #두번째가 불가능한 경우,
                else:
                    
                    #세번째, 동전 2개 이상일때,
                    if coin >= 2:
                        
                        #임시로 저장해둔 배열 B에 저장된 카드 2장으로 n+1이 되는지 체크
                        for i in range(len(B)):
                            for j in range(i+1,len(B)):

                                if B[i] + B[j] == n+1:
                                
                                #i < j이므로 i번째 원소 제거했으면, j번째 원소는 j-1번째가 된다
                                
                                    del B[i] 
                                    del B[j-1]
                                    find = True
                                    break

                            if find:
                                break
                        
                        if find:
                            coin -= 2 #가능하다면 동전 2개 쓰고 다음으로 넘어감
                        
                        #여기마저도 불가능하다면 게임 종료
                        else:
                            break
                    
                    #동전이 2개 이상이 아니면 게임 종료
                    else:
                        break
            
            #동전이 1개 이상이 아니면 게임 종료
            else:    
                break        
    
        
    return answer