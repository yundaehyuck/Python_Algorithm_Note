#suffix array
#Manber-Myers Algorithm(O(nlog^2n))
def get_suffix_array(s):
    
    n = len(s)

    #i+d/2번째 접미사의 rank를 찾다가, 넘어가는 경우 빈 문자열의 rank는 0으로 하기 위해
    rank = [[0,0,0] for _ in range(n)]

    #d = 1일때 정렬단계
    for i in range(n):

        #첫번째 원소는 i번째 접미사의 rank
        #i번째 접미사의 첫 문자를 아스키코드로 바꿔놓은 값으로 바꿔놓는다
        #소문자로만 이루어져있다고 가정

        #두번째 원소는 i+d/2번째 접미사의 rank

        #세번째 원소(suffix array)는 i번째 접미사의 시작 인덱스 i로 초기화
        rank[i] = [ord(s[i]) - ord('a') + 1,0,i]
    
    
    d = 1 #d/2를 나타내는 값
    
    #i + d/2가 모두 빈 문자열이 될때까지 반복문을 수행
    #d < 2*n일때 반복을 종료
    while d < 2*n:
        
        #d단계 정렬 O(NlogN)정렬
        #첫번째, 두번째 원소로만 정렬하도록
        rank = sorted(rank,key = lambda x: [x[0],x[1]])

        #rank 재구성

        new_rank = [0]*n
        new_rank[0] = 1

        for i in range(1,n):
            
            if rank[i-1][0] == rank[i][0] and rank[i-1][1] == rank[i][1]:
                
                new_rank[i] = new_rank[i-1]
            
            else:
                
                new_rank[i] = new_rank[i-1] + 1
        
        #모든 접미사가 1~n개의 그룹으로 나뉘면 접미사 배열이 완성된 것
        #새롭게 부여된 rank는 첫번째 원소를 구성하는데,
        #모두 서로 다르다면 순서쌍을 정렬 하더라도 변화 없기 때문이다.
        if new_rank[n-1] == n:
            
            break
        
        #i번째 접미사의 rank를 저장
        ind_rank = [0]*n

        for i in range(n):
            
            rank[i][0] = new_rank[i]
            ind_rank[rank[i][2]] = rank[i][0]
        

        #순서쌍 재구성
        #두번째 원소를 i+d/2번째 접미사의 rank로 구성
        for i in range(n):
            
            #i번째 접미사의 위치 i = rank[i][2]
            #d/2칸 앞의 위치는 rank[i][2] + d

            #d/2칸 앞 위치가 길이를 넘어가면, 0으로
            if rank[i][2]+d >= n:
                
                rank[i][1] = 0

            #길이를 넘어가지 않으면...
            #i+d/2번째 접미사의 rank는 ind_rank[rank[i][2]+d]에 있다

            else:
                
                rank[i][1] = ind_rank[rank[i][2]+d]

        #다음 d 값을 2배 하기
        d *= 2
    
    #rank배열의 3번째 원소를 가지고와 suffix array 구성
    suffix = [0]*(n)

    for i in range(n):
        
        suffix[i] = rank[i][2]

    return suffix