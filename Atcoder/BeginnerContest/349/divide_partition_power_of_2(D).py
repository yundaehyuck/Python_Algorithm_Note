L,R = map(int,input().split())

division = []

while L < R:
        
    i = 0
    
    #i = 0부터 시작해서 L이 2^(i+1)로 나누어 떨어지면서..
    #다음 점 (L//(2^(i+1)+1)*(2^(i+1))이 R 이하라면...
    #i를 1 증가시킨다..
    #이렇게 R 이내에서 조건을 만족하는 가장 먼 점을 찾는다
    while L % (2**(i+1)) == 0 and (L//(2**(i+1))+1)*(2**(i+1)) <= R:
      
        i += 1
    
    #반복문이 끝나면 해당 i를 찾았고, 구간을 갱신
    j = L//(2**i)
    max_j = (j+1)*(2**i)
    division.append((L,max_j))
    L = max_j

print(len(division))
for a,b in division:
    
    print(a,b)