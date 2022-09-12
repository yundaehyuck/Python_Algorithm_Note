#postorder traverse

def postorder(node):
    
    if node:
        
        postorder(node.left)
        postorder(node.right)
        print(node.data,end = ' ')

postorder(root) # 4 5 2 3 1
