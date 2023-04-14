edges = [(1,10**9), (1,2000), (1,4), (30,10**9), (6,7)]

nums = set()

#사용되는 모든 정점의 번호를 set에 넣어준다.

for v1,v2 in edges:
    
    nums.add(v1)
    nums.add(v2)

#sorted()를 이용해 오름차순 정렬된 리스트를 생성
sorted_nums = sorted(nums)


#grid compression
compression = dict()

i = 1

for num in sorted_nums:
    
    compression[num] = i
    
    print(num, "->", i)
    
    i += 1

#간선을, 압축한 정점 번호로 변경
for i in range(5):
    
    v1,v2 = edges[i]
    edges[i] = (compression[v1], compression[v2])

1 -> 1
4 -> 2
6 -> 3
7 -> 4
30 -> 5
2000 -> 6
1000000000 -> 7