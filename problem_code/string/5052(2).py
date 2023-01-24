from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    
    n = int(stdin.readline())

    phone_list = []

    for _ in range(n):
        
        phone = stdin.readline().rstrip()

        phone_list.append(phone)
    
    phone_list.sort()

    no = False

    for i in range(n-1):
        
        compare = min(len(phone_list[i]),len(phone_list[i+1]))
        
        if phone_list[i][:compare] == phone_list[i+1][:compare]:
            
            print('NO')
            no = True
            break
    
    if no == False:
        
        print('YES')