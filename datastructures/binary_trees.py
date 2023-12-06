class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if not root:
        return False
    
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
    

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

t1.left, t1.right = t2, t3

print(search(t1, 33))