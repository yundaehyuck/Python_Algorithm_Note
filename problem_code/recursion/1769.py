from sys import stdin

def change(n,cnt):
    
    #길이가 1이면, 3의 배수가 되는지 검사
    if len(n) == 1:
        
        y = int(n[0])

        if y % 3 == 0:
            
            return cnt,'YES'
        
        else:
            
            return cnt,'NO'
   
   #길이가 1이 아니면
    else:
        
        #해당 리스트의 원소를 정수로 만들어서 합을 구하고 
        #이걸 다시 string으로 바꾸고, list로 바꾼다음에
        n = list(str(sum(list(map(int,n)))))
        
        #변환 과정을 한번 했으니까, cnt+1을 해서 재귀적 호출 수행
        return change(n,cnt+1)

#숫자 문자열의 리스트로 
x = list(stdin.readline().rstrip())

cnt,ans = change(x,0)

print(cnt)
print(ans)