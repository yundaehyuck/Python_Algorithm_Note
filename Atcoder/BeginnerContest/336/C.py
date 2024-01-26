#0,2,4,6,8로만 이루어진 수를 오름차순으로 나열할때, N번째 숫자
#0,2,4,6,8,20,22,24,26,28,...을 2로 나눠보면
#0,1,2,3,4,10,11,12,13,14,...
#0,1,2,3,4,5,(5+1),(5+2),(5+3),(5+4)
#따라서 반대로 생각해서 N-1을 5진수로 고쳐서 각 자리수를 2배하면 된다
n = int(input()) - 1

if n == 0:
    
    print(0)

else:

    m = []
    
    while n > 0:
    
        n,r = n//5,n%5
    
        m.append(2*r)
    
    m.reverse()
    
    print(''.join(map(str,m)))