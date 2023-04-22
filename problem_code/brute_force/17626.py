from sys import stdin

n = int(stdin.readline())

x = 1

m = int(n**(1/2))

num_list = [y**2 for y in range(1,m+1)]

find = False

#1개의 제곱수 합으로 나타내는 경우
for i in range(m):

    if num_list[i] == n:
        
        find = True

        break

if find:

    print(x)

#제곱수 1개로 찾지 못한 경우
else:

    x += 1
    
    #제곱수 2개로 찾는 경우
    for i in range(m):

        for j in range(m):

            if num_list[i] + num_list[j] == n:

                find = True
                break

        if find:

            break

    if find:

        print(x)
    
    #제곱수 2개로 찾지 못한 경우
    else:

        x += 1
        
        #제곱수 3개로 찾는 경우
        for i in range(m):

            for j in range(m):

                for k in range(m):

                    if num_list[i] + num_list[j] + num_list[k] == n:

                        find = True
                        break

                if find:

                    break

            if find:

                break

        if find:

            print(x)
        
        #제곱수 3개로도 답을 찾지 못한다면, 정답은 4이다.
        else:

            print(x+1)