#두 수의 합이 최소가 되도록 나누기
from sys import stdin

while 1:
    
    A = stdin.readline().rstrip().split()

    if len(A) == 1:
        
        break
    
    else:
        
        n = int(A[0])
        a = A[1:]
        
        #숫자카드를 정렬하고,
        a.sort(reverse = True)

        n2 = n//2
        n1 = n - n2

        a1 = []
        a2 = []
        
        #숫자 카드 개수가 홀수개이면, 한개를 한쪽에 주고
        if n % 2 == 1:
            
            a1.append(a.pop())
        
        one = True
        
        #작은 수부터 차례대로 양쪽에 배분해준다
        while a:
            
            if one:
                
                a1.append(a.pop())
                one = False
            
            else:
                
                a2.append(a.pop())
                one = True
        
        #0이 있는 경우에 대한 예외 처리
        #a1,a2가 작은 수부터 정렬된 상태
        #처음으로 0이 아닌 수를 찾았다면, 맨 앞으로 옮겨주면 된다
        for i in range(len(a1)):
            
            if a1[i] != '0':
                
                a1[0],a1[i] = a1[i],a1[0]
                break
        
        for i in range(len(a2)):
            
            if a2[i] != '0':
                
                a2[0],a2[i] = a2[i],a2[0]
                break
                
        a1 = int(''.join(a1))
        a2 = int(''.join(a2))

        print(a1+a2)