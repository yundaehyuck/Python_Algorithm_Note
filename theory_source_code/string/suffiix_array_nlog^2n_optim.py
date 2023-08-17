#manber-myers o(nlog^2n) optimization algorithm

def compare(rank,a,b,d):
    
    if rank[a] == rank[b] and rank[a+d] == rank[b+d]:
        
        return 0
    
    else:
        
        return 1

def get_suffix_array(rank):
    
    d = 1

    while d < 2*n:

        #counting sort대신에 quick sort를 하는 부분
        #rank 배열의 값에 따라 정렬된 index를 suffix_array로 해준다
        #0~n-1을 정렬하는데, rank[i]의 값(rank배열의 첫번째 원소 i번째 접미사의 rank)에 따라 정렬
        #rank[i]가 같으면 rank[min(i+d,n)]에 따라 정렬(rank배열의 두번째 원소 i+d번째 접미사의 rank)
        #i+d가 n이상이면 rank[n] = 0으로 부여해준다
        suffix_array = sorted(range(n), key = lambda i: [rank[i],rank[min(i+d,n)]])

        new_rank = [0]*(n+1)

        new_rank[suffix_array[0]] = 1

        for i in range(1,n):
            
            new_rank[suffix_array[i]] = new_rank[suffix_array[i-1]] + compare(rank, suffix_array[i-1], suffix_array[i] , d)

        if new_rank[suffix_array[n-1]] == n:
            
            break
        
        rank = new_rank

        d *= 2

    return suffix_array 
            

s = input()

n = len(s)

#suffix array를 초기화하지 않아도 된다.

rank = [ord(s[i]) - ord('a') + 1 for i in range(n)]
rank.append(0)

suffix_array = get_suffix_array(rank)

print(" ".join(map(str, suffix_array)) + "\n")