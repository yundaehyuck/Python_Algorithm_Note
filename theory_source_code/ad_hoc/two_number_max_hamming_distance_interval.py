#a이상 b이하의 정수들 중 해밍거리가 가장 큰 두 정수 x,y를 구하기

a,b = map(int,input().split())

#a,b를 이진수로 나타내고
a = bin(a)[2:]
b = bin(b)[2:]

#이진수의 길이를 서로 맞춰주기 위해 a에 0을 앞에 채워넣음
a = '0'*(len(b) - len(a)) + a

X = []
Y = []

#이제 a,b를 상위비트부터 차례대로 살펴봐서
#서로 다른 두 비트가 발생한다면
#X = 11111....0XXXXXXX
#Y = 11111....1YYYYYYY 처럼 생길 것
#그러면 0 이후로는 1을 채우고, 1 이후로는 0을 채우면
#11111...01111111
#11111...10000000이면 해밍거리가 최대가 된다
#특히 X는 A이상,B이하가 되며 Y는 B이하, A이상이 된다는 점도 주목
for i in range(len(a)):
    
    if a[i] != b[i]:
        
        X.append('1')
        Y.append('0')
        break
    
    else:
        
        X.append(a[i])
        Y.append(a[i])

X = ''.join(X)
Y = ''.join(Y)

X += '0'*(len(a)-1-i)
Y += '1'*(len(a)-1-i)

print(int(X,2),int(Y,2))