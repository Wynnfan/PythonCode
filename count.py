class Solution:
    def fib(self, n):
        first ,second = 0, 1
        if n ==1 or n == 0:
            return first
        elif n == 2:
            return 1
        for i in range(2, n):
            temp = first
            first = second
            second += temp
        return second
rec = Solution
rec.fib(10)