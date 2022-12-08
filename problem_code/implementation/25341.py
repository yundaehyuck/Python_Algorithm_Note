from sys import stdin

n,m,q = map(int,stdin.readline().split())

neural_list = []

#m개의 은닉층 인공신경망을 입력받는다

for _ in range(m):
    
    neural = list(map(int,stdin.readline().split()))

    neural_list.append(neural)

#출력층 인공신경망
final_neural = list(map(int,stdin.readline().split()))

#출력층 인공신경망 마지막 원소는 bias
final_bias = final_neural[-1]

#크기가 n+1인 빈 리스트 초기화
#wk를 구해서 해당 위치에 맞게 넣어줄 것
all_neural_list = [0]*(n+1)

#m개의 출력층 인공신경망을 순회해서
for i in range(m):
    
    c = neural_list[i][0] #가중치 개수
    
    #bias의 총합 bk는 하나의 항으로 계산되므로 계속 누적합 시켜준다
    final_bias += (neural_list[i][-1] * final_neural[i])
    
    #input data가 들어가는 위치를 index로 해서 
    #wk를 누적합 시켜준다
    for j in range(c):
        
        all_neural_list[neural_list[i][1+j]-1] += final_neural[i]*neural_list[i][1+c+j]
    
for _ in range(q):
    
    input_list = list(map(int,stdin.readline().split()))
    
    #bk의 총합 + b를 구해준다.
    final_output = final_bias 
    
    #xwk를 구해준다
    for i in range(n):
        
        final_output += (all_neural_list[i] * input_list[i])
    
    print(final_output) #최종값은 xwk + bk + b