#greedy - case by case
n = int(input())

A = list(map(int,input()))
B = list(map(int,input()))

switch = {0:1,1:0}

#0번을 누를 수 없는 경우
count1 = 0

C = A[:]

#1번부터 n-2번까지 순회하여 누를 수 있는지 없는지 체크
#i-1번이 목표로 하는 상태와 다르다면 i+1번부터는 바꿀 수 없으므로 i번을 눌러야한다.
for i in range(1,n-1):
    
    if C[i-1] != B[i-1]:
        
        count1 += 1
        
        C[i-1] = switch[C[i-1]]
        C[i] = switch[C[i]]
        C[i+1] = switch[C[i+1]]
    

#마지막 n-1번을 눌러야하는가 말아야하는가
#n-2번이 다르고, n-1번도 다르다면 n-1번을 눌러서 둘 다 바꿔줘야한다
if C[n-2] != B[n-2] and C[n-1] != B[n-1]:
    
    count1 += 1

#n-2번이나 n-1번 둘중 하나라도 서로 같다면, 눌러도 동일하게 바꿀 수 없으므로 불가능한 경우
elif (C[n-2] == B[n-2] and C[n-1] != B[n-1]) or (C[n-2] != B[n-2] and C[n-1] == B[n-1]):
    
    count1 = -1


#0번을 반드시 누른 경우
count2 = 1

C = A[:]

C[0] = switch[C[0]]
C[1] = switch[C[1]]

#1번부터 n-2번까지 순회하여 누를 수 있는지 없는지 체크
#i-1번이 목표로 하는 상태와 다르다면 i+1번부터는 바꿀 수 없으므로 i번을 눌러야한다.
for i in range(1,n-1):
    
    if C[i-1] != B[i-1]:
        
        C[i-1] = switch[C[i-1]]
        C[i] = switch[C[i]]
        C[i+1] = switch[C[i+1]]

        count2 += 1

#마지막 n-1번을 눌러야하는가 말아야하는가
#n-2번이 다르고, n-1번도 다르다면 n-1번을 눌러서 둘 다 바꿔줘야한다
if C[n-2] != B[n-2] and C[n-1] != B[n-1]:
    
    count2 += 1

#n-2번이나 n-1번 둘중 하나라도 서로 같다면, 눌러도 동일하게 바꿀 수 없으므로 불가능한 경우
elif (C[n-2] == B[n-2] and C[n-1] != B[n-1]) or (C[n-2] != B[n-2] and C[n-1] == B[n-1]):
    
    count2 = -1
    

#둘 다 불가능하다면, 바꿀 수 없는 경우
if count1 == -1 and count2 == -1:
    
    print(-1)

#둘 중 하나라도 가능하다면 최솟값이 정답
elif count1 == -1 and count2 != -1:
    
    print(count2)

elif count1 != -1 and count2 == -1:
    
    print(count1)

else:
    
    if count1 > count2:
        
        print(count2)
    
    else:
        
        print(count1)