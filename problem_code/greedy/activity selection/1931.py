from sys import stdin

n = int(stdin.readline())

room_list = []

for _ in range(n):
    
    s,e = map(int,stdin.readline().split())

    room_list.append((s,e))

#종료시간이 빠른 순서대로, 종료시간이 같다면 시작시간이 빠른 순서대로 정렬
sorted_room_list = sorted(room_list,key=lambda item: [item[1],item[0]])

a = sorted_room_list[0][1]

cnt = 1

#이전 작업의 종료시간 이상으로 다음 작업의 시작시간이 시작하면, 그것을 선택
#다음 작업의 종료시간으로 a를 변경
for s,e in sorted_room_list[1:]:
    
    if s >= a:
        
        cnt += 1
    
        a = e

print(cnt)