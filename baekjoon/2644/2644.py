import sys

class KinshipDegreeCalculator(object):

    def __init__(self, N, ancestors):
        self.N = N
        self.ancestors = ancestors
        self.parents = [-1 for _ in range(N+1)]
        for p, c in self.ancestors:        
            self.parents[c] = p

    def _get_kinship_degree_ancestors(self, p, c, degrees):
        if p == -1:
            return
        degrees[p] = c
        self._get_kinship_degree_ancestors(
            self.parents[p], c+1, degrees)
    
    def get_kinship_degree(self, A, B):
        A_degrees = [-1 for _ in range(self.N+1)]
        B_degrees = [-1 for _ in range(self.N+1)]
        self._get_kinship_degree_ancestors(A, 0, A_degrees)
        self._get_kinship_degree_ancestors(B, 0, B_degrees)

        degree = self.N + 1
        for a_d, b_d in zip(A_degrees, B_degrees):
            if a_d >= 0 and b_d >= 0:
                degree = min(degree, a_d + b_d)

        return degree if degree != self.N+1 else -1

if __name__ == '__main__':
    T = int(sys.stdin.readline())
    A, B = list(map(lambda x: int(x), sys.stdin.readline().split(' ')))
    m = int(sys.stdin.readline())
    ancestors = []
    for i in range(m):
        ancestors.append(
            list(map(lambda x: int(x), sys.stdin.readline().split(' '))))

    calc = KinshipDegreeCalculator(T, ancestors)
    print(calc.get_kinship_degree(A, B))
    


