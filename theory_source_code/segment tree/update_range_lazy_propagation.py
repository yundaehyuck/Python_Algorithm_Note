def update_range(tree,lazy,tree_index,start,end,left,right,value):

    #노드를 방문하면서, lazy값이 존재하는지 확인하면서 트리를 갱신시킨다.
    #그러니까 lazy 배열을 업데이트한다.
    update_lazy(tree,lazy,tree_index,start,end)
    
    #<빨간색>부분
    #[left,right]와 [start,end]가 완전히 벗어나는 경우
    #그냥 return하고 탐색 종료
    
    if left > end or right < start:
        
        return
    
    #<초록색>부분
    #[left,right]안에 [start,end]가 완전히 포함된 경우
    if left <= start and end <= right:
        
         #[start,end]안에 포함된 수들에 value를 모두 더해준다.
         #[start,end]안에 포함된 수들의 개수는 (end-start+1)개
         
        tree[tree_index] += (end-start+1)*value
        
        #그런데 start != end인 경우, 리프노드가 아닌 경우에는..
        #두 자식 노드 2*tree_index, 2*tree_index+1의 lazy배열에 value를 더해준다.
        
        if start != end:
            
            lazy[2*tree_index] += value
            lazy[2*tree_index+1] += value
            
        return #더 이상 아래로 내려가지 않는다.
   
    
    #<파란색>부분
    #[left,right]와 [start,end]가 일부만 겹치는 경우
    #왼쪽, 오른쪽으로 나누어 탐색
    
    mid = (start+end)//2
    
    update_range(tree,lazy,2*tree_index,start,mid,left,right,value)
    update_range(tree,lazy,2*tree_index+1,mid+1,end,left,right,value)
    
    #위의 <빨간색>, <초록색>에서 return되면서 변경된 자식값들을 가지고와, 올라오면서,
    #값들을 변경해주는 작업
    tree[tree_index] = tree[2*tree_index] + tree[2*tree_index+1]