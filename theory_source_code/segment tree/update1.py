def update_tree(tree,tree_index,start,end,index,difference):
    
    #index가 [start,end]에 포함되지 않는 경우
    
    if index < start or index > end:
        
        return
    
    #index가 포함되는 구간이라면.. 해당 노드의 값을 바꿔줌
    tree[tree_index] = tree[tree_index] + difference
    
    #리프노드가 아닌 경우, 왼쪽,오른쪽 자식으로 탐색함
    
    mid = (start + end) // 2
    
    if start != end:
        
        update_tree(tree,2*tree_index,start,mid, index, difference)
        update_tree(tree,2*tree_index+1,mid+1,end,index,difference)

def update(A,tree,N,index,value):
    
    difference = value - A[index] #합을 변경시킬 값
    
    A[index] = value #index값이 value로 바뀜
    
    update_tree(tree,1,0,n-1,index,difference) #루트부터 탐색해서 값이 바뀐다