#문자열에서 일부를 골라 WHEE....를 만드는 방법의 수
n = int(input())

s = input()

w = 0
h = 0
e = 0

answer = 0

mod = 10**9+7

for i in range(n):
    
    if s[i] == 'W':
        
        w += 1
    
    elif s[i] == 'H':
        
        h += w #WH의 개수
    
    elif s[i] == 'E':
        
        #원래 WHEE...의 개수(answer)에 E를 붙이면 그것도 조건을 만족하므로 그만큼 늘어나므로...
        #그리고 WHE의 개수 e에 E를 붙이면 WHEE가 되고 이것도 조건을 만족하므로..
        #처음으로 E를 만나면 원래 answer개에 answer+e개가 더 늘어나게 된다
        #그리고 WH의 개수 h에 E를 붙이면 WHE가 되므로, e에 h만큼 누적해준다
        answer += (answer+e)
        answer %= mod
        e += h

print(answer)