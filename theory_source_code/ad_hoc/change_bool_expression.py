#주어진 논리식의 일부를 적당히 바꿔서 원하는 결과가 나오도록 하는 최소 횟수
#왼쪽부터 마지막 2개를 제외한 논리 연산을 수행해서 a (연산자) (b)의 형태로 두고
#(연산자)와 (b)만 적당히 바꾸면 반드시 원하는 결과가 나오게 할 수 있다
n = int(input())

s = list(input().split())

f = input()

v = s[0]

#연산식 길이가 1인 경우
#연산식과 그대로 비교해서 같으면 안바꾸면 되고 다르면 바꾸면 되고
if n == 1:
    
    if v == f:
        
        print(0)
    
    else:
        
        print(1)

#길이가 3 이상인 경우
#마지막 2개를 제외한 나머지를 왼쪽부터 차례로 연산
else:

    for i in range(2,n-2,2):
        
        if s[i-1] == '&':
            
            if v == 'T' and s[i] == 'T':
                
                v = 'T'
            
            else:
                
                v = 'F'
        
        else:
            
            if v == 'F' and s[i] == 'F':
                
                v = 'F'
            
            else:
                
                v = 'T'
    
    #v s[n-2] s[n-1] 형태의 식에서 원하는 결과 f가 되도록 만들려면?
    #연산자 s[n-2]와 s[n-1]에 따라 최소 횟수를 잘 생각해서.. 모든 경우를 다 계산
    if s[n-2] == '&':
        
        if v == 'T' and s[n-1] == 'T':
            
            if f == 'T': #T & T = T인 경우
                
                print(0)
            
            else: #T & T = F인 경우 T만 F로 바꾸면 
                
                print(1)
        
        else: #F & F, F & T, T & F인 경우
            
            if f == 'F': #결과가 F면 안바꿔도 되고
                
                print(0)
            
            else:
                
                #F & F = T인 경우는 &를 |으로 F를 T로 바꿔야만 가능
                if v == 'F' and s[n-1] == 'F':
                    
                    print(2)
                
                #F & T = T, T & F = T인 경우 &를 |으로 바꾸면 가능
                else:
                    
                    print(1)
    
    else:
        
        #F | F인 경우
        if v == 'F' and s[n-1] == 'F':
            
            if f == 'F': #F | F = F인 경우
                
                print(0)
            
            else: # F | F = T인 경우, F를 T로 바꾸면 가능
                
                print(1)
        
        #T | F, T | T, F | T인 경우
        else:
            
            if f == 'T': #안바꿔도 가능
                
                print(0)
            
            else:
                
                #T | T = F인 경우 T를 F로 바꾸고 |를 &로 바꿔야
                if v == 'T' and s[n-1] == 'T':
                    
                    print(2)
                
                #T | F = F, F | T = F인 경우, |를 &로 바꾸면 가능
                else:
                    
                    print(1)