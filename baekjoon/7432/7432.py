from sys import stdin


class DiscTree(object):

    class Node(object):
        def __init__(self, name):
            self.name = name
            self.children = {}

        def get_node(self, name):
            if name not in self.children:
                self.children[name] = self.__class__(name) 
            return self.children[name]

    def __init__(self, pathes):
        self._pathes = pathes
        self._root = self.Node('')

    def create_tree(self):
        for path in self._pathes:
            names = path.split('\\')
            cur = self._root
            for n in names:
                cur = cur.get_node(n)

    def print_tree(self):
        self._pprint(self._root, -1)

    def _pprint(self, cur, depth):
        if depth >= 0:
            print(f"{' '*depth}{cur.name}")

        for _, node in sorted(cur.children.items()):
            self._pprint(node, depth+1)


if __name__ == '__main__':
    n = int(stdin.readline())
    pathes = [stdin.readline().rstrip() for _ in range(n)]

    dt = DiscTree(pathes)
    dt.create_tree()
    dt.print_tree()

