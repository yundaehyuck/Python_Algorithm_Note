from sys import stdin

def prefix_function(s):
    
    n = len(s)

    pi = [0]*n

    for i in range(1,n):
        
        j = pi[i-1]

        while j > 0 and s[i] != s[j]:
            
            j = pi[j-1]
        
        if s[i] == s[j]:
            
            j += 1
        
        pi[i] = j
    
    return pi

n = int(stdin.readline())

for _ in range(n):
    
    w = stdin.readline().rstrip()
    t = stdin.readline().rstrip()

    count = 0

    pi = prefix_function(w + "#" + t)

    n = len(w)
    m = len(t)

    for i in range(2*n,n+m+1):
        
        if pi[i] == n:
            
            count += 1
    
    print(count)