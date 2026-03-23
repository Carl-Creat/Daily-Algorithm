"""
算法单元测试 - 对应 LeetCode 题目已在注释中标注
运行: pytest tests/test_algorithms.py -v
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from binary_search import binary_search
from fibonacci import fib, fib_optimized
from bfs import bfs
from merge_sort import merge_sort
from quick_sort import quick_sort
from union_find import UnionFind
from sliding_window import max_sum_subarray, min_window_substring
from prefix_sum import PrefixSum
from sorting.heap_sort import heap_sort
from graph.dijkstra import dijkstra
from graph.topological_sort import topological_sort_kahn


# ==================== 二分查找 ====================
# LeetCode: 704, 35, 33, 153
class TestBinarySearch:
    def test_found(self):
        assert binary_search([1, 3, 5, 7, 9], 7) == 3

    def test_not_found(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1

    def test_single_element_found(self):
        assert binary_search([5], 5) == 0

    def test_single_element_not_found(self):
        assert binary_search([5], 3) == -1

    def test_empty(self):
        assert binary_search([], 1) == -1

    def test_first_element(self):
        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_last_element(self):
        assert binary_search([1, 2, 3, 4, 5], 5) == 4


# ==================== 斐波那契 ====================
# LeetCode: 509, 70, 198, 322
class TestFibonacci:
    def test_base_cases(self):
        assert fib(0) == 0
        assert fib(1) == 1

    def test_fib_10(self):
        assert fib(10) == 55

    def test_fib_20(self):
        assert fib(20) == 6765

    def test_optimized_matches(self):
        for i in range(15):
            assert fib(i) == fib_optimized(i)


# ==================== BFS ====================
# LeetCode: 102, 200, 994, 127
class TestBFS:
    def test_basic(self):
        graph = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}
        result = bfs(graph, 1)
        assert result[0] == 1
        assert set(result) == {1, 2, 3, 4, 5}

    def test_single_node(self):
        assert bfs({1: []}, 1) == [1]

    def test_disconnected(self):
        graph = {1: [2], 2: [], 3: [4], 4: []}
        result = bfs(graph, 1)
        assert result == [1, 2]


# ==================== 归并排序 ====================
# LeetCode: 912, 148, 315
class TestMergeSort:
    def test_basic(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([1]) == [1]

    def test_reverse(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert merge_sort([3, 3, 1, 1]) == [1, 1, 3, 3]


# ==================== 快速排序 ====================
# LeetCode: 912, 215
class TestQuickSort:
    def test_basic(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert quick_sort(arr) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_empty(self):
        assert quick_sort([]) == []

    def test_single(self):
        assert quick_sort([42]) == [42]

    def test_reverse(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


# ==================== 堆排序 ====================
# LeetCode: 912, 347, 23
class TestHeapSort:
    def test_basic(self):
        assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_empty(self):
        assert heap_sort([]) == []

    def test_single(self):
        assert heap_sort([7]) == [7]

    def test_reverse(self):
        assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


# ==================== 并查集 ====================
# LeetCode: 547, 684, 200, 1584
class TestUnionFind:
    def test_basic_union_find(self):
        uf = UnionFind(5)
        assert uf.count == 5
        uf.union(0, 1)
        assert uf.find(0) == uf.find(1)
        assert uf.count == 4

    def test_connected(self):
        uf = UnionFind(4)
        uf.union(0, 1)
        uf.union(2, 3)
        assert uf.connected(0, 1)
        assert uf.connected(2, 3)
        assert not uf.connected(0, 2)

    def test_chain_union(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(2, 3)
        assert uf.connected(0, 3)
        assert uf.count == 2


# ==================== 滑动窗口 ====================
# LeetCode: 209, 3, 76, 438
class TestSlidingWindow:
    def test_max_sum_subarray(self):
        assert max_sum_subarray([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16

    def test_min_window(self):
        result = min_window_substring("ADOBECODEBANC", "ABC")
        assert result == "BANC"

    def test_min_window_no_result(self):
        assert min_window_substring("A", "AA") == ""


# ==================== 前缀和 ====================
# LeetCode: 303, 560, 304
class TestPrefixSum:
    def test_range_sum(self):
        ps = PrefixSum([1, 2, 3, 4, 5])
        assert ps.range_sum(0, 4) == 15
        assert ps.range_sum(1, 3) == 9
        assert ps.range_sum(2, 2) == 3

    def test_subarray_sum_equals_k(self):
        ps = PrefixSum([1, 1, 1])
        assert ps.subarray_sum_equals_k(2) == 2


# ==================== Dijkstra ====================
# LeetCode: 743, 787, 1514
class TestDijkstra:
    def test_basic(self):
        graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        dist = dijkstra(graph, 0, 4)
        assert dist[0] == 0
        assert dist[1] == 3
        assert dist[2] == 1
        assert dist[3] == 4

    def test_unreachable(self):
        graph = {0: [(1, 1)], 1: [], 2: []}
        dist = dijkstra(graph, 0, 3)
        assert dist[2] == float('inf')


# ==================== 拓扑排序 ====================
# LeetCode: 207, 210, 269
class TestTopologicalSort:
    def test_basic(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        result = topological_sort_kahn(graph, 4)
        assert result is not None
        assert result.index(0) < result.index(1)
        assert result.index(0) < result.index(2)
        assert result.index(1) < result.index(3)

    def test_cycle_detection(self):
        graph = {0: [1], 1: [2], 2: [0]}
        result = topological_sort_kahn(graph, 3)
        assert result is None
