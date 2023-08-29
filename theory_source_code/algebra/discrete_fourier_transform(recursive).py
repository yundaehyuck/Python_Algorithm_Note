#DFT로 모든 f(w)를 구하는 함수
def dft(f,w):

    n = len(f) #2의 거듭제곱으로 맞춰져있음

    if n == 1:

        return
    
    #f의 크기를 절반씩 줄여나감
    #n >> 1 = n//2
    odd = [0]*(n>>1)
    even = [0]*(n>>1)
    
    #줄여나간 위치에 맞는 계수를 넣는다
    #f = a0 + a1x + a2x^2 + a3x^3 + a4x^4 + ... 
    #f = (a0 + a2x^2 + a4x^4 + ...) + (a1x + a3x^3 + a5x^5 + ...)
    #짝수 홀수 다항식을 관찰해보면..
    # 0번 > 0//2 = 0번, 2번 > 2//2 = 1번, 4번 >> 4//2 = 2번,...
    # 1번 > 1//2 = 0번, 3번 > 3//2 = 1번, 5번 >> 5//2 = 2번,...
    #절반 위치로 계수가 이동함을 확인할 수 있다
    
    for i in range(n):

        if i & 1:

            odd[i >> 1] = f[i]

        else:

            even[i >> 1] = f[i]
    
    #다항식을 계속해서 분할하고.. 위에 보면 n == 1이면 return(분할할 수 없을때까지 분할)
    #w^2을 넣는 이유는 f(x) = f_even(x^2) + xf_odd(x^2)이라서..
    dft(even,w*w)
    dft(odd,w*w)
    
    #현재 크기에서 모든 w에 대해 f(w)를 구함
    #f(w) = f_even(w^2) + w*f_odd(w^2)
    #f(-w) = f_even(w^2) -w * f_odd(w^2)
    
    #위에서 w*w를 넣어 분할했기 때문에, even[i],odd[i]에는 w_pow^2이 들어가있다
    
    w_pow = 1

    for i in range(n//2):

        f[i] = even[i] + w_pow * odd[i]  #w = x_i
        f[i+n//2] = even[i] - w_pow * odd[i] #-w = x_i+n/2, 대칭관계에 있음

        w_pow = w_pow * w