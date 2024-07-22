#n번째로 작은 팰린드롬 수 찾기
#1자리,2자리,3자리,... 팰린드롬 수가 10,9,90,90,900,..개씩 존재함
n = int(input())

if n <= 10: #n이 10 이하이면 1자리 팰린드롬 수 0,1,2,..,9로 10개
    
    print(n-1)

else:
    #n이 10보다 크면 2자리이상의 팰린드롬 수
    #n에 10,9,90,90,900,..을 차례대로 빼면서 몇자리 팰린드롬 수인지 찾는다
    d = 1

    n -= 10

    while n > 0:
        
        d += 1

        #9,90,90,900,...은 d = 2에서 9*10**((d+1)//2-1)과 같다

        n -= (9 * 10**((d+1)//2-1))
    
    #음수가 되는 순간, 다시 이전에 뺀 수를 더해주면
    n += (9*10**((d+1)//2-1))

    #이제는 d자리 n번째 팰린드롬 수를 찾는 문제가 되었다.

    #이는 놀랍게도 앞 (d+1)//2자리를 나열해보면
    #10,11,12,13,14,...,99가 순서대로 나열된다는 것을 알 수 있고

    #따라서 d자리 n번째 팰린드롬 수는
    answer = 10**((d+1)//2-1) + n-1

    #d가 짝수인가 홀수인가에 따라, 짝수라면 그대로 거꾸로 붙여주면 될 것
    #홀수라면 마지막 자리를 빼고, 나머지를 거꾸로 붙여주면 팰린드롬이 될 것
    if d % 2 == 0:
        
        print(str(answer) + str(answer)[::-1])
    
    else:
        
        print(str(answer) + str(answer)[:-1][::-1])