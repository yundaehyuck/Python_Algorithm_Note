#A/B가 기약분수가 아닐때, A,B의 최대공약수 구하기
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

#A/B = p_k/q_k이므로, A = p_k*g, B = q_k*g이다.
#g = A//p[-1] = B//q[-1]

a = 12
b = 8

p,q = convergent(continued_fraction(a,b))

print(a//p[-1])
print(b//q[-1])