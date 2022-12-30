from sys import stdin

#https://www.acmicpc.net/problem/23062
#확장 유클리드 알고리즘
def extended_gcd(a,b):
    
    before_x = 1
    before_y = 0

    x = 0 
    y = 1

    while b != 0:
        
        q,r = a//b, a%b

        a,b = b,r

        before_x,x = x,before_x-x*q
        before_y,y = y,before_y-y*q
    
    return a,before_x,before_y

#유클리드 알고리즘
def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

T = int(stdin.readline())

for _ in range(T):
    
    A,B,C,a,b,c = map(int,stdin.readline().split())

    m = [0,A,B,C]
    s = [0,a,b,c]

    answer = 0

    for i in range(1,3):

        m_gcd = gcd(m[i],m[i+1])

        #abs(s[i+1]-s[i])로 절댓값 취하지 않아도 된다.

        if (s[i+1] - s[i]) % m_gcd != 0:

            answer = -1
            break 

        M_gcd,k1,k2 = extended_gcd(m[i]//m_gcd,m[i+1]//m_gcd)
        
        #서로소가 아닐때, 중국인의 나머지 정리 점화식
        s[i+1] = m[i]*(s[i+1]-s[i])*k1//m_gcd + s[i]
        m[i+1] = m[i]*m[i+1]//m_gcd
    
    #s[-1]이 음수일수 있어서 최소의 양수로 바꾸는 과정
    #나머지연산 1번이면 가능
    if answer == 0:            
        
        answer = s[-1] % m[-1]
    
    print(answer)