"""
LeetCode 241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/

Difficulty: Medium | Priority: P1 | Topic: backtracking, math

## 思路
- 分治：以每个运算符为分割点，递归计算左右两部分
- 笛卡尔积合并左右子问题的所有结果

## 复杂度
- Time: O(Catalan(n)) — n 为运算符个数
- Space: O(Catalan(n))

## 边界条件
- 纯数字表达式（无运算符）-> [数字本身]
- 单个运算符
- 含负数结果

## 常见 Bug 审计
1. isdigit() 对多位数也返回 True，所以 base case 判断正确
2. 运算符后面的 expression[i+1:] 别越界
3. 忘记处理减法导致负数的情况
"""
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])

                for l in left_results:
                    for r in right_results:
                        if char == "+":
                            results.append(l + r)
                        elif char == "-":
                            results.append(l - r)
                        else:
                            results.append(l * r)

        return results
