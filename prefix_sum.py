"""
前缀和 (Prefix Sum)

前缀和是一种预处理技巧，用于快速计算数组某个区间的和。
核心思想：预先计算从数组开头到每个位置的累加和，
通过 sum[j] - sum[i-1] 快速得到区间 [i, j] 的和。

适用场景：
- 频繁查询子数组和
- 子数组和等于某个值的问题
- 二维矩阵区域和查询

时间复杂度：
- 预处理：O(n)
- 查询：O(1)

空间复杂度：O(n)
"""

from typing import List, Dict, Optional
from collections import defaultdict


class PrefixSum:
    """
    前缀和类
    
    Attributes:
        prefix: 前缀和数组，prefix[i] 表示 nums[0..i-1] 的和
    """
    
    def __init__(self, nums: List[int]):
        """初始化前缀和数组"""
        n = len(nums)
        self.prefix = [0] * (n + 1)
        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]
    
    def range_sum(self, left: int, right: int) -> int:
        """
        计算区间 [left, right] 的和（包含两端）
        
        Args:
            left: 左边界索引
            right: 右边界索引
        
        Returns:
            区间和
        """
        return self.prefix[right + 1] - self.prefix[left]
    
    def total_sum(self) -> int:
        """返回整个数组的和"""
        return self.prefix[-1]


# ============== LeetCode 实战 ==============

def leetcode_303_range_sum_query():
    """
    LeetCode 303. 区域和检索 - 数组不可变
    https://leetcode.com/problems/range-sum-query-immutable/
    
    给定一个整数数组 nums，处理多个查询：
    sumRange(left, right) 返回数组 nums 中索引 left 和 right（包含）之间的元素的和。
    
    示例：
        NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
        numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
        numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
    """
    class NumArray:
        """使用前缀和实现区域和查询"""
        
        def __init__(self, nums: List[int]):
            self.prefix = [0] * (len(nums) + 1)
            for i in range(len(nums)):
                self.prefix[i + 1] = self.prefix[i] + nums[i]
        
        def sumRange(self, left: int, right: int) -> int:
            return self.prefix[right + 1] - self.prefix[left]
    
    # 测试用例
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    
    test_cases = [
        (0, 2, 1),
        (2, 5, -1),
        (0, 5, -3),
    ]
    
    print("=== LeetCode 303: 区域和检索 ===")
    for i, (left, right, expected) in enumerate(test_cases, 1):
        result = num_array.sumRange(left, right)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_560_subarray_sum_equals_k():
    """
    LeetCode 560. 和为 K 的子数组
    https://leetcode.com/problems/subarray-sum-equals-k/
    
    给你一个整数数组 nums 和一个整数 k，请你统计并返回该数组中和为 k 的连续子数组的个数。
    
    示例：
        输入: nums = [1,1,1], k = 2
        输出: 2
        解释: 有两个子数组和为 2: [1,1]（索引 0-1）和 [1,1]（索引 1-2）
    """
    def subarray_sum(nums: List[int], k: int) -> int:
        """
        使用前缀和 + 哈希表优化
        
        思路：
        - prefix[j] - prefix[i-1] = k
        - prefix[i-1] = prefix[j] - k
        - 用哈希表记录每个前缀和出现的次数
        """
        count = 0
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # 前缀和为 0 的情况
        
        for num in nums:
            prefix_sum += num
            # 查找之前有多少个前缀和等于 prefix_sum - k
            count += prefix_count[prefix_sum - k]
            prefix_count[prefix_sum] += 1
        
        return count
    
    # 测试用例
    test_cases = [
        ([1,1,1], 2, 2),
        ([1,2,3], 3, 2),
        ([1,-1,0], 0, 3),
    ]
    
    print("\n=== LeetCode 560: 和为 K 的子数组 ===")
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = subarray_sum(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_974_subarray_sums_divisible_by_k():
    """
    LeetCode 974. 和可被 K 整除的子数组
    https://leetcode.com/problems/subarray-sums-divisible-by-k/
    
    给定一个整数数组 nums 和一个整数 k，返回其中元素之和可被 k 整除的（连续、非空）子数组的数目。
    
    示例：
        输入: nums = [4,5,0,-2,-3,1], k = 5
        输出: 7
        解释: 有 7 个子数组满足其元素之和可被 k = 5 整除：
              [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    """
    def subarrays_div_by_k(nums: List[int], k: int) -> int:
        """
        使用前缀和 + 同余定理
        
        思路：
        - (prefix[j] - prefix[i-1]) % k == 0
        - prefix[j] % k == prefix[i-1] % k
        - 统计相同余数的前缀和个数
        """
        count = 0
        prefix_sum = 0
        remainder_count = defaultdict(int)
        remainder_count[0] = 1  # 余数为 0 的情况
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            # 处理负数余数
            if remainder < 0:
                remainder += k
            
            count += remainder_count[remainder]
            remainder_count[remainder] += 1
        
        return count
    
    # 测试用例
    test_cases = [
        ([4,5,0,-2,-3,1], 5, 7),
        ([5], 9, 0),
    ]
    
    print("\n=== LeetCode 974: 和可被 K 整除的子数组 ===")
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        result = subarrays_div_by_k(nums, k)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_304_range_sum_query_2d():
    """
    LeetCode 304. 二维区域和检索 - 矩阵不可变
    https://leetcode.com/problems/range-sum-query-2d-immutable/
    
    给定一个二维矩阵 matrix，处理多个查询：
    sumRegion(row1, col1, row2, col2) 返回左上角 (row1, col1)、右下角 (row2, col2) 的子矩阵的元素和。
    
    示例：
        给定 matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
        ]
        sumRegion(2, 1, 4, 3) -> 8
    """
    class NumMatrix:
        """使用二维前缀和实现区域和查询"""
        
        def __init__(self, matrix: List[List[int]]):
            if not matrix or not matrix[0]:
                return
            
            m, n = len(matrix), len(matrix[0])
            # prefix[i][j] 表示从 (0,0) 到 (i-1,j-1) 的矩形区域和
            self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(m):
                for j in range(n):
                    self.prefix[i + 1][j + 1] = (
                        matrix[i][j] 
                        + self.prefix[i][j + 1] 
                        + self.prefix[i + 1][j] 
                        - self.prefix[i][j]
                    )
        
        def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            """
            计算矩形区域的和
            
            使用容斥原理：
            sum = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
            """
            return (
                self.prefix[row2 + 1][col2 + 1]
                - self.prefix[row1][col2 + 1]
                - self.prefix[row2 + 1][col1]
                + self.prefix[row1][col1]
            )
    
    # 测试用例
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    num_matrix = NumMatrix(matrix)
    
    test_cases = [
        (2, 1, 4, 3, 8),
        (1, 1, 2, 2, 11),
        (1, 2, 2, 4, 12),
    ]
    
    print("\n=== LeetCode 304: 二维区域和检索 ===")
    for i, (row1, col1, row2, col2, expected) in enumerate(test_cases, 1):
        result = num_matrix.sumRegion(row1, col1, row2, col2)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


# ============== 主函数 ==============

if __name__ == "__main__":
    print("前缀和 (Prefix Sum) 算法实现")
    print("=" * 50)
    
    # 运行 LeetCode 题目
    leetcode_303_range_sum_query()
    leetcode_560_subarray_sum_equals_k()
    leetcode_974_subarray_sums_divisible_by_k()
    leetcode_304_range_sum_query_2d()
