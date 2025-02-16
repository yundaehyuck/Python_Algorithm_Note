#가장 긴 연속하는 올바른 괄호 부분문자열의 길이

n = int(input())

A = list(input())

#스택에 [-1]로 초기화
stack = [-1]

answer = 0

#(이 들어오면 현재 인덱스 넣고
#)이 들어오면, 스택에서 원소 하나 뺀다음
#스택이 비어있다면 현재 인덱스를 넣고
#스택이 비어있지 않다면, (현재 인덱스 - 스택의 마지막 인덱스)로 길이를 갱신
for i in range(n):
    
    if A[i] == '(':
        
        stack.append(i)
    
    else:
        
        s = stack.pop()

        if len(stack) == 0:
            
            stack.append(i)
        
        else:
            
            if answer < i-stack[-1]:
                
                answer = i-stack[-1]

print(answer)