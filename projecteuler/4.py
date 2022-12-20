max_p = 0

for i in range(999,99,-1):
    
    for j in range(999,99,-1):
        
        product = str(i*j)

        len_p = len(product)

        palindrome = True

        for k in range(len_p//2):
            
            if product[k] != product[len_p-1-k]:
                
                palindrome = False
                break
        
        if palindrome == True:
            
            if max_p < int(product):
                
                max_p = int(product)


print(max_p)