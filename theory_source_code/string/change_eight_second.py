#eight > second

from sys import stdin

s = stdin.readline().rstrip()

second = []

#앞에서부터 8진수 하나씩 읽어서
#3자리 2진수로 바꿔주고
#차례대로 이어붙여준다

for c in s:
    
    c = int(c)

    num = 0

    sub = ''

    while c > 0:
        
        q,r = divmod(c,2)
        
        sub += str(r)

        num += 1

        c = q
    
    while num != 3:
        
        sub += '0'
        num += 1
    
    second.append(sub[::-1])


if s != '0':
    
    #리스트에 넣어서 마지막에 문자열로 바꿔줘야 시간복잡도 감소
    second = ''.join(second)

    if second[0] == '0' and second[1] == '0':
        print(second[2:])
    
    elif second[0] == '0' and second[1] != '0':
        
        print(second[1:])
    
    else:
        
        print(second)

elif s == '0':

    print('0')