"""
LeetCode 69. Sqrt(x)
https://leetcode.com/problems/sqrtx/

Difficulty: Easy | Priority: P0 | Topic: binary_search, math

## 思路
- 核心不变量：找到最大整数 k 使得 k*k <= x
- 二分搜索 [0, x]，维护 ans 记录最后一个满足条件的 mid

## 复杂度
- Time: O(log x)
- Space: O(1)

## 边界条件
- x = 0 -> 0
- x = 1 -> 1
- 大数（不会溢出，Python 无整数溢出）

## 常见 Bug 审计
1. square == x 时应该返回 mid 而不是 square（原代码有此 bug）
2. 忘记 x=0 的特殊处理
3. 二分区间取 [0, x] 对 x=1 时也能工作
"""


class Solution:
    def my_sqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left, right, ans = 0, x, 0

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return ans
