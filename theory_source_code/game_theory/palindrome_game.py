#팰린드롬인 정수 개수만큼 돌을 가져갈 때 이기는 방법
#첫 돌이 10의 배수이면 선공이 지고
#첫 돌이 10의 배수가 아니면, 1~9중 하나를 가져가 돌의 개수가 
#항상 10의 배수인 상태로 넘겨주면 선공이 이길 수 있다 
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    
    s = stdin.readline().rstrip()

    if s[-1] == '0':
        
        print('E')
    
    else:
        
        print('B')