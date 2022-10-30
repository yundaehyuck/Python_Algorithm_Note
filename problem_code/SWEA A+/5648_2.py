##시뮬레이션 하지 않고 충돌 가능한 경우를 모두 찾아 한번에 처리

T = int(input())

for tc in range(1,T+1):
    
    n = int(input())

    atom_list = [list(map(int,input().split())) for _ in range(n)] ##원자들의 리스트

    ##원자들 간의 충돌 가능성을 모두 찾는다

    ##상,하로 움직이는데 x좌표가 같은 경우
    ##좌,우로 움직이는데 y좌표가 같은 경우
    ##x+y가 같은 경우(직각 충돌)
    ##x-y가 같은 경우(직각 충돌)

    colide_candidate = {}  ##충돌 가능한 후보를 저장한 사전
    
    ##n개중에 2개를 뽑은 모든 조합을 조사해서 충돌 가능한 모든 경우를 찾는다
    
    for i in range(n-1):
        
        x1,y1,d1,k1 = atom_list[i]
        
        for j in range(i+1,n):
            
            x2,y2,d2,k2 = atom_list[j]

            if x1 == x2: ##x좌표가 서로 같다면..
                
                colide_t = abs((y2-y1)/2)  ##충돌 시간
                
                if y1 > y2: ## 첫번째가 위에 있는 경우 하,상이면 충돌가능
                    
                    if d1 == 1 and d2 == 0:
                        
                        if colide_candidate.get((x1,(y1+y2)/2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,(y1+y2)/2,colide_t)] = [(i,k1),(j,k2)]  ##충돌위치, 충돌시간을 key로 하고 (원자 고유번호,에너지)를 리스트로
                        
                        else:
                            
                            colide_candidate[(x1,(y1+y2)/2,colide_t)].append((i,k1))
                            colide_candidate[(x1,(y1+y2)/2,colide_t)].append((j,k2))
                
                else: ##두번째 원자가 위에 있는 경우, 상,하이면 충돌 가능
                    
                    if d1 == 0 and d2 == 1:
                        
                        if colide_candidate.get((x1,(y1+y2)/2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,(y1+y2)/2,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x1,(y1+y2)/2,colide_t)].append((i,k1))
                            colide_candidate[(x1,(y1+y2)/2,colide_t)].append((j,k2))
            
            elif y1 == y2: ##y좌표가 서로 같다면...
                
                colide_t = abs((x2-x1)/2) ##충돌 시간
                
                if x1 > x2: ##첫번째 원자가 오른쪽에 있다면..
                    
                    if d1 == 2 and d2 == 3: ##좌,우로 향하면 충돌 가능
                        
                        if colide_candidate.get(((x1+x2)/2,y1,colide_t),0) == 0:
                            
                            colide_candidate[((x1+x2)/2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[((x1+x2)/2,y1,colide_t)].append((i,k1))
                            colide_candidate[((x1+x2)/2,y1,colide_t)].append((j,k2))
                
                else: ##두번째 원자가 오른쪽에 있다면.. 우,좌로 향하면 충돌 가능
                    
                    if d1 == 3 and d2 == 2: ##우,좌로 향하면 충돌 가능
                        
                        if colide_candidate.get(((x1+x2)/2,y1,colide_t),0) == 0:
                            
                            colide_candidate[((x1+x2)/2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[((x1+x2)/2,y1,colide_t)].append((i,k1))
                            colide_candidate[((x1+x2)/2,y1,colide_t)].append((j,k2))
            

            elif x1-y1 == x2-y2: ##x-y가 서로 같으면 충돌 가능
                
                colide_t = abs(x2-x1) ##충돌 시간
                
                if x1 > x2: ##첫번째가 오른쪽에 존재한다면..
                    
                    if (d1 == 2 and d2 == 0):
                        
                        if colide_candidate.get((x2,y1,colide_t),0) == 0:
                            
                            colide_candidate[(x2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x2,y1,colide_t)].append((i,k1))
                            colide_candidate[(x2,y1,colide_t)].append((j,k2))
                    
                    elif d1 == 1 and d2 == 3:
                        
                        if colide_candidate.get((x1,y2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,y2,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x1,y2,colide_t)].append((i,k1))
                            colide_candidate[(x1,y2,colide_t)].append((j,k2))
                
                else:
                    
                    if (d1 == 0 and d2 == 2):
                        
                        if colide_candidate.get((x1,y2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,y2,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x1,y2,colide_t)].append((i,k1))
                            colide_candidate[(x1,y2,colide_t)].append((j,k2))
                    
                    elif d1 == 3 and d2 == 1:
                        
                        
                        if colide_candidate.get((x2,y1,colide_t),0) == 0:
                            
                            colide_candidate[(x2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x2,y1,colide_t)].append((i,k1))
                            colide_candidate[(x2,y1,colide_t)].append((j,k2))
            

            elif x1+y1 == x2+y2: ##x+y가 서로 같으면 충돌 가능
                
                colide_t = abs(x1-x2) ##충돌 시간
                
                if x1 > x2: ##첫번째가 오른쪽에 존재한다면..
                    
                    if (d1 == 2 and d2 == 1):
                        
                        if colide_candidate.get((x2,y1,colide_t),0) == 0:
                            
                            colide_candidate[(x2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x2,y1,colide_t)].append((i,k1))
                            colide_candidate[(x2,y1,colide_t)].append((j,k2))
                    
                    elif d1 == 0 and d2 == 3:
                        
                        if colide_candidate.get((x1,y2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,y2,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x1,y2,colide_t)].append((i,k1))
                            colide_candidate[(x1,y2,colide_t)].append((j,k2))
                
                else:
                    
                    if (d1 == 1 and d2 == 2):
                        
                        if colide_candidate.get((x1,y2,colide_t),0) == 0:
                            
                            colide_candidate[(x1,y2,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x1,y2,colide_t)].append((i,k1))
                            colide_candidate[(x1,y2,colide_t)].append((j,k2))
                    
                    elif d1 == 3 and d2 == 0:
                        
                        if colide_candidate.get((x2,y1,colide_t),0) == 0:
                            
                            colide_candidate[(x2,y1,colide_t)] = [(i,k1),(j,k2)]
                        
                        else:
                            
                            colide_candidate[(x2,y1,colide_t)].append((i,k1))
                            colide_candidate[(x2,y1,colide_t)].append((j,k2))
            
            else:
                
                pass ##이외의 조합은 모두 충돌 불가능
    
    
    ##충돌 처리를 하여 충돌 에너지를 계산
    
    ##충돌이 가능한 모든 조합을 선정했으면
    
    ##이제 시간이 빠른 순서대로 정렬함

    sorted_candidate = sorted(colide_candidate.items(), key = lambda item: item[0][2])

    dead_atom = [0]*n ##이미 충돌해서 없어진 원자, 중복처리를 하기 위함

    ans = 0 ##충돌 에너지 총합

    ##충돌시작

    for key,colide_atom in sorted_candidate:  ##(충돌위치,충돌시간), (고유번호,에너지)의 리스트
        
        energy = []  ##충돌한 에너지

        cnt = 0  ##충돌 수

        tmp = set()  ##충돌한 원자들
        
        for i,k in colide_atom:
            
            if dead_atom[i] == 0: ##아직 충돌한 것이 아니라면..
                
                dead_atom[i] = 1  ##충돌하여 소멸처리

                cnt += 1  ##충돌한 원자수

                energy.append(k)  ##충돌한 원자의 방출 에너지
                tmp.add(i)  ##원자들의 고유번호 저장
        
        if cnt >= 2:  ##충돌한 원자수가 2개 이상이면, 실제로 충돌이 일어났다
            
            ans += sum(energy) ##에너지들의 합을 누적
        
        else:  ##충돌한 원자수가 1개 이하이면, 충돌하지 않았다.
            
            for i in tmp:  ##충돌하지 않았는데 임시로 저장한 고유번호가 충돌처리 되었으므로
                
                dead_atom[i] = 0 ##다시 충돌할 수 있다고 원상복구
    
    

    print('#'+str(tc),ans)