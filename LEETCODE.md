# LeetCode 题目对照表

本仓库每个算法都对应若干 LeetCode 经典题目，方便学完算法后直接上手练习。

## 基础算法

| 算法 | 文件 | LeetCode 题目 |
|------|------|--------------|
| 二分查找 | `binary_search.py` | [704](https://leetcode.cn/problems/binary-search/) · [35](https://leetcode.cn/problems/search-insert-position/) · [33](https://leetcode.cn/problems/search-in-rotated-sorted-array/) · [153](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/) |
| 斐波那契/DP | `fibonacci.py` | [509](https://leetcode.cn/problems/fibonacci-number/) · [70](https://leetcode.cn/problems/climbing-stairs/) · [198](https://leetcode.cn/problems/house-robber/) · [322](https://leetcode.cn/problems/coin-change/) |
| BFS | `bfs.py` | [102](https://leetcode.cn/problems/binary-tree-level-order-traversal/) · [200](https://leetcode.cn/problems/number-of-islands/) · [994](https://leetcode.cn/problems/rotting-oranges/) · [127](https://leetcode.cn/problems/word-ladder/) |
| 并查集 | `union_find.py` | [547](https://leetcode.cn/problems/number-of-provinces/) · [684](https://leetcode.cn/problems/redundant-connection/) · [1584](https://leetcode.cn/problems/min-cost-to-connect-all-points/) |
| 滑动窗口 | `sliding_window.py` | [209](https://leetcode.cn/problems/minimum-size-subarray-sum/) · [3](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) · [76](https://leetcode.cn/problems/minimum-window-substring/) · [438](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) |
| 前缀和 | `prefix_sum.py` | [303](https://leetcode.cn/problems/range-sum-query-immutable/) · [560](https://leetcode.cn/problems/subarray-sum-equals-k/) · [304](https://leetcode.cn/problems/range-sum-query-2d-immutable/) |

## 排序算法

| 算法 | 文件 | LeetCode 题目 |
|------|------|--------------|
| 归并排序 | `sorting/merge_sort.py` | [912](https://leetcode.cn/problems/sort-an-array/) · [148](https://leetcode.cn/problems/sort-list/) · [315](https://leetcode.cn/problems/count-of-smaller-numbers-after-self/) |
| 快速排序 | `sorting/quick_sort.py` | [912](https://leetcode.cn/problems/sort-an-array/) · [215](https://leetcode.cn/problems/kth-largest-element-in-an-array/) |
| 堆排序 | `sorting/heap_sort.py` | [912](https://leetcode.cn/problems/sort-an-array/) · [347](https://leetcode.cn/problems/top-k-frequent-elements/) · [23](https://leetcode.cn/problems/merge-k-sorted-lists/) |

## 图算法

| 算法 | 文件 | LeetCode 题目 |
|------|------|--------------|
| BFS | `graph/bfs.py` | [102](https://leetcode.cn/problems/binary-tree-level-order-traversal/) · [200](https://leetcode.cn/problems/number-of-islands/) · [994](https://leetcode.cn/problems/rotting-oranges/) |
| DFS | `graph/dfs.py` | [200](https://leetcode.cn/problems/number-of-islands/) · [130](https://leetcode.cn/problems/surrounded-regions/) · [417](https://leetcode.cn/problems/pacific-atlantic-water-flow/) |
| Dijkstra | `graph/dijkstra.py` | [743](https://leetcode.cn/problems/network-delay-time/) · [787](https://leetcode.cn/problems/cheapest-flights-within-k-stops/) · [1514](https://leetcode.cn/problems/path-with-maximum-probability/) |
| 拓扑排序 | `graph/topological_sort.py` | [207](https://leetcode.cn/problems/course-schedule/) · [210](https://leetcode.cn/problems/course-schedule-ii/) · [269](https://leetcode.cn/problems/alien-dictionary/) |

## 动态规划

| 题型 | 文件 | LeetCode 题目 |
|------|------|--------------|
| 基础 DP | `dp/fibonacci.py` | [509](https://leetcode.cn/problems/fibonacci-number/) · [70](https://leetcode.cn/problems/climbing-stairs/) · [746](https://leetcode.cn/problems/min-cost-climbing-stairs/) |

---

## 推荐刷题顺序

### 第一周：基础打底
1. [704 二分查找](https://leetcode.cn/problems/binary-search/) ⭐
2. [509 斐波那契数](https://leetcode.cn/problems/fibonacci-number/) ⭐
3. [70 爬楼梯](https://leetcode.cn/problems/climbing-stairs/) ⭐
4. [200 岛屿数量](https://leetcode.cn/problems/number-of-islands/) ⭐⭐

### 第二周：排序与图
5. [912 排序数组](https://leetcode.cn/problems/sort-an-array/) ⭐⭐
6. [215 第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) ⭐⭐
7. [207 课程表](https://leetcode.cn/problems/course-schedule/) ⭐⭐
8. [743 网络延迟时间](https://leetcode.cn/problems/network-delay-time/) ⭐⭐⭐

### 第三周：高级技巧
9. [3 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) ⭐⭐
10. [76 最小覆盖子串](https://leetcode.cn/problems/minimum-window-substring/) ⭐⭐⭐
11. [560 和为K的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) ⭐⭐
12. [547 省份数量](https://leetcode.cn/problems/number-of-provinces/) ⭐⭐
