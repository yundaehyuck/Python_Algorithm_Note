#repeated substring

def counting_sort(suffix_array,rank,d,n):
    
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
        
        suffix_array = counting_sort(suffix_array,rank,d,n)

        new_rank = [0]*(n+1)

        new_rank[suffix_array[0]] = 1

        for i in range(1,n):
            
            new_rank[suffix_array[i]] = new_rank[suffix_array[i-1]] + compare(rank,suffix_array[i-1], suffix_array[i],d)
        
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
        
        adj = suffix_array[reverse_suffix_array[i]-1]

        while i+k < n and adj+k < n and s[i+k] == s[adj+k]:
            
            k += 1
        
        lcp[reverse_suffix_array[i]] = k
        
        if k > 0:
            
            k -= 1
    
    return lcp

s = input()

n = len(s)

suffix_array = [i for i in range(n)]
rank = [ord(s[i]) - ord('a') + 1 for i in range(n)]
rank.append(0)

suffix_array = get_suffix_array(suffix_array,rank)
lcp = kasai(suffix_array,s)

#전체 문자열에서 두번 이상 나타나는 가장 긴 부분문자열은..?
#lcp값이 가장 큰 위치 i를 찾고, 해당 s[suffix_array[i]:]에서 lcp값만큼 접두사로 가져오면 된다.
max_lcp = 0
ind = 0

for i in range(n):
    
    if lcp[i] > max_lcp:
        
        max_lcp = lcp[i]
        ind = i

print(s[suffix_array[ind]:suffix_array[ind]+max_lcp])