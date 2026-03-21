"""
归并排序 (Merge Sort)
时间复杂度: O(n log n) - 始终如一
空间复杂度: O(n)
稳定与否: 稳定
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    归并排序 - 分治法经典实现
    
    原理:
    1. 分解: 将数组分成两半
    2. 递归: 对两半分别排序
    3. 合并: 将两个有序数组合并
    
    Args:
        arr: 待排序数组
    
    Returns:
        排序后的新数组
    """
    if len(arr) <= 1:
        return arr
    
    # 分解: 找到中点
    mid = len(arr) // 2
    
    # 递归排序左右两部分
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 合并两个有序数组
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    合并两个有序数组
    
    使用双指针法, 时间复杂度 O(n)
    """
    result = []
    i = j = 0
    
    # 同时遍历两个数组, 选择较小的元素
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余元素
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_inplace(arr: List[int], left: int = None, right: int = None) -> None:
    """
    原地归并排序 (节省空间但复杂)
    """
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    
    if left < right:
        mid = (left + right) // 2
        
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        
        # 原地合并
        merge_inplace(arr, left, mid, right)


def merge_inplace(arr: List[int], left: int, mid: int, right: int) -> None:
    """原地合并操作"""
    # 复制左半部分
    left_copy = arr[left:mid + 1]
    # 右半部分的起始位置
    i, j, k = 0, mid + 1, left
    
    while i < len(left_copy) and j <= right:
        if left_copy[i] <= arr[j]:
            arr[k] = left_copy[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1
    
    # 复制剩余元素
    while i < len(left_copy):
        arr[k] = left_copy[i]
        i += 1
        k += 1


# ==================== 测试 ====================
if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 9, 1, 7, 6, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
        [1],
        [],
        [3, 3, 3, 1, 1, 2, 2],
    ]
    
    print("=" * 50)
    print("归并排序算法测试")
    print("=" * 50)
    
    for i, arr in enumerate(test_cases):
        original = arr.copy()
        sorted_arr = merge_sort(arr.copy())
        print(f"\n测试 {i + 1}:")
        print(f"  输入: {original}")
        print(f"  输出: {sorted_arr}")
        assert sorted_arr == sorted(original)
    
    print("\n" + "=" * 50)
    print("✅ 所有测试通过!")
    print("=" * 50)
