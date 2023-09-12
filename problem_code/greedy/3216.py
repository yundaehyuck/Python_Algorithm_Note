from sys import stdin

n = int(stdin.readline())

music = []

for _ in range(n):
    
    d,v = map(int,stdin.readline().split())

    music.append((d,v))

#다운받으면서 음악 재생시간을 누적해가고.. 어느 순간 재생하면 모든 다운 로드 시간을 커버~ X
#처음부터 순회하면서.. 이전에 받은 음악 재생시간으로 다운로드 시간을 상쇄해가며 전체 필요한 다운로드 시간을 구하기 O
answer = music[0][1]
play = music[0][0]

for i in range(1,n):

#누적된 음악 재생시간보다 다운로드 시간이 더 크다면..
#음악 재생시간으로 다운로드 시간을 일부 없애고 남은 시간만큼 다운로드에 쓴다

    if music[i][1] > play:
        
        answer += music[i][1] - play
        play = 0

#누적된 음악 재생시간이 다운로드 시간보다 더 짧다면..
#음악 재생시간을 사용해서 다운로드 시간을 모두 없애버린다

    else:
        
        play -= music[i][1]

    play += music[i][0] #해당 음악을 다운받으면.. 음악 재생시간에 누적해가고..

print(answer)