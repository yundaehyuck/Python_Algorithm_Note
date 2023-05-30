#boj 2437
from sys import stdin

n = int(stdin.readline())

#수열을 오름차순으로 정렬
s = sorted(map(int,stdin.readline().split()))

#처음에 0~0까지 만들 수 있다
sum_value = 0

#작은 수부터 꺼내서,
for num in s:
    
    #나온 수가 만들 수 있는 수의 최댓값+1보다 크다면, 
    #만들 수 있는 수의 최댓값+1부터 num-1까지는 만들 수 없는 수이다.
    if sum_value+1 < num:
        
        break
    
    #만들 수 있는 수의 최댓값+1이 num이상이라면,
    #그러면 나는 0~sum_value+num까지 이제 만들 수 있게 되었다.
    sum_value += num

#반복문을 탈출했을때, sum_value+1은 만들 수 없는 수의 최솟값
print(sum_value+1)