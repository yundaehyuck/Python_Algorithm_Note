#count of all unique repeated substring

from sys import stdin

def counting_sort(suffix_array,rank,d):
    
    m = max(n,256)

    counting = [0]*(m+1)

    counting[0] = d

    for i in range(d,n):
        
        counting[rank[i]] += 1
    
    for i in range(1,m+1):
        
        counting[i] += counting[i-1]
    
    second = [0]*n

    for i in range(n-1,-1,-1):
        
        if i+d >= n:
            
            ind = n
        
        else:
            
            ind = i+d

        counting[rank[ind]] -= 1
        second[counting[rank[ind]]] = i
    
    counting = [0]*(m+1)

    for i in range(n):
        
        counting[rank[i]] += 1
    
    for i in range(1,m+1):
        
        counting[i] += counting[i-1]
    
    for i in range(n-1,-1,-1):
        
        counting[rank[second[i]]] -= 1
        suffix_array[counting[rank[second[i]]]] = second[i]
    
    return suffix_array

def compare(rank,a,b,d):
    
    if rank[a] == rank[b] and rank[a+d] == rank[b+d]:
        
        return 0
    
    else:
        
        return 1

def get_suffix_array(suffix_array,rank):
    
    d = 1

    while d < 2*n:
        
        suffix_array = counting_sort(suffix_array,rank,d)

        new_rank = [0]*(n+1)

        new_rank[suffix_array[0]] = 1

        for i in range(1,n):
            
            new_rank[suffix_array[i]] = new_rank[suffix_array[i-1]] + compare(rank,suffix_array[i-1],suffix_array[i],d)

        if new_rank[suffix_array[n-1]] == n:
            
            break
        
        rank = new_rank
        d *= 2
    
    return suffix_array

def kasai(suffix_array,s):
    
    lcp = [0]*n
    reverse_suffix_array = [0]*n

    for i in range(n):
        
        reverse_suffix_array[suffix_array[i]] = i
    
    k = 0

    for i in range(n):
        
        if reverse_suffix_array[i] == 0:
            
            continue
        
        adj = suffix_array[reverse_suffix_array[i] - 1]

        while i+k < n and adj+k < n and s[i+k] == s[adj+k]:
            
            k += 1
        
        lcp[reverse_suffix_array[i]] = k

        if k > 0:
            
            k -= 1
    
    return lcp

T = int(stdin.readline())

for _ in range(T):
    
    s = stdin.readline().rstrip()

    n = len(s)

    suffix_array = [i for i in range(n)]
    rank = [ord(s[i]) - ord('a') + 1 for i in range(n)]
    rank.append(0)

    suffix_array = get_suffix_array(suffix_array,rank)
    lcp = kasai(suffix_array,s)
    
    #lcp[i] = suffix_array[i]와 suffix_array[i-1]의 가장 긴 공통 접두사의 길이
    #lcp[i-1] = suffix_array[i-1], suffix_array[i-2]의 가장 긴 공통 접두사의 길이
    
    #lcp[i] - lcp[i-1] > 0이면, lcp[i] - lcp[i-1]만큼 suffix_array[i]부분에서 새로운 반복된 부분문자열이 생겨났고
    #lcp[i] - lcp[i-1] < 0이면, suffix_array[i-1] 부분에 suffix_array[i]에서 생긴 모든 반복 부분 문자열이 포함되어 있으니 더해주면 안된다
    
    answer = 0

    for i in range(1,n):
        
        if lcp[i] - lcp[i-1] > 0:
            
            answer += (lcp[i]-lcp[i-1])
    
    print(answer)