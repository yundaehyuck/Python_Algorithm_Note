#선형일차연립방정식이 유일한 해를 가질때
#gaussian elimination

from sys import stdin

#i번째 행의 leading element가 0이라면, j (> i)번째 행과 교환하는 연산
def row_exchange(matrix,i):

    for j in range(i+1,n):

        if matrix[j][i] != 0:

            matrix[i],matrix[j] = matrix[j],matrix[i]
            break

    return matrix

#i번째 행의 i번째 열 원소인 leading element를 1로 만들었을때,
#i번째 열의 나머지 원소를 모두 0으로 만드는 연산
def convert_to_zero(matrix,i):

    for j in range(n):

        if i != j:

            a = matrix[j][i]

            for k in range(m):

                matrix[j][k] -= (matrix[i][k] * a)

    return matrix

#gaussian elimination
#선형연립방정식의 유일한 정수해를 구하는 함수
def gauss_elimination(matrix):
    
    #reduced row echelon form을 만드는 과정

    for i in range(n): #모든 행을 순회하여,

        if matrix[i][i] == 0: #i번째 행의 leading element가 0이라면..

            matrix = row_exchange(matrix,i) #i번째 열이 0이 아닌 다른 j (> i)번째 행과 교환
        
        #i번째 행의 leading element를 1로 만들기 위해,
        #모든 0,1,..,m-1열의 원소에 1/a를 곱한다
        a = matrix[i][i]
        
        for j in range(m):

            matrix[i][j] /= a
        
        #i번째 행의 leading element가 1로 되었다면,
        #i번째 열의 나머지 원소는 모두 0으로 만들어준다
        matrix = convert_to_zero(matrix,i)
    
    #reduced row echelon form을 만들었다면,
    #마지막 열이 선형연립방정식의 유일한 해집합
    solution = []

    for i in range(n):

        solution.append(round(matrix[i][-1])) #round()를 쓰면 가장 가까운 정수로 바꿔줌

    return solution

n = int(stdin.readline())

matrix = []

for _ in range(n):

    matrix.append(list(map(int,stdin.readline().split())))

m = len(matrix[0])

print(' '.join(map(str,gauss_elimination(matrix))))