from sys import stdin

def z_function(s):
    
    n = len(s)

    z = [0]*n

    z[0] = n

    left = 0
    right = 0

    for i in range(1,n):
        
        if i < right:
            
            z[i] = min(z[i-left], right-i)

        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            
            z[i] += 1
        
        if i+z[i] > right:
            
            left = i
            right = i+z[i]
    
    return z

T = int(stdin.readline())

for _ in range(T):
    
    p = stdin.readline().rstrip()
    s = stdin.readline().rstrip()

    z = z_function(p+'#'+s)

    count = 0

    for i in range(len(s)):
        
        if z[i+len(p)+1] == len(p):
            
            count += 1
    
    print(count)