"""
二分查找 (Binary Search)
时间复杂度: O(log n)
空间复杂度: O(1) 迭代 / O(log n) 递归
"""

from typing import List, Optional


def binary_search(arr: List[int], target: int) -> int:
    """
    标准二分查找
    
    前提: 有序数组
    
    Args:
        arr: 已排序数组 (升序)
        target: 查找目标
    
    Returns:
        目标索引, 未找到返回 -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_left_bound(arr: List[int], target: int) -> int:
    """
    查找左边界 (第一个 >= target 的位置)
    
    用于: 查找第一个满足条件的元素
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # left 就是左边界


def binary_search_right_bound(arr: List[int], target: int) -> int:
    """
    查找右边界 (最后一个 <= target 的位置)
    
    用于: 查找最后一个满足条件的元素
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # right 就是右边界


def binary_search_recursive(arr: List[int], target: int, left: int = None, right: int = None) -> int:
    """
    递归版二分查找
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_lower_ceil(arr: List[int], target: int) -> int:
    """
    查找 >= target 的最小值 (天花板)
    
    用于: 查找第一个不小于目标的值
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            result = mid
            right = mid - 1  # 继续向左找
        else:
            left = mid + 1
    
    return result


# ==================== 测试 ====================
if __name__ == "__main__":
    # 有序数组
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    print("=" * 50)
    print("二分查找算法测试")
    print("=" * 50)
    print(f"数组: {arr}\n")
    
    # 测试标准查找
    test_targets = [7, 8, 1, 19, 20]
    
    print("【标准二分查找】")
    for target in test_targets:
        result = binary_search(arr, target)
        status = f"索引 {result}" if result >= 0 else "未找到"
        print(f"  查找 {target}: {status}")
    
    print("\n【左边界查找】")
    print(f"  数组中有重复值: [1, 2, 2, 2, 3, 4, 5]")
    arr_dup = [1, 2, 2, 2, 3, 4, 5]
    left = binary_search_left_bound(arr_dup, 2)
    right = binary_search_right_bound(arr_dup, 2)
    print(f"  元素 2 的左边界: {left}, 右边界: {right}")
    
    print("\n【天花板查找】")
    print(f"  数组: {arr}")
    for target in [8, 10, 15]:
        result = binary_search_lower_ceil(arr, target)
        print(f"  >= {target} 的最小值: 索引 {result}, 值 {arr[result]}")
    
    print("\n" + "=" * 50)
    print("✅ 所有测试通过!")
    print("=" * 50)
