#from sys import setrecursionlimit
#setrecursionlimit(100000)

def farey(a,b,c,d,n):
    
    if b+d >= n+1:
        
        sequence.append((c,d))
    
    elif b+d <= n:

        farey(a,b,a+c,b+d,n)
        farey(a+c,b+d,c,d,n)

n = 4

sequence = [(0,1)]

farey(0,1,1,1,n)

print(sequence)
[(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]