from sys import stdin

def permutation(i,n,r,inequal_list):
    
    global max_value,min_value
    
    if i == r:
        
        num_value = p[0] #첫 수를 먼저 이어 붙이고
        find = True #조건을 만족시키는 수를 찾았는지 flag
        
        #inequal_list와 p를 동시에 순회
        for inequal,num in zip(inequal_list,p[1:]):
            
            if inequal == '>':
                 
                 #num_value의 마지막 원소와 p의 원소를 비교
                if num_value[-1] > num:
                    
                    num_value += num
                
                else:
                    #조건에 안맞으면 바로 break시킴
                    find = False
                    break
            
            else:
                
                if num_value[-1] < num:
                    
                    num_value += num
                
                else:
                    find = False
                    break
        
        #찾았으면 최댓값, 최솟값을 갱신
        if find == True:
            
            if num_value > max_value:
                
                max_value = num_value
            
            if num_value < min_value:
                
                min_value = num_value

    else:
        
        for j in range(n):
            
            if used[j] == 0:
                
                used[j] = 1

                p[i] = num_list[j]

                permutation(i+1,n,r,inequal_list)

                used[j] = 0

k = int(stdin.readline())

#모든 수는 str()로 받자
num_list = [str(i) for i in range(10)]

inequal_list = stdin.readline().rstrip().split()

p = [0]*(k+1)

used = [0]*10

#max_value와 min_value 초기화
max_value = str(0)
min_value ='9'*(k+1)

permutation(0,10,k+1,inequal_list)

print(max_value)
print(min_value)