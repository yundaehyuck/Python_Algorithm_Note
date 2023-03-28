from sys import stdin

def parametric_search(city,start,end,m):
    
    while start < end:
        
        #비용이 든 배열 city에서 중간 지점을 찾는다.
        #중간 지점이 "정수 상한액"
        mid = start + (end - start)//2

        total = 0

        #중간 지점 이후로는 정수 상한액 mid값을 더해주고
        #중간 지점 이전에는 해당 액수 c값을 더해주면
        for c in city:
            
            if c > mid:
                
                total += mid
            
            else:
                
                total += c
        
        #mid가 "정수 상한액"일때... 가능한지 아닌지 검사
        #배열 city가 오름차순이므로, 전체 비용이 예산보다 크다면...
        #start ~ mid-1에 정답이 있다
        if total > m:
            
            end = mid
        
        #전체 비용이 예산 이내라면...
        # mid ~ end에 정답이 있다
        else:
            
            start = mid + 1
    
    return start - 1

n = int(stdin.readline())

city = list(map(int,stdin.readline().split()))

m = int(stdin.readline())

city.sort()

print(parametric_search(city,0,city[-1]+1,m))