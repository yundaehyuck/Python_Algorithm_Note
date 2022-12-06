def update(A,tree, tree_index, start, end, index, value):
    
    #index가 [start,end]에 포함되어 있지 않다
    
    if index < start or index > end:
        
        return
    
    #리프노드를 찾았다면... 값을 바꿔준다
    
    if start == end:
        
        A[index] = value
        tree[tree_index] = value
        return
    
    #리프노드가 아니라면, 왼쪽, 오른쪽으로 나누어서 탐색
    
    mid = (start + end) // 2
    
    update(A,tree,2*tree_index, start, mid, index, value)
    update(A,tree,2*tree_index+1,mid+1,end, index, value)
    
    #update 함수가 return되면 자식 노드의 값들은 변경되어 있다
    tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]