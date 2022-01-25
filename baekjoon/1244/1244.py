import sys

class Switches(object):

    def __init__(self):
        self.N = None
        self.switches = None
        self.T = None
        self.students = None

    def input(self):
        self.N = int(sys.stdin.readline().rstrip())
        self.switches = sys.stdin.readline().rstrip().split(' ')
        self.T = int(sys.stdin.readline().rstrip())
        self.students = []
        for i in range(self.T):
            self.students.append(
                list(map(lambda x: int(x),
                     sys.stdin.readline().rstrip().split(' '))))

    def get_last_state(self):
        for gender, n in self.students:
            if gender == 1:
                self.manipulate_by_boy(n)
            else:
                self.manipulate_by_girl(n)

    def change_status(self, n):
        if self.switches[n-1] == '1':
            self.switches[n-1] = '0'
        else:
            self.switches[n-1] = '1'

    def find_same_status_switches(self, n):
        length = 0
        n -= 1
        while n-length >= 0 and n+length < self.N:
            if self.switches[n-length] != self.switches[n+length]:
                break
            length += 1
        return length-1

    def manipulate_by_boy(self, n):
        for i in range(n, self.N+1, n):
            self.change_status(i)

    def manipulate_by_girl(self, n):
        l = self.find_same_status_switches(n)
        for i in range(n-l, n+l+1):
            self.change_status(i)
        

if __name__ == '__main__':
    switches = Switches()
    switches.input()
    switches.get_last_state()
    for i in range(0, switches.N, 20):
        print(' '.join(switches.switches[i:i+20]))
