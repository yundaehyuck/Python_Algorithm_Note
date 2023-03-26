from sys import stdin

s = stdin.readline().rstrip()

n = len(s)

eight = []

three = []

k = 0

#뒤에서부터 3자리씩 읽어서,
#각각을 10진수로 만들면, 해당자리의 8진수가 된다.

#전부 차례대로 이어 붙여주면 8진수로 변환된다

for i in range(n-1,-1,-1):
    
    three.append(s[i])

    k += 1

    if k == 3:
        
        summation = 0

        for i in range(2,-1,-1):
            
            summation += int(three[i])*(2**i)
        
        eight.append(str(summation))

        k = 0
        three = []

#맨 앞에서 3자리 이진수가 안된다면, 앞에 0을 붙여서 3자리로 만들고
#10진수로 변환해주면 그것이 맨 앞자리의 8진수
if k != 0:
    
    while k != 3:
        
        three.append('0')
        k += 1

    summation = 0

    for i in range(2,-1,-1):
        
        summation += int(three[i])*(2**i)    
    
    eight.append(str(summation))

#리스트에 모두 부분문자열을 넣고, 마지막에 전체 문자열로 만들어줘야 시간복잡도 감소

print(''.join(eight[::-1]))