#inorder traverse

def inorder(node):
    
    if node:
        
        inorder(node.left)
        print(node.data, end = ' ')
        inorder(node.right)

inorder(root) #4 2 5 1 3