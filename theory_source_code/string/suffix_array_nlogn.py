#suffix array
#manber-myers O(NlogN) 최적화

#pair type stable sort
def counting_sort(suffix_array,rank,d):
    
    m = max(n,256) #가질 수 있는 rank 수
    
    counting = [0]*(m+1)

    #두번째 원소인 i+d번째 rank에 대한 정렬 단계
    #rank의 두번째 원소는 d번부터

    #i번째 접미사와 i+d번째 접미사의 rank차이가 d이기 때문
    #계산된 rank 누적합에 d를 더해줘야함
    counting[0] = d 

    for i in range(d,n):
        
        counting[rank[i]] += 1
    
    for i in range(1,m+1):
        
        counting[i] += counting[i-1]
    
    second = [0]*n

    for i in range(n-1,-1,-1):
        
        if i+d >= n: #index가 넘어가는 경우, 추가로 만든 n번 index로 
            
            ind = n
        
        else:
            
            ind = i+d #index가 넘어가지 않는 경우
        
        counting[rank[ind]] -= 1
        second[counting[rank[ind]]] = i
    
    #첫번째 원소에 대한 정렬

    counting = [0]*(m+1)

    for i in range(n):
        
        counting[rank[i]] += 1
    
    for i in range(1,m+1):
        
        counting[i] += counting[i-1]
    
    #rank배열의 최종 counting sort
    #rank배열을 정렬하고 index를 저장하면, suffix_array가 된다는 점을 이해하는 것이 중요하다.
    for i in range(n-1,-1,-1):
        
        counting[rank[second[i]]] -= 1

        suffix_array[counting[rank[second[i]]]] = second[i]
    
    return suffix_array

#새로운 rank를 부여하기 위한 비교 함수
def compare(rank,a,b,d):
    
    #a+d와 b+d가 n-1보다 클수 있는데..
    #rank[a] == rank[b]를 먼저 비교하면 신기하게 index error가 나지 않는다..
    #그러니까 rank[a] == rank[b]일때, a+d, b+d는 n-1보다 클수 없다는 뜻이긴한데... 정말 그런지는 모르겠다

    #rank배열의 첫번째 원소 rank[a],rank[b]
    #rank배열의 두번째 원소 rank[a+d],rank[b+d]

    #첫번째 원소와 두번째 원소가 모두 같으면 동일한 rank
    #아니라면 1 증가
    if rank[a] == rank[b] and rank[a+d] == rank[b+d]:

        return 0

    else:

        return 1 

#suffix array구성하는 함수
def get_suffix_array(suffix_array,rank):
    
    d = 1

    while d < 2*n: #d < 2n일때 반복
        
        #O(N) counting sort
        suffix_array = counting_sort(suffix_array,rank,d)

        new_rank = [0]*(n+1)

        #새로운 rank 재구성
        #suffix_array는 정렬된 결과라는 점을 이해하는 것이 중요하다.
        #suffix_array[0]는 가장 빠른 접미사의 index가 있으니 가장 작은 rank를 부여
        #suffix_array[i]의 rank는 이미 계산된 suffix_array[i-1]과 비교해서... rank를 부여
        new_rank[suffix_array[0]] = 1

        for i in range(1,n):
            
            new_rank[suffix_array[i]] = new_rank[suffix_array[i-1]] + compare(rank,suffix_array[i-1],suffix_array[i],d)
        
        #모든 rank가 서로 다르다면 정렬이 끝났다
        #new_rank[n-1]과 new_rank[suffix_array[n-1]]은 다르다
        if new_rank[suffix_array[n-1]] == n:
            
            break

        rank = new_rank #rank배열을 새롭게 구성한 new_rank로 대체

        d *= 2 #d를 2배하고 다음 반복으로
    
    return suffix_array

s = input()
n = len(s)

#초기화 단계
suffix_array = [i for i in range(n)]

#일차원 배열 rank에 첫번째 원소, 두번째 원소를 모두 넣을거임
#i번째 접미사의 첫번째 원소는 i번째에, 두번째 원소는 i+d번째에 있겠지
#i+d가 넘어가면 0으로 하면 되고

rank = [ord(s[i])-ord('a')+1 for i in range(n)]

rank.append(0) #i+d가 넘어가는 경우를 위해 rank[n] = 0을 구성

suffix_array = get_suffix_array(suffix_array,rank)

#배열에 대한 빠른 출력방법
#print(*suffix_array)보다 0.1초정도 빠르다
print(" ".join(map(lambda i:str(i+1), suffix_array)))
