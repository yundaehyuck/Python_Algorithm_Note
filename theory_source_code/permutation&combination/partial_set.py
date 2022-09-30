arr = [3,6,7]

n = len(arr)

for i in range(1<<n): ##i는 arr의 모든 부분집합

    partial = [] ##i를 나타내는 부분집합

    for j in range(n): #i를 길이 n인 이진수로 나타낼때, 0~n-1의 비트 검사

        if i & (1<<j): #i의 j번 비트가 1이라면..

            partial.append(arr[j]) ##j번 원소를 pick하여 부분집합에 추가
    
    print(partial)


"""
[]
[3]
[6]
[3, 6]
[7]
[3, 7]
[6, 7]
[3, 6, 7]
"""