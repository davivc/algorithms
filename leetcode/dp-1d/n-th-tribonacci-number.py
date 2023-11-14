class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        tri = [0,1,1]
        val = 2

        for i in range(3, n, 1):
            tri.pop(0)
            tri.append(val)
            val = tri[0] + tri[1] + tri[2]

        return val