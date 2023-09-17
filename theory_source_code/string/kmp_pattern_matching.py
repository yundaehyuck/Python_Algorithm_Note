#t에 부분문자열 p가 몇번이나 존재하는가?

#KMP prefix function
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

t = input()
p = input()

#p#t에 대한 pi배열 구하기
pi = prefix_function(p + "#" + t)

n = len(p)
m = len(t)

count = 0
pos = []

#0~m+n이 p#t의 인덱스이고
#t의 시작 위치는 n+1부터이다.
#그러나 p는 2n부터 등장할 수 있다.

#만약 pi[i] = n인 i가 있다면, p의 등장 위치는 i - n + 1이고
#i는 p#t의 인덱스이므로, n+1만큼 이동시켜서 i - n+1 -(n+1) = i-2n부터 등장한다고 해야한다.
#문제에서 1번부터 시작하라고 한다면 i-2n+1이라고 해야

for i in range(2*n, m + n + 1):
    
    if pi[i] == n:
        
        count += 1
        pos.append(i - n + 1 - n)

print(count)
print(*pos)