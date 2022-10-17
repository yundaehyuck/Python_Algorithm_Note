def dfs(num_list,op_list,i,n,result):
    
    global max_v,min_v
    
    ##n-1개의 연산자를 뽑으면 최대, 최소를 갱신
    
    if i == n:
        
        if max_v < result:
            
            max_v = result
        
        if min_v > result:
            
            min_v = result
    
    else:
        
        ##연산자 0,1,2,3에서 뽑고..
        
        for op in range(4):
            
            ##연산자가 아직 남아있다면..
            
            if op_list[op] != 0:
                
                ##그 연산자를 사용하고 counting 1 감소
                
                op_list[op] -= 1

                ##연산 수행
                ##연산 결과를 임시 변수 dresult에 저장하고..

                if op == 0:
                    
                    dresult = result + num_list[i]
                
                elif op == 1:
                    
                    dresult = result - num_list[i]

                elif op == 2:
                    
                    dresult = result * num_list[i]
                
                else:
                    
                    dresult = int(result/num_list[i])

                ##dresult를 재귀에 넣어줘야.. result는 다른곳에 쓰일수 있겠지?
                ##i번째를 결정시키면.. 다음 i+1번째를 결정하러
                
                dfs(num_list,op_list,i+1,n,dresult)
                
                ##재귀 하나가 끝나면.. 연산자 사용한거 복구
                op_list[op] += 1
               

T = int(input())

for tc in range(1,T+1):
    
    n = int(input())

    op_list = list(map(int,input().split()))

    num_list = list(map(int,input().split()))

    max_v = -100000000
    min_v = 100000000
    
    ##숫자리스트, 연산자리스트, 첫번째 숫자 하나는 이미 뽑았고..
    dfs(num_list,op_list,1,n,num_list[0])

    print('#'+str(tc),max_v-min_v)