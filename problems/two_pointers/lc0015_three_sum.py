"""
LeetCode 15. 3Sum
https://leetcode.com/problems/3sum/

Difficulty: Medium | Topic: two_pointers

## 思路
- 排序 + 双指针
- 固定一个数 nums[i]，在 [i+1, n-1] 区间用双指针找两数之和 = -nums[i]
- 跳过重复元素避免重复三元组

## 复杂度
- Time: O(n^2)
- Space: O(1)（不计输出）

## 边界条件
- 数组长度 < 3 -> []
- 全 0 -> [[0,0,0]]
- 无解 -> []

## 常见 Bug 审计
1. 忘记对 i 去重（nums[i] == nums[i-1] 时跳过）
2. 忘记对 left/right 去重（找到解后要跳过相同值）
3. i 去重条件写成 nums[i] == nums[i+1] 会漏解
4. nums[i] > 0 时可以提前 break（排序后三数之和不可能为 0）
"""


class Solution:
    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # 提前终止：三数之和不可能为 0
            if nums[i] > 0:
                break
            # 跳过重复元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # 跳过重复元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result
