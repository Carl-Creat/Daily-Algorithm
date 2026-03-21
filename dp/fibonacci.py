"""
动态规划 - 斐波那契数列
Dynamic Programming - Fibonacci

斐波那契数列: F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

本文件展示从递归到动态规划的优化过程
"""

from typing import List
import functools
import time


# ==================== 方法1: 朴素递归 ====================
def fib_recursive(n: int) -> int:
    """
    朴素递归解法
    
    时间复杂度: O(2^n) - 指数级! 极慢
    空间复杂度: O(n) - 调用栈深度
    
    问题: 存在大量重复计算
    例如 fib(5) = fib(4) + fib(3)
         fib(4) = fib(3) + fib(2)
         fib(3) 被计算了多次
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# ==================== 方法2: 记忆化搜索 (自顶向下) ====================
def fib_memoization(n: int, memo: dict = None) -> int:
    """
    记忆化递归 (Top-Down DP)
    
    时间复杂度: O(n)
    空间复杂度: O(n) - 递归栈 + memo字典
    
    优化: 用空间换时间, 避免重复计算
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]


# ==================== 方法3: 动态规划 (自底向上) ====================
def fib_dp(n: int) -> int:
    """
    动态规划 (Bottom-Up DP)
    
    时间复杂度: O(n)
    空间复杂度: O(n)
    
    思路: 从 base case 向上构建
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


# ==================== 方法4: 空间优化 ====================
def fib_optimized(n: int) -> int:
    """
    空间优化版
    
    时间复杂度: O(n)
    空间复杂度: O(1)
    
    观察: 只关心前两个数, 不需要整个数组
    """
    if n <= 1:
        return n
    
    prev, curr = 0, 1
    
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return curr


# ==================== 方法5: 矩阵快速幂 ====================
def fib_matrix(n: int) -> int:
    """
    矩阵快速幂
    
    时间复杂度: O(log n)
    空间复杂度: O(log n) - 递归栈
    
    原理:
    | F(n+1) F(n)   |   | 1 1 |^n
    | F(n)   F(n-1) | = | 1 0 |
    """
    if n <= 1:
        return n
    
    def matrix_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        return [
            [A[0][0]*B[0][0] + A[0][1]*B[1][0], A[0][0]*B[0][1] + A[0][1]*B[1][1]],
            [A[1][0]*B[0][0] + A[1][1]*B[1][0], A[1][0]*B[0][1] + A[1][1]*B[1][1]]
        ]
    
    def matrix_power(M: List[List[int]], p: int) -> List[List[int]]:
        if p == 1:
            return M
        if p % 2 == 0:
            half = matrix_power(M, p // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(M, matrix_power(M, p - 1))
    
    result_matrix = matrix_power([[1, 1], [1, 0]], n)
    return result_matrix[0][1]


# ==================== 方法6: 闭包公式 (Binet's Formula) ====================
def fib_binet(n: int) -> int:
    """
    贝叶斯公式
    
    时间复杂度: O(1) - 常数时间!
    空间复杂度: O(1)
    
    公式: F(n) = (φ^n - ψ^n) / √5
    其中 φ = (1 + √5) / 2 ≈ 1.618 (黄金分割)
          ψ = (1 - √5) / 2 ≈ -0.618
    
    注意: 由于浮点数精度问题, 大 n 时会有误差
    """
    import math
    
    phi = (1 + math.sqrt(5)) / 2  # 黄金分割
    psi = (1 - math.sqrt(5)) / 2
    
    return int(round((phi**n - psi**n) / math.sqrt(5)))


# ==================== 测试 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("斐波那契数列 - 多种解法对比")
    print("=" * 60)
    
    # 正确性测试
    test_n = 20
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    
    methods = [
        ("递归 (memo)", fib_memoization),
        ("动态规划", fib_dp),
        ("空间优化", fib_optimized),
        ("矩阵快速幂", fib_matrix),
        ("贝叶斯公式", fib_binet),
    ]
    
    print(f"\n计算 F({test_n}):")
    print("-" * 40)
    
    for name, func in methods:
        result = func(test_n)
        status = "✅" if result == expected[test_n] else "❌"
        print(f"  {name:15s}: {result:6d} {status}")
    
    # 性能测试
    print("\n" + "-" * 40)
    print("性能测试 (n=30):")
    print("-" * 40)
    
    n = 30
    
    # 递归太慢, 跳过
    # start = time.time()
    # fib_recursive(30)
    # print(f"  朴素递归: {time.time() - start:.4f}s (太慢!)")
    
    for name, func in methods:
        start = time.time()
        result = func(n)
        elapsed = time.time() - start
        print(f"  {name:15s}: {elapsed:.6f}s -> F({n})={result}")
    
    # 大数测试
    print("\n" + "-" * 40)
    print("大数测试 (n=1000):")
    print("-" * 40)
    
    n = 1000
    start = time.time()
    result = fib_optimized(n)
    elapsed = time.time() - start
    print(f"  空间优化算法: {elapsed:.6f}s -> F({n}) 有 {len(str(result))} 位数字")
    
    print("\n" + "=" * 60)
    print("✅ 测试完成!")
    print("=" * 60)
