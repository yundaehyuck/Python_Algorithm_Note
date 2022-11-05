from sys import stdin

#시험장 수
n = int(stdin.readline())

#응시자 수
student_list = list(map(int,stdin.readline().split()))

#총감독관, 부감독관 감시 수
b,c = map(int,stdin.readline().split())

ans = 0

#응시자 수를 순회해서,
for s in student_list:
    
    #총 감독관 1명을 필수로 배치하고
    ans += 1
        
    s -= b
    
    #1명을 배치하더라도, 응시자 수가 남아있다면,
    if s > 0:
        
        #남은 응시자 수를 부감독관이 감시할 수 있는 수로 나눠줘서,
        k,r = divmod(s,c)
        
        #나머지가 양수라면, 부감독관 1명을 더 배치하고
        if r > 0:
            
            ans += (k+1)
        
        #나머지가 0이라면 몫만큼 배치하면 된다
        else:
            
            ans += k

print(ans)