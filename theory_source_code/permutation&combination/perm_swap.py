def permutation(i,r):

    if i == r: ##i번 인덱스가 원소의 개수와 동일해진다면...

        print(p) ##완성된 하나의 순열 p로 수행할 행동 처리
    
    else:
        
        for j in range(i,r):
            
            p[i],p[j] = p[j],p[i] #i,j번을 서로 뒤바꾸고
            permutation(i+1,r) #i+1번을 결정하러 이동
            p[i],p[j] = p[j],p[i] #재귀 이동을 수행하고 나서 원래 자리로 복구

p = [1,2,3,4]

permutation(0,4)

"""
[1, 2, 3, 4]
[1, 2, 4, 3]
[1, 3, 2, 4]
[1, 3, 4, 2]
[1, 4, 3, 2]
[1, 4, 2, 3]
[2, 1, 3, 4]
[2, 1, 4, 3]
[2, 3, 1, 4]
[2, 3, 4, 1]
[2, 4, 3, 1]
[2, 4, 1, 3]
[3, 2, 1, 4]
[3, 2, 4, 1]
[3, 1, 2, 4]
[3, 1, 4, 2]
[3, 4, 1, 2]
[3, 4, 2, 1]
[4, 2, 3, 1]
[4, 2, 1, 3]
[4, 3, 2, 1]
[4, 3, 1, 2]
[4, 1, 3, 2]
[4, 1, 2, 3]
"""