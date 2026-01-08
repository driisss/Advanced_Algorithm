#binary tree
class TreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder(self,root):
        if root==None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)xb 


root = TreeNode(10)
root.left = TreeNode (20)
root.right = TreeNode (30)
root.left.left = TreeNode (40)
root.left.right = TreeNode (50)