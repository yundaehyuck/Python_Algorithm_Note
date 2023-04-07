from sys import stdin

n,l = map(int,stdin.readline().split())

A = list(map(int,input().split()))

answer = 0

#최초 알코올 섭취후 129이상 138이하인지 검사
if A[0] >= 129 and A[0] <= 138:
    
    answer += 1

blood = [0]*n

#알코올 누적합 배열
blood[0] = A[0]

t = 0 #섭취 몇시간째
s = 0 #몇번 알코올이 빠졌는지,

for i in range(n-1):

    blood[i+1] = blood[i]+A[i+1]

    t += 1
    
    #지속시간 L시간 이후에는, 0번원소부터 알코올이 빠져나감
    if t >= l:

        blood[i+1] -= A[s]
        s += 1
    
    #현재 시점에 129이상, 138이하인지 검사해서 지속시간 갱신
    if blood[i+1] >= 129 and blood[i+1] <= 138:
        
        answer += 1
        
print(answer)