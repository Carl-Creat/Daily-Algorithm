"""二分查找 (Binary Search)"""

def binary_search(arr, target):
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

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))  # 输出: 3
