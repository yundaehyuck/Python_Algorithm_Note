#preorder traverse

def preorder(node):

#if node는 왜 써야하냐?

# 1 >> 2 간 다음에 4와 5를 갈건데 4와 5는 node.left = None, node.right = None
#그래서 None.data 이거 하면 에러나거든
#그래서 None이면 아무것도 실행이 안되니까
#재귀함수를 종료시키는 역할을 함
    
    if node:
        
        print(node.data, end = ' ') #방문 순서를 한줄로 출력하고 싶다면 end 옵션 사용
        
        preorder(node.left)
        
        preorder(node.right)


preorder(root) #1 2 4 5 3