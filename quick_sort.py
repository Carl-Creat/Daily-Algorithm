"""
快速排序 (Quick Sort)
时间复杂度: O(n log n) 平均, O(n²) 最坏
空间复杂度: O(log n)
稳定与否: 不稳定
"""

import random
from typing import List


def quick_sort(arr: List[int], low: int = 0, high: int = None) -> List[int]:
    """快速排序主函数"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr


def partition(arr: List[int], low: int, high: int) -> int:
    """分区操作"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 9, 1, 7, 6, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
    ]
    
    print("快速排序测试")
    for i, arr in enumerate(test_cases):
        original = arr.copy()
        sorted_arr = quick_sort(arr.copy())
        print(f"测试 {i + 1}: {original} -> {sorted_arr}")
