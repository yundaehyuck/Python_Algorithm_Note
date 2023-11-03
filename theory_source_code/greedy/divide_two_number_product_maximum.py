#두 수의 곱이 최대가 되도록 나누기
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    
    s = list(stdin.readline().rstrip())
    
    #6은 9로 바꿔준다
    for i in range(len(s)):
        
        if s[i] == '6':
            
            s[i] = '9'
    
    #큰 수부터 사용하도록 내림차순 정렬
    s.sort(reverse = True)
    
    #최소한 하나의 수는 사용해야하므로, 각 수에 하나씩 분배
    n1 = [s[0]]
    n2 = [s[1]]
    
    #두 수의 차이가 작을수록 두 수의 곱이 커지므로,
    #매번 두 수를 비교해서 첫번째 수가 더 크다면, 두번째 수에 숫자를 붙여주고
    #두번째 수가 더 크다면, 첫번째 수에 숫자를 붙여줘서 두 수의 차이를 매번 줄여준다
    for i in range(2,len(s)):
        
        k1 = int(''.join(n1))
        k2 = int(''.join(n2))

        if k1 < k2:
            
            n1.append(s[i])
        
        else:
            
            n2.append(s[i])
    
    n1 = int(''.join(n1))
    n2 = int(''.join(n2))

    print(n1*n2)