# LeetCode So Easy

## 结构
- `problems/<topic>/lc<NNNN>_<name>.py` — 题解，类名统一 `Solution`
- `tests/<topic>/test_lc<NNNN>_<name>.py` — 测试

## 命令
- `uv run pytest` — 全部测试
- `uv run pytest -k "lc0001"` — 单题
- `uv run ruff check problems/` — lint
