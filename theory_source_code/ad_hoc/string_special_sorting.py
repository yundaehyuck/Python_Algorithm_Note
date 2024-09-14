#문자열을 a b k d e g h i l m n ng o p r s t u w y 기준으로 정렬하기

# a b k d e g h i l m n ng o p r s t u w y
# a b c d e f g h i j k  l m n o p q r s t 에 매핑하면 중복이 안됨

from sys import stdin

n = int(stdin.readline())

change = {'k':'c', 'g':'f','h':'g','i':'h',
          'l':'i', 'm':'j', 'n':'k',
          'o':'m', 'p':'n', 'r':'o', 's':'p',
          't':'q', 'u':'r', 'w':'s', 'y':'t'}

answer = []

for _ in range(n):
    
    s = stdin.readline().rstrip()
    
    #먼저 ng를 L로 바꿔주고
    ss = list(s.replace('ng','L'))
    
    #나머지 바꿔야하는 문자를 매핑되는 다른 문자로 하나씩 바꿔준 다음
    for k in change:
        
        for i in range(len(ss)):
            
            if ss[i] == k:
                
                ss[i] = change[k]
    
    #마지막에 L은 소문자 l로 바꿔주고
    for i in range(len(ss)):
        
        if ss[i] == 'L':
            
            ss[i] = 'l'
    
    #바뀐 문자열과 원본 문자열을 둔 다음
    answer.append((ss,s))

#정렬하고 대응하는 원본 문자열을 차례대로 출력
answer.sort()

for i in range(len(answer)):
    
    print(answer[i][1])