#서로 다른 부분문자열의 개수 구하기

#suffix array를 구하기
def counting_sort(suffix_array,rank,d):
    
    m = max(n,256)

    counting = [0]*(m+1)

    counting[0] = d

    for i in range(d,n):
        
        counting[rank[i]] += 1
    
    for i in range(m+1):
        
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
    
    for i in range(m+1):
        
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

#lcp 배열을 구하기
def kasai(suffix_array,s):
    
    lcp = [0]*n
    reverse = [0]*n

    for i in range(n):
        
        reverse[suffix_array[i]] = i
    
    k = 0

    for i in range(n):
        
        if reverse[i] == 0:
            
            continue
        
        adj = suffix_array[reverse[i]-1]

        while i + k < n and adj + k < n and s[i+k] == s[adj+k]:
            
            k += 1
        
        lcp[reverse[i]] = k

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

#모든 부분문자열은 접미사의 접두사이다.
#정렬된 i번째 접미사의 길이는 n - suffix_array[i]
#각 접미사는 n - suffix_array[i]개만큼 접두사(=부분문자열)를 가진다.
#i번째 접미사는 i-1번째 접미사와 lcp[i]만큼 서로 동일하다.
#따라서 0~n-1번 접미사를 순회하면서 부분문자열 개수를 더해나가고 겹치는 개수만큼 뺀다면..
#n - sa[0] + n-sa[1]-lcp[1] + n-sa[2]-lcp[2] + ... + n-sa[n-1]-lcp[n-1]
#n(n+1)//2 - sum(lcp)

print(n*(n+1)//2 - sum(lcp))