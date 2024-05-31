#정수 n은 d의 배수이면서 자릿수 합도 d의 배수이다.
#그러한 정수 n은 d를 d번 이어 붙인 수가 해당될 수 있다.

#dddddddddddddddddddd = d*10^n1+d*10^n2+...+d
#자릿수 합은 d*d
d = input()

answer = []

for _ in range(int(d)):
    
    answer.append(d)

print(''.join(answer))