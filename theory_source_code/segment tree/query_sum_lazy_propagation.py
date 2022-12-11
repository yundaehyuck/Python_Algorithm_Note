#구간 [left,right]의 합을 구하는 함수
def query_sum(tree,lazy,tree_index,start,end,left,right):
    
    #노드를 방문하면서, lazy값이 존재하는지 확인하면서 트리를 갱신시킨다.
    #그러니까 lazy 배열을 업데이트한다.
    update_lazy(tree,lazy,tree_index,start,end)
    
    #[left,right]가 [start,end]와 완전히 벗어난 경우
    
    if left > end or right < start:
        
        return 0
    
    #[left,right]안에 [start,end]가 완전히 포함된 경우
    
    if left <= start and end <= right:
        
        return tree[tree_index]
    
    #[left,right]와 [start,end]가 일부만 겹치는 경우
    #왼쪽, 오른쪽 나누어 탐색
    
    mid = (start+end)//2
    
    left_sum = query_sum(tree,lazy,2*tree_index,start,mid,left,right)
    right_sum = query_sum(tree,lazy,2*tree_index+1,mid+1,end,left,right)
    
    return left_sum + right_sum