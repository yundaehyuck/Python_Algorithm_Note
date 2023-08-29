from math import pi,sin,cos

def bit_reverse(f,n):

    j = 0

    for i in range(1,n):
    
        bit = n >> 1

        while j >= bit:
            
            j -= bit
            bit >>= 1
        
        j += bit

        if i < j:
            
            f[i],f[j] = f[j],f[i]


def dft(f,inverse = False):
    
    n = len(f)
    
    bit_reverse(f,n)
    
    roots = [0]*(n//2)

    if inverse == False:

        for i in range(n//2):
        
            roots[i] = complex(cos(2*i*pi/n),sin(2*i*pi/n))
    
    else:
        
        for i in range(n//2):
            
            roots[i] = complex(cos(2*i*pi/n),-sin(2*i*pi/n))
    
    i = 1

    while i <= n:
        
        step = n//i

        for j in range(0,n,i):
            
            for k in range(i//2):
                
                u = f[j+k]
                v = f[j+k+i//2] * roots[step*k]

                f[j+k] = u+v
                f[j+k+i//2] = u - v
        
        i *= 2