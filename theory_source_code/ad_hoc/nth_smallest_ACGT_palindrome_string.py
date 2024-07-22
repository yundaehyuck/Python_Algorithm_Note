#A,C,G,T만 사용한 길이 n인 팰린드롬 문자열을 사전 순으로 나열할때 k번째 문자열을 찾는 방법
n,k = map(int,input().split())

answer = ['A','C','G','T']

if n == 1:

    if k <= 4:

        print(answer[k-1])

    else:

        print('Impossible')

else:
    
    #앞 (n+1)//2자리의 문자열이 AAA,AAC,AAG,AAT,.. 순서대로 나열되므로 여기서 K번째를 찾고 
    #나머지는 거꾸로 붙여주면 된다
    d = (n+1)//2

    #길이 d인 문자열에서 각각 A,C,G,T 4가지 들어갈 수 있으므로 
    # 가능한 경우는 4**d가지니까 k가 이보다 크면 존재하지 않아
    if k > 4**d:

        print('Impossible')

    else:

        str_list = ['A']*d
        chr_list = ['A','C','G','T']

        #AAA,AAC,AAG,AAT,ACA,ACC,ACG,...가 1,2,3,4,..번째 문자열인데
        #zero index 0,1,2,3,4,...로 바꾸고
        #각각을 길이 3인 4진법으로 바꿔보면
        #000,001,002,003,010,011,012,...인데
        #0은 A, 1은 C, 2는 G, 3은 T에 대응
        k -= 1

        four = []

        while k > 0:
            
            p,q = k//4,k%4
            four.append(q)
            k = p
        
        while len(four) != d:
            
            four.append(0)
        
        for i in range(len(four)):
            
            str_list[d-1-i] = chr_list[four[i]]
        
        answer = ''.join(str_list)

        if n % 2 == 0:

            print(answer + answer[::-1])

        else:

            print(answer + answer[:-1][::-1])