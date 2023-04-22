from sys import stdin

while 1:
    
    n = int(stdin.readline())

    if n == 0:
        
        break
    
    else:
        
        m = int(n**(1/2))

        count = 0

        for i in range(1,m+1):
            
            if i*i == n:
                
                count += 1
            
            else:
                
                remain1 = n-i*i

                for j in range(i,int(remain1**(1/2))+1):
                    
                    if j*j == remain1:
                        
                        count += 1
                    
                    else:
                        
                        remain2 = remain1-j*j

                        for k in range(j,int(remain2**(1/2))+1):
                            
                            if k*k == remain2:
                                
                                count += 1
                            
                            else:
                                
                                remain3 = remain2-k*k
                                
                                remain4 = remain3**(1/2)

                                if remain3 > 0 and int(remain4) == remain4 and remain4 >= k:
                                    
                                    count += 1
      
        print(count)