from sys import stdin

s = list(stdin.readline().rstrip())
t = list(stdin.readline().rstrip())

a = len(s)
b = len(t)

answer = 0

while b != a:
    
    #마지막 문자가 A라면, A를 제거
    if t[-1] == 'A':
        
        t.pop()
        b -= 1
    
    #마지막 문자가 B라면 B를 제거하고 뒤집어준다.
    else:
        
        t.pop()
        b -= 1
        t = t[::-1]
    
    #길이가 서로 같아진다면 두 문자열이 같은지를 체크해본다.
    if a == b:
        
        if t == s:
            
            answer = 1
        
        else:
            
            answer = 0
        break

print(answer)