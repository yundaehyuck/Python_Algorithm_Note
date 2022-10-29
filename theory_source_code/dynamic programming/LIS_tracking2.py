#이진 탐색으로 최장 증가 부분수열 역추적하기

##배열에서 읽어들인 숫자보다 크거나 같은, 최초의 위치를 찾는다

def lower_bound(array,target,start,end):
    
    while start < end:
        
        mid = (start+end)//2

        if array[mid] >= target:
            
            end = mid
        
        else:
            
            start = mid + 1
    
    return end


s = [8,2,4,3,6,11,7,10,14,5]

n = len(s)

c = [1000000000000000000000000000000000]*n #매우 큰 값으로 c배열 초기화

p = [0]*n #c배열에 들어간 원소의 위치를 저장할 배열

LIS = 0 #현재 가장 긴 증가 부분수열의 길이

for i in range(n):

    ##num보다 크거나 같은 값 중에서 가장 작은 위치를 찾는다

    loc = lower_bound(c,s[i],0,n)
    
    #찾은 위치가 현재 가장 긴 증가 부분수열의 길이와 같다
    if loc == LIS:
        
        c[LIS] = s[i] ##그 위치에 숫자를 넣고

        p[i] = LIS #i번째 숫자가 c배열에 들어간 위치를 저장

        LIS += 1
    
    else: #찾은 위치가 현재 가장 긴 증가 부분수열의 길이와 다르다면..?
        
        c[loc] = s[i] #그냥 그 위치에 넣고,

        p[i] = loc #p배열에도 그 숫자의 위치를 넣어준다.

##역추적

lis_list = [0]*LIS

target = LIS-1

for i in range(n-1,-1,-1): #p배열을 뒤에서부터 읽어들인다..
    
    if p[i] == target:
        
        lis_list[target] = s[i]

        target -= 1
    
    if target == -1:
        
        break

print(lis_list)
"""
[2, 3, 6, 7, 10, 14]
"""