from collections import Counter
 
s = Counter(input())
t = Counter(input())
 
no = False
 
replace_list = ['a','t','c','o','d','e','r']
 
def f(s,t,no):
 
    for k,v in s.items():
        
        if k == '@':
            
            continue
        
        if t.get(k,0) == 0:
            
            if t.get('@',0) < v or k not in replace_list:
                
                no = True
                break
            
            else:
                
                t['@'] -= v
                t[k] = v
        
        else:
            
            
            if t[k] < v:
                
                    
                if t['@'] < (v-t[k]) or k not in replace_list:
 
                    no = True
                    break
 
                else:
 
                    t['@'] -= (v-t[k])
                    t[k] += (v-t[k])
    
    return no
 
no = f(s,t,no)
 
if no:
    
    print('No')
 
else:
    
    no = f(t,s,no)
 
    if no:
        
        print('No')
    
    else:
    
        print('Yes')