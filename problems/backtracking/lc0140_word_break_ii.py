"""
LeetCode 140. Word Break II
https://leetcode.com/problems/word-break-ii/

Difficulty: Hard | Priority: P1 | Topic: backtracking, dp

## 思路
- 递归 + 记忆化：遍历所有可能前缀，若在字典中则递归处理后缀
- memo[s] 存储字符串 s 能拆分成的所有句子

## 复杂度
- Time: O(n * 2^n)  — 最坏情况指数级，但记忆化大幅剪枝
- Space: O(n * 2^n)

## 边界条件
- 空字符串 -> []
- 字典中没有任何匹配 -> []
- 整个字符串就是一个单词

## 常见 Bug 审计
1. base case：空串应返回 [] 还是 [""]，取决于实现方式
2. 记忆化 key 用子串 vs 索引，两种都可以
3. 拼接时 prefix + " " + suffix 在 suffix 为空时会多一个空格
"""
class Solution:
    def word_break(self, s: str, word_dict: list[str]) -> list[str]:
        word_set = set(word_dict)
        memo: dict[str, list[str]] = {}

        def solve(s: str) -> list[str]:
            if s in memo:
                return memo[s]

            if not s:
                return []

            results = []

            for i in range(1, len(s) + 1):
                prefix = s[:i]
                if prefix in word_set:
                    if i == len(s):
                        results.append(prefix)
                    else:
                        for sub in solve(s[i:]):
                            results.append(prefix + " " + sub)

            memo[s] = results
            return results

        return solve(s)
