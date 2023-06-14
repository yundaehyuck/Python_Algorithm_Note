from sys import stdin

n = int(stdin.readline())

answer = 0

#i = 1부터 시작해서, x와 i의 부등식 하한 상한인 start,end를 구합니다.
i = 1

x = n//i

start = n//(x+1)
end = n//x

while 1:
    
    #현재 x에 대하여 가능한 i의 합을 구합니다.
    k = end*(end+1)//2 - start*(start+1)//2
    
    #k*x를 누적합하고
    answer += k*x
    
    #다음 i로 이동합니다.
    #부등식의 길이인 (end - start)를 더해주면 다음 i로 이동할 수 있습니다.
    i += (end-start)
    
    #현재 i에서 x값을 구해줍니다.
    x = n//i
    
    #x의 최솟값은 1이므로, x가 0이 나오면 반복문을 탈출합니다.
    if x == 0:
        
        break
    
    #현재 x에 대해 i의 부등식 하한,상한을 구해줍니다.
    end = n//x
    start = n//(x+1)

#실질적 약수를 구하기 위해 1의 개수 n-1개,
#1부터 n까지의 합을 제외해줍니다
answer -= (n-1)
answer -= n*(n+1)//2

print(answer % 1000000)