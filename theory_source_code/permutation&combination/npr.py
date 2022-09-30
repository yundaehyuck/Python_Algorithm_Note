def nPr(i,n,r):

    if i == r: #r번이 될때까지만 순열을 채워넣자

        print(p)
    
    else:

        for j in range(n):

            if used[j] == 0: ##a[j]가 사용되지 않았으면..

                p[i] = a[j] #i번째에 a[j]를 사용하여 채워넣고

                used[j] = 1 #a[j]를 사용했다고 표시하고

                nPr(i+1,n,r)  ##i+1번째를 결정하러 이동한다

                used[j] = 0  ##완성 후에 a[j]를 다른 자리에서도 쓸 수 있도록

n = 4

r = 2

a = [i for i in range(1,n+1)]

used = [0] * n

p = [0] * r

nPr(0,n,r)

"""
[1, 2]
[1, 3]
[1, 4]
[2, 1]
[2, 3]
[2, 4]
[3, 1]
[3, 2]
[3, 4]
[4, 1]
[4, 2]
[4, 3]
"""