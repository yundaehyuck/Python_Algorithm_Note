def continued_fraction(p,q):
    
    f = []

    while q != 0:
        
        f.append(p//q)
        p,q = q,p%q
    
    return f

def convergent(f):
    
    p = [0,1]
    q = [1,0]

    for a in f:
        
        p.append(a*p[-1]+p[-2])
        q.append(a*q[-1]+q[-2])
    
    return p,q

#ax+by = c의 특수해를 구하는 함수
def diophantine(a,b,c):
    
    #a/b의 연분수 표현 p,q를 구한다
    p,q = convergent(continued_fraction(a,b))
    
    #a = pk * g, b = qk * g이므로, g = a//pk
    g = a // p[-1]
    
    #c가 g = gcd(a,b)로 나누어 떨어지지 않으면 정수해가 존재하지 않는다
    if c % g == 0:
        
        c //= g
    
    else:
        
        return -1,-1,-1
    
    #(-1)^{k+1}의 부호를 정한다
    #k+1 = len(p)이므로, len(p)가 홀수이면 -1
    #len(p)가 짝수이면 1
    t = -1 if len(p) % 2 else 1
    
    #x = (-1)^(k+1)*C*q_(k-1)/g, y = -1*(-1)^(k+1)*C*p_(k-1)/g    
    #여기서 p[-1] = p_k이고 p[-2] = p_k-1
    x = t*c*q[-2]
    y = -t*c*p[-2]
    
    return g,x,y #a,b의 최대공약수, 특수해 x,y