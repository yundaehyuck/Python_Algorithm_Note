#연분수의 사칙연산
#연분수 > 유리수 > 사칙연산(합,차,곱,나눗셈) > 기약분수 > 연분수

#연분수를 유리수로 바꾸는 함수
#p_k = a_k*p_(k-1) + p_(k-2)
#q_k = a_k*q_(k-1) + q_(k-2)

#p_(-1) = 1, p_(-2) = 0
#q_(-1) = 0, q_(-2) = 1
def convergent(f):
    
    p = [0,1]
    q = [1,0]

    for a in f:
        
        p.append(p[-1]*a + p[-2])
        q.append(q[-1]*a + q[-2])
    
    return p[-1],q[-1]

#유리수 p/q를 연분수로 나타내는 함수
#p,q는 서로소
def continued_fraction(p,q):
    
    f = []

    while q:
        
        f.append(p//q)
        p,q = q,p%q
    
    return f

#a,b의 최대공약수를 구하는 유클리드 알고리즘
def gcd(a,b):
    
    while b != 0:
        
        a,b = b,a%b
    
    return a

#유리수 p/q를 기약분수로 나타내는 함수
#p,q의 최대공약수 g에 대하여 p = gr, q = gk, r,k는 서로소
#p//g, q//g가 기약분수
def reduced(p,q):
    
    g = gcd(p,q)

    return p//g, q//g

t = 1

while 1:
    
    n1,n2 = map(int,input().split())

    if n1 == 0 and n2 == 0:
        
        break
    
    else:
        
        #연분수
        f1 = list(map(int,input().split()))
        f2 = list(map(int,input().split()))
        
        #연분수 > 유리수
        p1,q1 = convergent(f1)
        p2,q2 = convergent(f2)
        
        #유리수 사칙연산
        #> 기약분수
        #> 연분수
        add = continued_fraction(*reduced(p1*q2+p2*q1,q1*q2))
        minus = continued_fraction(*reduced(p1*q2-p2*q1,q1*q2))
        multiply = continued_fraction(*reduced(p1*p2,q1*q2))
        divide = continued_fraction(*reduced(p1*q2,q1*p2))

        print(f'Case {t}:')
        print(' '.join(map(str,add)))
        print(' '.join(map(str,minus)))
        print(' '.join(map(str,multiply)))
        print(' '.join(map(str,divide)))
        t += 1