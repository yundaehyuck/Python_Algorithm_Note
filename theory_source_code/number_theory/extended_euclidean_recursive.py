#재귀함수

def recursive_extended_gcd(a,b):
    
    #유클리드 알고리즘에서 a를 b로 나누는데, b가 0이면 종료함
    if b == 0:
        
        return a,1,0
    
    gcd,x1,y1 = recursive_extended_gcd(b,a%b)
    
    #점화식 x = y1, y = x-qy, q = a//b
    x = y1
    y = x1 - y1*(a//b)
    
    return gcd,x,y