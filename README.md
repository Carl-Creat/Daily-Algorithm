# Daily-Algorithm

> 每日算法练习，持续更新中...

## 算法学习路线图

### 基础算法

| 算法 | 文件 | 难度 | 核心思想 |
|------|------|------|----------|
| 二分查找 | `binary_search.py` | ⭐ | 有序数组快速查找 |
| 斐波那契 | `fibonacci.py` | ⭐ | 递归/动态规划基础 |
| BFS 广度优先搜索 | `graph/bfs.py` | ⭐⭐ | 按层遍历 |
| DFS 深度优先搜索 | `graph/dfs.py` | ⭐⭐ | 递归深入探索 |

### 排序算法

| 算法 | 文件 | 时间复杂度 | 空间复杂度 |
|------|------|------------|------------|
| 归并排序 | `sorting/merge_sort.py` | O(n log n) | O(n) |
| 快速排序 | `sorting/quick_sort.py` | O(n log n) | O(log n) |
| 堆排序 | `sorting/heap_sort.py` | O(n log n) | O(1) |

### 图算法

| 算法 | 文件 | 难度 | 适用场景 |
|------|------|------|----------|
| BFS | `graph/bfs.py` | ⭐⭐ | 最短路径、无环遍历 |
| DFS | `graph/dfs.py` | ⭐⭐ | 路径搜索、连通分量 |
| Dijkstra | `graph/dijkstra.py` | ⭐⭐⭐ | 单源最短路径 |
| 拓扑排序 | `graph/topological_sort.py` | ⭐⭐⭐ | 依赖排序、任务调度 |

### 高级技巧

| 算法 | 文件 | 难度 | 核心思想 |
|------|------|------|----------|
| 并查集 | `union_find.py` | ⭐⭐ | 集合合并与查询 |
| 滑动窗口 | `sliding_window.py` | ⭐⭐ | 子数组优化 |
| 前缀和 | `prefix_sum.py` | ⭐⭐ | 区间和快速查询 |

### 动态规划 (DP)

| 文件夹 | 内容 |
|--------|------|
| `dp/` | 各类 DP 问题 |

---

## 学习建议

### 入门阶段 (1-2周)
1. **排序算法**：理解时间/空间复杂度
2. **二分查找**：高频面试题
3. **BFS/DFS**：图入门必备

### 进阶阶段 (2-4周)
1. **滑动窗口**：子数组问题必杀技
2. **前缀和**：区间查询杀手锏
3. **并查集**：连通性问题克星
4. **Dijkstra**：最短路径经典

### 高级阶段 (4周+)
1. **动态规划**：最难题型，多练多总结
2. **高级图算法**：网络流、强连通分量
3. **数学算法**：数论、组合数学

---

## 代码结构

```
Daily-Algorithm/
├── README.md              # 本文件
├── binary_search.py       # 二分查找
├── fibonacci.py          # 斐波那契
├── bfs.py                # 广度优先搜索
├── merge_sort.py         # 归并排序
├── quick_sort.py         # 快速排序
├── union_find.py         # 并查集
├── sliding_window.py     # 滑动窗口
├── prefix_sum.py         # 前缀和
│
├── sorting/              # 排序算法目录
│   ├── heap_sort.py
│   ├── merge_sort.py
│   └── quick_sort.py
│
├── graph/                # 图算法目录
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   └── topological_sort.py
│
├── dp/                   # 动态规划目录
│   └── ...
│
├── searching/            # 搜索算法目录
│   └── ...
│
└── requirements.txt     # Python 依赖
```

---

## 快速运行

```bash
# 克隆仓库
git clone https://github.com/Carl-Creat/Daily-Algorithm.git
cd Daily-Algorithm

# 运行单个算法文件
python binary_search.py
python union_find.py
python sliding_window.py
python prefix_sum.py
```

---

## 贡献指南

欢迎提交 PR 完善仓库！

1. Fork 本仓库
2. 创建新分支 (`git checkout -b feature/新算法`)
3. 添加代码和注释
4. 提交更改 (`git commit -m '添加 xxx 算法'`)
5. 推送到分支 (`git push origin feature/新算法`)
6. 提交 Pull Request

---

## 相关资源

- [LeetCode](https://leetcode.com/) - 算法练习平台
- [算法可视化](https://visualgo.net/) - 可视化学习算法
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/) - 时间复杂度速查

---

## 更新日志

- **2026-03-21**: 新增堆排序、拓扑排序、Dijkstra、并查集、滑动窗口、前缀和
- **2026-03-20**: 初始化仓库

---

*Keep practicing, keep improving!*
