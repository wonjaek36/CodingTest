from sys import stdin


class CreateN(object):

    def __init__(self, n):
        self.n = str(n)
        self.n_len = len(str(n))
        self._ways = set()
        self.count = 0

    def num_append(self, nums: list, i: str, left_append: bool) -> list:
        new_nums = nums.copy()
        try:
            last = nums[-1]
        except:
            last = ""

        if left_append:
            new_nums.append(i+last)
        else:
            new_nums.append(last+i)
        return new_nums

    def _count_ways(self, nums):
        if self.n_len == len(nums):
            self.count += 1 
            if nums[-1] == self.n:
                self._ways.add(tuple(nums))
            return

        for i in range(10):
            left = self.num_append(nums, str(i), left_append=True)
            if left[-1] in self.n:
                self._count_ways(left)

            right = self.num_append(nums, str(i), left_append=False)
            if right[-1] in self.n:
                self._count_ways(right)

    def count_ways(self):
        self._count_ways([])
        # print(self._ways)
        return len(self._ways)


if __name__ == '__main__':
    n = int(stdin.readline())
    cn = CreateN(n)
    print(cn.count_ways())
