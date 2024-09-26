#n명의 사람이 0~10점 정수 척도 설문조사를 했을때,각 문항마다 평균점수가 소수점 셋째자리까지 버린 상태로 주어지면
#최솟값 n을 구하는 문제
from sys import stdin
from decimal import Decimal


#a/b를 소수점 셋째자리까지 정확하게 구하는 함수
def divide(a,b):
    
    answer = []

    p,r = a//b, a%b

    answer.append(str(p))
    answer.append('.')

    a = r*10

    while len(answer) < 5:

        p,r = a//b, a%b
        answer.append(str(p))
        a = r*10
    
    return float(''.join(answer))

n = int(stdin.readline())

A = []

for _ in range(n):
    
    s = Decimal(stdin.readline())
    A.append(s)

x = 1

#i번째 문항의 점수 합이 v이고 x명 설문조사 했을때
#A[i] <= v/x < A[i] + 0.001
# 위 식을 만족하는 정수 v는 i번째 문항의 설문조사 점수 합이 될 수 있다 

for x in range(1,1001): #소수점 셋째자리까지 주어지기 때문에 아무리 많아야 1000명까지 가능
    
    no = False

    for i in range(n):
        
        v1 = A[i]*Decimal(x)
        v2 = (A[i] + Decimal('0.001'))*Decimal(x) #실수 오차를 방지하기 위해 Decimal을 사용
        
        if int(v1) == v1:
            
            v1 = int(v1)
        
        else:
            
            v1 = int(v1) + 1
        
        if v1 < v2:

            d = divide(v1,x)
            
            if d != float(A[i]):

                no = True
                break
        
        else:
            
            no = True
            break
    
    if no == False:
        
        break

print(x)