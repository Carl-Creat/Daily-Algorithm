"""
堆排序 (Heap Sort)

算法原理：
堆排序是一种基于二叉堆数据结构的比较排序算法。二叉堆是一个完全二叉树，分为最大堆和最小堆。
- 最大堆：每个节点的值都大于或等于其子节点的值
- 最小堆：每个节点的值都小于或等于其子节点的值

排序过程：
1. 构建最大堆：从最后一个非叶子节点开始，自底向上调整堆
2. 排序：将堆顶元素（最大值）与末尾元素交换，然后对剩余元素重新调整堆
3. 重复步骤2，直到所有元素有序

时间复杂度：O(n log n) - 所有情况下都是 O(n log n)
空间复杂度：O(1) - 原地排序

优点：
- 原地排序，不需要额外空间
- 时间复杂度稳定，不受输入数据影响
- 可以方便地实现优先队列

缺点：
- 不稳定排序（相同元素可能改变相对顺序）
- 对缓存不友好，实际性能可能不如快排
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    调整堆，使以 i 为根的子树满足最大堆性质
    
    参数:
        arr: 待调整的数组
        n: 堆的大小（有效元素个数）
        i: 当前需要调整的节点索引
    """
    largest = i          # 初始化最大值为当前节点
    left = 2 * i + 1     # 左子节点索引
    right = 2 * i + 2    # 右子节点索引
    
    # 如果左子节点存在且大于当前最大值
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # 如果右子节点存在且大于当前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # 如果最大值不是当前节点，交换并继续调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> List[int]:
    """
    堆排序主函数
    
    参数:
        arr: 待排序数组
    
    返回:
        排序后的数组
    """
    n = len(arr)
    
    # 第一步：构建最大堆
    # 从最后一个非叶子节点开始，自底向上调整
    # 最后一个非叶子节点索引为 n//2 - 1
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 第二步：逐个提取堆顶元素
    for i in range(n - 1, 0, -1):
        # 将堆顶（最大值）与当前末尾元素交换
        arr[0], arr[i] = arr[i], arr[0]
        # 对剩余元素重新调整堆
        heapify(arr, i, 0)
    
    return arr


# ============================================================
# LeetCode 实战题目
# ============================================================

"""
题目1: 数组中的第K个最大元素 (LeetCode 215)
难度: 中等

题目描述:
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例:
输入: [3,2,1,5,6,4], k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4
"""


def find_kth_largest(nums: List[int], k: int) -> int:
    """
    使用堆排序思想找第K大的元素
    优化：不需要完全排序，只需要执行k次堆调整
    
    时间复杂度: O(n + k log n) = O(n log n) 最坏情况
    空间复杂度: O(1)
    """
    n = len(nums)
    
    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    
    # 执行k-1次提取，第k次堆顶就是答案
    for i in range(n - 1, n - k, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)
    
    return nums[0]


"""
题目2: 排序数组 (LeetCode 912)
难度: 中等

题目描述:
给你一个整数数组 nums，请你将该数组升序排列。

示例:
输入: nums = [5,2,3,1]
输出: [1,2,3,5]

输入: nums = [5,1,1,2,0,0]
输出: [0,0,1,1,2,5]
"""


def sort_array(nums: List[int]) -> List[int]:
    """
    使用堆排序对数组进行排序
    
    时间复杂度: O(n log n)
    空间复杂度: O(1)
    """
    return heap_sort(nums)


"""
题目3: 数据流中的第K大元素 (LeetCode 703)
难度: 简单

题目描述:
设计一个找到数据流中第 k 大元素的类（class）。注意是排序后的第 k 大元素，
不是第 k 个不同的元素。

示例:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""

import heapq


class KthLargest:
    """
    使用最小堆维护前k大的元素
    堆顶就是第k大的元素
    
    时间复杂度: 
        - 构造函数: O(n log k)
        - add: O(log k)
    空间复杂度: O(k)
    """
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        """
        添加新元素并返回第k大的元素
        """
        # 如果堆大小小于k，直接加入
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # 如果新元素大于堆顶，替换堆顶
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        return self.min_heap[0]


# ============================================================
# 测试代码
# ============================================================

if __name__ == "__main__":
    # 测试堆排序
    print("=" * 50)
    print("堆排序测试")
    print("=" * 50)
    
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [1],
        [],
    ]
    
    for arr in test_cases:
        original = arr.copy()
        result = heap_sort(arr)
        print(f"原数组: {original}")
        print(f"排序后: {result}")
        print()
    
    # 测试 LeetCode 215
    print("=" * 50)
    print("LeetCode 215: 第K个最大元素测试")
    print("=" * 50)
    
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"数组: {nums1}, k={k1}")
    print(f"第{k1}大的元素: {find_kth_largest(nums1.copy(), k1)}")
    
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"数组: {nums2}, k={k2}")
    print(f"第{k2}大的元素: {find_kth_largest(nums2.copy(), k2)}")
    
    # 测试 LeetCode 703
    print()
    print("=" * 50)
    print("LeetCode 703: 数据流第K大元素测试")
    print("=" * 50)
    
    kth = KthLargest(3, [4, 5, 8, 2])
    print(f"add(3) -> {kth.add(3)}")
    print(f"add(5) -> {kth.add(5)}")
    print(f"add(10) -> {kth.add(10)}")
    print(f"add(9) -> {kth.add(9)}")
    print(f"add(4) -> {kth.add(4)}")
