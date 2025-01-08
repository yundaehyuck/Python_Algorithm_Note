#x+y = x|y를 만족하는 k번째 작은 자연수 y를 찾는 문제
#x,y의 같은 위치의 비트가 서로 0,0이거나 0,1이거나 1,0이어야한다 
x,k = map(int,input().split())

k = bin(k)[2:]

x = list(bin(x)[2:][::-1])

j = len(k)-1

#x를 2진수로 바꾸고 1인 부분은 모두 0으로 바꾼다
#0인 부분에는 k를 그대로 집어넣는다
for i in range(len(x)):
    
    if x[i] == '0':
        
        if j >= 0:
            
            x[i] = k[j]
            j -= 1
    
    else:
        
        x[i] = '0'

#k를 아직 다 집어넣지 못했다면 x의 뒷부분에 넣어야하므로...
while j >= 0:
    
    x.append(k[j])
    j -= 1

x = ''.join(x[::-1])

print(int(x,2))