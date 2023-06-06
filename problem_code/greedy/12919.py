from sys import stdin

def search(s,t,a,b):
    
    #두 문자열의 길이가 같을때, 두 문자열이 서로 같은지 비교
    if a == b:

        if s == t:

            return 1

        else:

            return 0
    
    #두 문자열의 길이가 다르다면,
    else:
        
        #T의 0번째 문자가 B인 경우,
        if t[0] == 'B':
            
            #마지막 문자도 B라면 이전에 2)연산을 사용했다.
            #T를 뒤집고, 마지막 문자 B를 제거한다.
            if t[-1] == 'B':
                
                return search(s,t[::-1][:-1],a,b-1)
            
            #마지막 문자가 B가 아니라면? 1),2) 모두 가능하다.
            else:
                
                return max(search(s,t[:-1],a,b-1),search(s,t[::-1][:-1],a,b-1))
        #T의 0번째 문자가 A인 경우
        else:
            
            #T의 마지막 문자가 B라면?
            #S에서 1),2) 연산을 사용해서 절대로 만들 수 없다
            #백트래킹으로 재귀 탐색 중지
            if t[-1] == 'B':
                
                return 0
            
            #T의 마지막 문자가 A라면?
            #오직 1)연산만 가능하다.
            else:
                
                return search(s,t[:-1],a,b-1)
                       
s = stdin.readline().rstrip()
t = stdin.readline().rstrip()

a = len(s)
b = len(t)

print(search(s,t,a,b))