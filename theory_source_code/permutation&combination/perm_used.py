def permutation(i,r):

    if i == r:

        print(p) #완성된 순열 p를 이용한 행동
    
    else:

        for j in range(r):

            if used[j] == 0: #a[j]가 사용되지 않았으면

                used[j] = 1 #a[j]를 사용했다고 표시

                p[i] = a[j] #p의 i번째를 a[j]로 사용하고

                permutation(i+1,r) #p의 i+1번째를 결정하러 이동

                used[j] = 0 #순열을 완성하고 나서 a[j]를 다른데서 쓸수 있도록 복구

n = 3

a = [i for i in range(1,n+1)]

p = [0] * n

used = [0] * n

permutation(0,3)
"""
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
"""

