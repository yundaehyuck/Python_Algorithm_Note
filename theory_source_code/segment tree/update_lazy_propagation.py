#lazy배열을 업데이트 하는 함수
#[start,end]는 방문한 노드가 저장하는 구간
def update_lazy(tree,lazy,tree_index,start,end):
    
    #방문한 노드에 저장된 lazy가 0이 아니라면..
    
    if lazy[tree_index] != 0:
        
        #해당 노드가 저장하는 구간 [start,end]에 포함된 모든 수들에 lazy[tree_index]를 더해준다.
        #[start,end]에 포함된 모든 수들의 개수는 (end-start+1)
        
        #따라서, tree[tree_index]에 (end-start+1)*lazy[tree-index]를 더해준다.
        
        tree[tree_index] += (end-start+1)*lazy[tree_index]
        
        #만약 리프노드가 아니라면..
        if start != end:
            
            #두 자식노드에 lazy값을 전달해준다
            lazy[2*tree_index] += lazy[tree_index]
            lazy[2*tree_index+1] += lazy[tree_index]
        
        #변경에 사용한 lazy값은 초기화시킨다.
        lazy[tree_index] = 0