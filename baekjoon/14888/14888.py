from sys import stdin


class OperatorInserter(object):

    def __init__(self, operands, operators):
        self.operands = operands
        self.operators = operators
        self.mx = -0x7fffffff
        self.mi = 0x7fffffff

    def compute(self, operator, op1, op2):
        if operator == '+':
            return op1 + op2
        if operator == '-':
            return op1 - op2
        if operator == '*':
            return op1 * op2
        if operator == '/':
            if op1 < 0:
                return -((-op1) // op2)
            return op1 // op2
        assert False

    def recursive(self, pos, v):
        if pos >= len(self.operands):
            self.mx = max(v, self.mx)
            self.mi = min(v, self.mi)
            return

        for operator, idx in zip(['+', '-', '*', '/'], range(4)):
            if self.operators[idx] <= 0:
                continue

            nv = self.compute(operator, v, self.operands[pos])
            self.operators[idx] -= 1
            self.recursive(pos+1, nv)
            self.operators[idx] += 1


    def get_max_min(self):
        self.recursive(1, self.operands[0])
        return self.mx, self.mi


if __name__ == '__main__':
    rd = stdin.readline
    n = int(rd())
    operands = list(map(int, rd().split()))
    operators = list(map(int, rd().split()))
    
    oi = OperatorInserter(operands, operators)
    mx, mi = oi.get_max_min()
    print(mx)
    print(mi)
