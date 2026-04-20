"""
LeetCode 93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Difficulty: Medium | Priority: P0 | Topic: string, backtracking

## 思路
- 回溯：每次截取 1-3 位，验证合法性（0-255，无前导零）
- path 记录已选段，满 4 段且用完所有字符时收集结果

## 复杂度
- Time: O(3^4) = O(81)  — 常数级，最多 4 段每段最多 3 位
- Space: O(1)  — 不计输出

## 边界条件
- 长度 < 4 或 > 12 -> []
- 全 0 -> ["0.0.0.0"]
- 含前导零的段无效（"01" 不合法）

## 常见 Bug 审计
1. 前导零判断：len > 1 且首位为 '0' 要排除
2. 忘记 start_index == len(s) 的终止条件
3. 段数到 4 但字符没用完时要剪枝
"""
class Solution:
    def restore_ip_addresses(self, s: str) -> list[str]:
        results = []
        path: list[str] = []
        self._backtrack(s, 0, path, results)
        return results

    def _backtrack(self, s: str, start_index: int, path: list[str], results: list[str]):
        if len(path) == 4 and start_index == len(s):
            results.append(".".join(path))
            return

        if len(path) == 4:
            return

        for i in range(1, 4):
            if start_index + i > len(s):
                break
            segment = s[start_index:start_index + i]
            if self._is_valid_segment(segment):
                path.append(segment)
                self._backtrack(s, start_index + i, path, results)
                path.pop()

    def _is_valid_segment(self, segment: str) -> bool:
        if len(segment) > 1 and segment[0] == "0":
            return False
        return 0 <= int(segment) <= 255
