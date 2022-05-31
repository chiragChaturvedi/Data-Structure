class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0
class BST:
    def __init__(self, input):
        if isinstance(input, list):
            self.root = TreeNode(input[0])
            for i in range(1, len(input)):
                self.eleInsert(input[i], self.root)
        elif isinstance(input, str):
            if str(input).isalnum() and len(str(input)) == 1:
                self.root = TreeNode(input)
        elif isinstance(input, int):
            self.root = TreeNode(input)
        else:
            print('given argumentmust be a list or alnum char')
    def eleInsert(self, ele, current):
        if current == None:
            return TreeNode(ele)
        elif current.val > ele:
            current.left = self.eleInsert(ele, current.left)
            return current
        elif current.val < ele:
            current.right = self.eleInsert(ele, current.right)
            return current
    def preOrder(self, current):
        preOut = []
        if current:
            preOut.append(current.val)
            preOut = preOut + self.preOrder(current.left)
            preOut = preOut + self.preOrder(current.right)
        return preOut
    def inOrder(self, current):
        inOut = []
        if current:
            inOut = inOut + self.inOrder(current.left)
            inOut.append(current.val)
            inOut = inOut + self.inOrder(current.right)
        return inOut
    def postOrder(self, current):
        postOut = []
        if current:
            postOut = postOut + self.postOrder(current.left)
            postOut = postOut + self.postOrder(current.right)
            postOut.append(current.val)
        return postOut
if __name__ == '__main__':
    lst = [30,34,21,54,19,29,91,23]
    tree = BST(lst)
    preOrder = tree.preOrder(tree.root)
    inOrder = tree.inOrder(tree.root)
    postOrder = tree.postOrder(tree.root)
    print(preOrder, inOrder, postOrder)

