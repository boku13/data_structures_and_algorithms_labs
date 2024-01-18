class node():
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
    
    def Print_level(root):
        
        #dont forget the base cases
        if root is None:
            return 
        
        queue = []
        queue.append(root)
        
        while(len(queue) > 0):
            print(queue[0].root)
            queue.pop(0)  #list.pop() removes last element otherwise
            
        if node.left is not None:
            queue.append(node.left)
        
        if node.right is not None:
            queue.append(node.right)
    
            
            