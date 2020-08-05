# A node contains the data, left and right pointers
class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = self.right = None

def invert(node):  
  
    if (node == None): 
        return
    else: 
        # swap the pointers in this node
        node.left, node.right = node.right, node.left
  
        # recursive calls
        invert(node.left)  
        invert(node.right)  
  

# print InOrder binary tree traversal.
def print_tree(node) : 
  
    if (node == None):  
        return
          
    print_tree(node.left)  
    print(node.data, end=' ')
    print_tree(node.right)  

if __name__ == "__main__":
    root = Node(1)  
    root.left = Node(2)  
    root.right = Node(3)
    root.left.left = Node(4)  
    root.left.right = Node(5)  
    root.right.left = Node(6)  
    root.right.right = Node(7)  
      
      
    # Print inorder traversal of the input tree
    print("Inorder traversal of the constructed tree is")  
    print_tree(root)  
          
    # Convert tree to its mirror
    invert(root)  
      
    # Print inorder traversal of the mirror tree
    print("\nInorder traversal of the mirror treeis ")  
    print_tree(root)  
    print()
