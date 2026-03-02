# LeetCode So Easy

## 用法

```bash
uv sync                        # 装依赖
uv run pytest                  # 跑全部测试
uv run pytest -k "lc0088"      # 跑单题
uv run pytest tests/array/     # 跑某个 topic
uv run ruff check problems/    # 代码检查
```

## 结构

```
problems/<topic>/lc<NNNN>_<name>.py    # 题解
tests/<topic>/test_lc<NNNN>_<name>.py  # 测试
```

## 已完成

| # | 题目 | Topic | 难度 |
|---|------|-------|------|
| 58 | Length of Last Word | string | Easy |
| 69 | Sqrt(x) | binary_search | Easy |
| 88 | Merge Sorted Array | array | Easy |
| 93 | Restore IP Addresses | backtracking | Medium |
| 95 | Unique BST II | tree | Medium |
| 140 | Word Break II | backtracking | Hard |
| 241 | Different Ways to Add Parentheses | backtracking | Medium |
| 894 | All Possible Full Binary Trees | tree | Medium |
