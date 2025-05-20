# 🧩 LeetCode-Multilang Solutions

> **把刷题当成多语言闯关游戏**  
> 同一道题分别用 **Python / JavaScript / Go** 实现，配上可视化 Notebook，顺手练算法、写代码、学工程。

[![CI](https://github.com/<yourname>/leetcode-multilang/actions/workflows/ci.yml/badge.svg)](https://github.com/<yourname>/leetcode-multilang/actions)

---

## ✨ 项目亮点

- **三语对照**：直观比较不同语言的语法与性能取舍。  
- **算法类型分层**：`dynamic-programming/`, `backtracking/` … 查找复习更高效。  
- **自动脚本**：`./scripts/new_solution.sh 300 dynamic-programming` → 一键生成文件夹 + 代码骨架 + README 模板。  
- **Notebook 深讲**：高频/趣味题目用 Jupyter 可视化思路演进、复杂度分析。  
- **全链路 CI**：GitHub Actions 统一跑 `black + ruff`, `prettier + eslint`, `go vet + golangci-lint`，Push / PR 即验收。  
- **自动索引表**：提交后脚本更新顶层 README，将题号 ↔ 代码链接映射一目了然。  

---

## 🗂️ 目录结构

```text
.
├── dynamic-programming/
│   └── leetcode-300-LIS/
│       ├── solution.py
│       ├── solution.js
│       ├── solution.go
│       └── README.md          # 题目描述 & 解题思路
├── backtracking/
│   └── leetcode-46-Permutations/
│       └── ...
├── notebooks/
│   └── 42-trapping-rain-water.ipynb
├── scripts/
│   ├── new_solution.sh        # 生成题目骨架
│   └── update_index.py        # 自动刷新索引
├── .github/workflows/ci.yml
└── ...
