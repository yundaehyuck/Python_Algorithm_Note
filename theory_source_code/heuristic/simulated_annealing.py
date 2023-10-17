#담금질 기법을 이용한 최소 외접원 문제
from sys import stdin

#두 점 사이 거리
def distance(x,y):
    
    return (x[0]-y[0])**2 + (x[1] - y[1])**2

#담금질 기법
#f(x,y) = max((x-a1)^2+(y-b1)^2, ... , (x-an)^2+(y-bn)^2)을 최소화하는 x,y를 찾는 문제
#f = max(x^2,y^2)은 global optimal만 존재하는 함수
def simulated_annealing(x,y,n):
    
    #최소 외접원의 중점 초기값 설정
    X = sum(x)/n
    Y = sum(y)/n
    
    #global optimal을 찾을 수 있는 적절한 값을 설정해야함
    #temperature가 너무 크면 빠르게 global optimal로 다가가더라도, exploding 가능성이 있고
    #너무 작으면 굉장히 많은 시행횟수가 필요하다.
    temperature = 0.2 #온도(learning rate)
    
    #정확히 정답을 찾을려면 최대한 많은 시행횟수를 하는게 좋을 것이다
    epochs = 50000 #담금질 시행 횟수(epoch)
    
    #매 시행마다 모든 점들과 중점 (X,Y)사이 거리를 조사해서, 최댓값을 찾는다
    for epoch in range(epochs):
        
        max_dist = 0

        max_ind = -1

        for j in range(n):
            
            dist = distance((X,Y),(x[j],y[j]))

            if max_dist < dist:
                
                max_dist = dist
                max_ind = j
        
        #grdient descent방법에 의해 x < x - learning_rate*gradient로 갱신
        #혹은, (x[max_ind],y[max_ind])와 (X,Y) 사이 learning_rate 비율로 분할하는 점으로 갱신해도 답이 나오긴 한다
        #X = x[max_ind]*learning_rate + X*(1-learning_rate)
        #Y = y[max_ind]*learning_rate + Y*(1-learning_rate)
        
        X = X -temperature * 2*(X-x[max_ind]) 
        Y = Y -temperature * 2*(Y-y[max_ind])
        
        #온도 감률 0.95~0.9999사이 값중 하나를 매 시행마다 곱하여, 온도를 변화시키며 담금질 시행
        temperature *= 0.9995
    
    #마지막 시행에서 찾은 max_dist값이 최소 외접원의 반지름의 제곱이다 
    return 2*(max_dist**(1/2))
    
n = int(stdin.readline())

x = []
y = []

for _ in range(n):
    
    a,b = map(int,stdin.readline().split())
    
    x.append(a)
    y.append(b)

print(f'{simulated_annealing(x,y,n):.2f}')