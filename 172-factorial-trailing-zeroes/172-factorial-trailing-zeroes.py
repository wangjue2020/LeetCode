class Solution:
    def trailingZeroes(self, n: int) -> int:
        factorial = 1
        two = 0
        five = 0
        for i in range(1, n+1):
            if i%2 == 0:
                two += self.power(2, i)
            if i%5 == 0:
                five += self.power(5, i)
        return min(two,five)

        return ans
    def power(self, base, n):
        ans = 0
        while n % base == 0:
            ans += 1
            n /= base
        return ans