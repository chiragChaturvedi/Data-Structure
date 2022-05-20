class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class BST:
    def __init__(self, input):
        self.inOut = []
        self.postOut = []
        if type(input) == 'list':
            self. root = input[0]
            for ele in range(1, len(input)):
                self.eleInsert(ele, self.root)
        elif type(input) == 'str' or type(input) == 'int':
            if str(input).isalnum() and len(str(input)) == 1:
                self.root = TreeNode(input)
        else:
            print('given argumentmust be a list or alnum char')
    def eleInsert(self, ele, current):
        if current == None:
            current = TreeNode(ele)
        elif current.val > ele:
            self.eleInsert(ele, current.left)
        elif current.val < ele:
            self.eleInsert(ele, current.right)
        return
    def preOrder(self, current):
        preOut = []
        if current:
            self.preout.append(current.val)
            self.preOrder(self, current.left)
            self.preOrder(self, current.right)
    def inOrder():
        pass
    def postOrder():
        pass
