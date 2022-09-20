from collections import deque

def get_num(n,len_n,key_dict):
    
    ans = 0

    for i in range(len_n-1,-1,-1):
        
        key = key_dict.get(n[i],0)

        if key == 0:
        
            ans += (int(n[i])*(16**(len_n-1-i)))
        
        else:
            
            ans += key*(16**(len_n-1-i))
    
    return ans
        


key_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}


T = int(input())

for t in range(1,T+1):

    n,k = map(int,input().split())

    a = n//4

    queue = deque(list(input()))

    password_set = set()

    r = 0

    while r != a:
        
        cnt = 0

        ans = ''

        for b in queue:
            
            ans += str(b)

            cnt += 1

            if cnt == a:
                
                transform_ans = get_num(ans,a,key_dict)
                
                password_set.add(transform_ans)
                
                cnt = 0

                ans = ''
        
        
        queue.rotate(1)

        r += 1
    

    password = sorted(list(password_set),reverse=True)

    print('#'+str(t),password[k-1])