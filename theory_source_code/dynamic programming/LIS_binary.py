#이진탐색으로 최장증가 부분수열 찾기

##배열에서 읽어들인 숫자보다 크거나 같은 최초의 위치를 찾는다
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

c = [1000000000000000000000000000000]*n #매우 큰 값으로 c배열을 초기화

LIS = 0 #현재 가장 긴 증가하는 부분수열의 길이

for num in s: ##s에서 숫자를 처음부터 읽어들여..
    
    ##num보다 크거나 같은 값들 중에서 가장 작은 위치를 찾는다.

    loc = lower_bound(c,num,0,n)
    
    #찾은 위치가 현재 가장 긴 증가하는 부분수열과 같다면..

    if loc == LIS:
        
        c[LIS] = num # 그 위치에 숫자를 넣고

        LIS += 1 #가장 긴 증가하는 부분수열의 길이를 1 증가
    

    else:
        
        c[loc] = num

print(LIS)