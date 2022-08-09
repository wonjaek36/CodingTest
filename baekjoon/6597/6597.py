from sys import stdin


class TreeRepair(object):

    def __init__(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        self.tree = {} 
        self.root = None
    
    def construct_tree(self, cur, subset):
        if subset == '':
            return None, cur-1

        root = self.preorder[cur]
        self.tree[root] = {
            "left": None, "right": None
        }

        for idx, val in enumerate(subset):
            if val == root:
                self.tree[root]["left"], cur = self.construct_tree(
                    cur+1, subset[:idx])
                self.tree[root]["right"], cur = self.construct_tree(
                    cur+1, subset[idx+1:])
                break

        return root, cur

    def postorder(self, node):
        if node is None:
            return ""

        s = ""
        s += self.postorder(self.tree[node]["left"])
        s += self.postorder(self.tree[node]["right"])
        s += node
        return s

    def get_postorder(self):
        self.root, cur = self.construct_tree(0, self.inorder)
        assert cur == len(self.preorder)-1
        return self.postorder(self.root)


if __name__ == '__main__':
    rd = stdin.readline

    while True:
        try:
            preorder, inorder = rd().strip().split()
        except Exception as e:
            break
            
        tr = TreeRepair(preorder, inorder)
        print(tr.get_postorder())
