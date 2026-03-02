"""
LeetCode 58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Difficulty: Easy | Priority: P0 | Topic: string

## 思路
- 从尾部跳过空格，再计数非空格字符

## 复杂度
- Time: O(n)
- Space: O(1)

## 边界条件
- 全空格字符串 -> 0
- 单个单词无空格
- 末尾有多个空格

## 常见 Bug 审计
1. 没有先跳过末尾空格就开始计数
2. 空字符串没有处理（题目保证至少一个单词，但防御性考虑）
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        i = n - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        if i < 0:
            return 0

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
