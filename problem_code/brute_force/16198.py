from sys import stdin

def dfs(e,w,w_list):
    
    global max_e
    
    #남은 원소가 2개이면..
    #최댓값 갱신
    if w == 2:
        
        if max_e < e:
            
            max_e = e
    
    else:
        
        #1번부터 w-2번까지 모두 골라본다
        for k in range(1,w-1):
            
            #k번을 골랐을때, k-1번 원소랑 k+1번 원소의 곱을 누적합
            de = e + (w_list[k-1]*w_list[k+1])
            
            #원본은 남겨두고
            w_list_copy = w_list[:]
            
            #k번 원소를 삭제하고
            del w_list_copy[k]
            
            #재귀경로를 생성
            dfs(de,w-1,w_list_copy)

n = int(stdin.readline())

w_list = list(map(int,stdin.readline().split()))

max_e = 0

dfs(0,n,w_list)

print(max_e)