"""
LeetCode 88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

Difficulty: Easy | Priority: P0 | Topic: array, two_pointers

## 思路
- 核心不变量：从后往前填充，p 指针始终指向下一个待填充位置
- 双指针从尾部开始比较，大的放到 nums1 末尾

## 复杂度
- Time: O(m + n)
- Space: O(1)

## 边界条件
- nums2 为空 (n=0)
- nums1 原有元素全部小于 nums2
- nums1 原有元素全部大于 nums2

## 常见 Bug 审计
1. 忘记处理 p2 还有剩余的情况（p1 先耗尽）
2. p1 耗尽时不需要额外处理（nums1 前面的元素已经在正确位置）——但其实 p2 剩余才需要拷贝
3. 循环条件用 > 而非 >= 导致漏处理索引 0
"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
