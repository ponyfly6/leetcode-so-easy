# binary search
# 找到一个最大的整数使得平方小于等于x


class Solution:

    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        left, right, ans = 0, x, 0

        while left <= right:
            mid = left + (right - left) // 2

            square = mid * mid
            if square == x:
                return square
            elif square < x:
                left = mid + 1
                ans = mid      # mid 是一个潜在的答案 (防不胜防，这个就像是搜索过程中设置的一个安全点或记忆点)
            else:
                right = mid - 1

        return ans

