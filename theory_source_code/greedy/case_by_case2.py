#case by case greedy

n = int(input())

bulb = list(input())

change = {'R':'G','G':'B','B':'R'}

bulb2 = bulb[:]

answer = []

#첫번째 전구의 색을 R,G,B중 하나로 고정시키고
#두번째, 세번째, ... 모두 바꿔본 다음
#전부 같은지 검사해준다
for init in ['R','G','B']:

    count = 0
    
    #첫번째 전구의 색을 고정시키기
    while bulb2[0] != init:
        
        bulb2[0] = change[bulb2[0]]
        bulb2[1] = change[bulb2[1]]
        bulb2[2] = change[bulb2[2]]

        count += 1

    i = 1
    
    #두번째 전구부터 색을 첫번째 전구와 동일하게 바꿔본다
    while i <= n-3:

        for _ in range(3):
            
            if bulb2[i] == init: #바꾸지 않아도 처음부터 같을 수 있음
                
                break
                
            bulb2[i] = change[bulb2[i]]
            bulb2[i+1] = change[bulb2[i+1]]
            bulb2[i+2] = change[bulb2[i+2]]

            count += 1
        
        i += 1
    
    #반복문을 탈출하면, -1, -2번 인덱스의 값이 같은지 다른지만 검사해주면 됨
    #하나라도 다르다면, 전부 같은 색으로 바꿀 수 없다
    if bulb2[-1] != init or bulb2[-2] != init:
        
        count = -1

    answer.append(count)
    bulb2 = bulb[:]

if answer[0] == -1 and answer[1] == -1 and answer[2] == -1:
    
    print(-1)

else:
    
    count = 10000000000000000000000000

    for i in range(3):
        
        if answer[i] == -1:
            
            continue
        
        else:
            
            if answer[i] < count:
                
                count = answer[i]
    
    print(count)