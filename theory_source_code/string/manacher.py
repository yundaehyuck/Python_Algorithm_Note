#주어진 문자열
temp = "bananac"

#주어진 문자열 내 문자 사이사이 #을 넣는다
#join을 이용해 시간복잡도를 줄인다
input_str = "#" + "#".join(temp) + "#"

#manacher algorithm
n = len(input_str) #n은 변형된 문자열의 길이

#A: i번지를 중심으로 하는 홀수 길이의 palindrome중 가장 긴 palindrome의 반지름 길이
#즉, [I-A[i], i+A[i]]가 i를 중심으로 하는 최장 palindrome

A = [0]*n
r = -1
p = -1

#r: j < i를 만족하는 j중 max(j+A[j])
#p: max(j+A[j])가 되는 j의 값

for i in range(n):
    
    #만약 r이 i보다 작다면... 줄일 수 있는 부분이 없어서 A[i] = 0부터
    if r < i:
        
        A[i] = 0
    
    #r이 i보다 같거나 크다면, i를 p로부터 대칭시킨 ii에 대하여..
    #이미 계산된 A[ii]를 이용해
    #i를 중심으로 뻗어나갈 수 있는 적절한 초기값을 O(1)에 설정

    else:
        
        ii = 2*p-i
        A[i] = min(r - i, A[ii])
    
    #i를 중심으로 최대로 뻗어나간다
    while i-A[i]-1 >= 0 and i+A[i]+1 < n and input_str[i-A[i]-1] == input_str[i+A[i]+1]:
        
        A[i] += 1
    
    #i+A[i]중 최대가 되도록, r,p를 갱신
    #r은 지금까지 구한 i+A[i]중 최댓값, p는 그 때의 i
    if i+A[i] > r:
        
        r,p = i+A[i],i

#최장 palindrome의 길이 계산
answer = 0
for i in range(n):
    
    answer = max(answer,2*A[i]+1)

#처음 주어진 문자열에서 #을 제외한 부분의 길이가 실제 답이 된다.
print(answer//2)