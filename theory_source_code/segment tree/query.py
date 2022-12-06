#tree, tree의 인덱스
#[start,end]는 해당 트리 인덱스가 저장하는 구간
#[left,right]는 합을 구하고 싶은 구간

#최초에 tree_index = 1, start = 0, end = N-1(배열 A의 크기 N)

def query(tree, tree_index, start, end, left, right):
    
    #[left,right]가 [start,end]를 완전히 벗어난 경우
    #탐색할 필요도 없고 값을 가져올 필요도 없다
    if left > end or right < start:
        
        return 0
    
    #[left,right]가 [start,end]를 완전히 포함하는 경우
    #해당 노드에 저장된 값을 가져오고 더 이상 탐색할 필요는 없다
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    #그 이외의 경우
    #왼쪽 자식과 오른쪽 자식으로 나누어서 탐색
    
    #부모 인덱스가 tree_index라면... 왼쪽 자식은 2*tree_index, 오른쪽 자식은 2*tree_index+1
    
    mid = (start + end) // 2
    
    left_answer = query(tree,2*tree_index, start, mid, left, right)
    
    right_answer = query(tree,2*tree_index+1, mid+1, end, left, right)
    
    return left_answer + right_answer