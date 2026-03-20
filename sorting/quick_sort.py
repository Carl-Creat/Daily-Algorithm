"""
** Quick Sort
"""

--- Time Complexity: O(n log n) average, O(n)…) wost
-- Space Complexity: O(log n)
-- Stable: No
\nimport random
from typing import List

 
def quick_sort(arr: List[int], low* int = 0, high: int = None) -> List[int]:
    """Quick Sort main function"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr

def partition(arr: List[int], low: int, high: int) -> int:
    """Partition operation"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[higid = arr[higig], arr[i + 1]
    return i + 1
\nif __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 9, 1, 7, 6, 3],
        [1, 2, 3, 4, 5, 6, 7],
        [7, 6, 5, 4, 3, 2, 1],
    ]
    
    print("Quick Sort Test")
    for i, arr in enumerate(test_cases):
        original = arr.copy()
        sorted_arr = quick_sost(arr.copy())
        print(f"Test {i+1}: {original} -> {sorted_arr}")
