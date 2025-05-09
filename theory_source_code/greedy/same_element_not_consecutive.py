#서로 동일한 인덱스를 연속으로 사용하지 않고 일렬로 배치
#최댓값인 원소의 개수 m개 나머지 원소들의 개수 sum(A)-m개

#최댓값인 원소 인덱스를 먼저 나열하고
#그 사이사이에 나머지 원소 인덱스를 집어넣는 느낌으로

#m,_,m,_,...,_,m

#그 사이사이에는 m-1개의 공간이 있다
#r = m-1이면 사이사이에 나머지 원소를 배치하면 전부 일렬로 배치가능
#r = m이면 m,r,m,r,m,r,...,r,m으로 m-1개에 r을 넣고 m,r,m,r,...,r,m 다음에 r을 1개 하면 된다
#r = m+1 이상이면 나머지 원소 n1,n2,..는 최대 m개이므로
#m 사이에는 나머지 원소 n1을 전부 배치하고 m,n1,m,n1,...,n1,m,n1로 배치하고
#이제 n2부터 새롭게 배치해야하므로 n2,n3,...n3,n2로 똑같은 문제가 되니까 결국 전부 일렬로 배치할 수 있게 된다
# 
# 하지만 r = m-2,m-3,,...이면 m이 서로 붙어버린다
# 따라서 r을 전부 배치하면 m이랑 합쳐서 2r개 배치하고 나머지 m들 중 1개만 사용가능하니 2r+1개  
n = int(input())

A = list(map(int,input().split()))

m = max(A)
s = sum(A)

r = s - m

if m <= r+1:
    
    print(s)

else:
    
    print(2*r+1)