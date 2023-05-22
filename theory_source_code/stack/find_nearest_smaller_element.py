#특정 수보다 작으면서 가장 가까운 위치의 인덱스를 찾는 알고리즘

n = int(input())
A = list(map(int,input().split()))

right_side = []
left_side = []

stack = []
len_s = 0

#왼쪽에서 더 작은 원소를 찾는 과정
#A를 왼쪽부터 차례대로 순회함
for i in range(n):
    
    #스택에 원소가 존재하지 않을때
    if len_s == 0:
        
        #가까운 원소가 존재하지 않는다
        left_side.append(-1)
        
        #현재 원소의 인덱스를 넣고, 스택의 길이 + 1
        stack.append(i)
        len_s += 1
    
    #스택에 원소가 존재하는 경우
    else:
        
        #스택에 원소가 존재하면서,
        #스택의 맨 위에 있는 원소가 현재 지정된 A의 i번째 원소보다 크거나 같을때,
        while (len_s != 0 and A[i] <= A[stack[-1]]):
            
            #스택에서 계속해서 원소를 제거한다
            stack.pop()
            len_s -= 1
        
        #반복문이 끝나고, 스택의 길이가 0이면,
        if len_s == 0:
            
            #A의 i번째 원소보다 작은 원소는 왼쪽에 존재하지 않는다
            left_side.append(-1)
        
        #스택에 원소가 존재한다면,
        #스택의 맨 위 원소는 A의 i번째 원소보다 작으면서 위치상으로 가장 가깝다
        else:
            
            left_side.append(stack[-1])
        
        #현재 i번째 원소를 스택에 넣어주고, 다음 i+1번째 원소를 검사하러 
        stack.append(i)
        len_s += 1

stack = []
len_s = 0

#오른쪽에서 더 작은 원소의 인덱스를 찾는 과정
#오른쪽에서 순회를 시작
for i in range(n-1,-1,-1):

    #스택에 원소가 비어있다면,
    if len_s == 0:
        
        #현재 i번째 원소보다 오른쪽에서 더 작은 원소는 존재하지 않는다 
        right_side.append(-1)
        
        #결과에 원소를 담으면, 스택에 현재 원소의 인덱스를 담고
        stack.append(i)
        len_s += 1
    
    #스택에 원소가 존재한다면,
    else:
        
        #스택의 길이가 0이 아니면서,
        #스택의 맨 위 원소가 현재 i번째 원소보다 크거나 같다면,
        #스택의 맨 위 원소를 계속해서 제거한다
        while (len_s != 0 and A[i] <= A[stack[-1]]):
            
            stack.pop()
            len_s -= 1
        
        #반복문이 끝났을때, 스택에 원소가 존재하지 않는다면
        if len_s == 0:
            
            #결과에 -1을 넣어주고
            right_side.append(-1)
        
        #반복문이 끝나더라도 스택에 원소가 남아있다면
        else:
            
            #스택의 마지막 원소는 현재 i번째 원소보다 더 작으면서 
            #오른쪽에서 가장 가까운 원소이다.
            right_side.append(stack[-1])
        
        #결과를 담으면 스택에 현재 i번째 원소를 담는다
        stack.append(i)
        len_s += 1

#현재 위치 i와 left,right사이 거리를 계산하고, 
#최종 결과, 왼쪽 오른쪽에서 가장 가까운 원소의 위치를 찾는다.

result = []

for i in range(n):
    
    #right_side에는 역순으로 담겨있으니, 역으로 접근해야한다는 점에 주의해야한다
    if left_side[i] == -1 and right_side[n-i-1] == -1:
        
        result.append(-1)
    
    elif left_side[i] == -1 and right_side[n-i-1] != -1:
        
        result.append(right_side[n-i-1])
    
    elif left_side[i] != -1 and right_side[n-i-1] == -1:
        
        result.append(left_side[i])
    
    else:

        a = i - left_side[i]
        b = right_side[n-i-1] - i

        if a > b:
            
            result.append(right_side[n-i-1])
        
        else:
            
            result.append(left_side[i])

print(*result)
7
3 1 2 10 5 6 4
1 -1 1 2 2 4 2