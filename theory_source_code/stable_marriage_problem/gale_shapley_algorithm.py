#안정 결혼 문제(stable marriage problem)

#게일-섀플리 알고리즘(gale shapley algorithm)
from sys import stdin

n = int(stdin.readline())

man = [0]*(n+1)

woman = [0]*(n+1)

for i in range(1,n+1):
    
    man[i] = list(map(int,stdin.readline().split()))

for i in range(1,n+1):
    
    woman[i] = list(map(int,stdin.readline().split()))


matching = [0]*(n+1)

no_matching_woman = list(range(1,n+1))

man_reject_woman = [[] for _ in range(n+1)]

    #각 남자의 라운드마다 득표현황

vote_man = [[] for _ in range(n+1)]

while 1:

    #짝이 없는 사람중에서..

    for i in no_matching_woman:
        
        #여자가 best인 사람을 왼쪽부터 차례대로 뽑는데

        for best in woman[i]:
            
            #거절당하지 않은 남자중에서..

            if best not in man_reject_woman[i]:
             
             #베스트에 투표를 한다
                vote_man[best].append(i)
                break
    
    #matching 시작

    for i in range(1,n+1):
        
        #2표 이상 득표를 한 남자는..

        if len(vote_man[i]) >= 2:
            
            #최선의 선호도를 가지는 여자를 선택한다

            min_ind = n+1

            for j in vote_man[i]:
                
                j_index = man[i].index(j)

                #index가 가장 작아야 최선의 선호도를 가진 여자

                if min_ind > j_index:
                    
                    min_ind = j_index
            
            #i번째 남자는 min_ind가 최선의 여자
            
            matching[i] = man[i][min_ind]

            for j in vote_man[i]:

                if j != man[i][min_ind]:

                    man_reject_woman[j].append(i)

               
        
        elif len(vote_man[i]) == 1:
            
            matching[i] = vote_man[i][0]
           
    
    no_matching_woman = []

    vote_man = [[] for _ in range(n+1)]

    for i in range(1,n+1):
        
        if i not in matching:
            
            no_matching_woman.append(i)
        
        if matching[i] != 0:
            
            vote_man[i].append(matching[i])
    
    if no_matching_woman == []:
        
        break


for i in range(1,n+1):
    
    print(matching[i])