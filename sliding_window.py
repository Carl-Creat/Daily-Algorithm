"""
滑动窗口 (Sliding Window)

滑动窗口是一种数组/字符串问题的优化技巧，用于解决子数组/子串问题。
核心思想：维护一个窗口，通过移动左右边界来寻找满足条件的子数组。

适用场景：
- 寻找满足特定条件的连续子数组
- 子数组求和/求最大最小值
- 字符串匹配问题

时间复杂度：O(n) - 每个元素最多被访问两次
空间复杂度：O(1) 或 O(k)，取决于问题
"""

from typing import List, Dict, Optional
from collections import defaultdict


# ============== 基础模板 ==============

def sliding_window_template(nums: List[int], target: int) -> int:
    """
    滑动窗口基础模板
    
    思路：
    1. 初始化左右指针 left = right = 0
    2. 扩展右边界，直到窗口满足条件
    3. 收缩左边界，寻找最优解
    4. 重复步骤 2-3
    """
    left = 0
    result = 0
    window_sum = 0
    
    for right in range(len(nums)):
        # 扩展右边界
        window_sum += nums[right]
        
        # 收缩左边界（当不满足条件时）
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        
        # 更新结果
        result = max(result, right - left + 1)
    
    return result


# ============== LeetCode 实战 ==============

def leetcode_209_minimum_size_subarray_sum():
    """
    LeetCode 209. 长度最小的子数组
    https://leetcode.com/problems/minimum-size-subarray-sum/
    
    给定一个含有 n 个正整数的数组和一个正整数 target，
    找出该数组中满足其和 ≥ target 的长度最小的连续子数组。
    
    示例：
        target = 7, nums = [2,3,1,2,4,3]
        输出：2
        解释：子数组 [4,3] 是该条件下的最小子数组
    """
    def min_subarray_len(target: int, nums: List[int]) -> int:
        """
        使用滑动窗口找到最小长度子数组
        """
        left = 0
        window_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # 收缩窗口，寻找最小长度
            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0
    
    # 测试用例
    test_cases = [
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
    ]
    
    print("=== LeetCode 209: 长度最小的子数组 ===")
    for i, (target, nums, expected) in enumerate(test_cases, 1):
        result = min_subarray_len(target, nums)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_3_longest_substring_without_repeating():
    """
    LeetCode 3. 无重复字符的最长子串
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    
    给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。
    
    示例：
        输入: s = "abcabcbb"
        输出: 3
        解释: 答案是 "abc"，长度为 3
    """
    def length_of_longest_substring(s: str) -> int:
        """
        使用滑动窗口 + 哈希表记录字符位置
        """
        char_index = {}  # 记录字符最后出现的位置
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            # 如果字符已存在且在窗口内，收缩左边界
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            
            char_index[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
    
    # 测试用例
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]
    
    print("\n=== LeetCode 3: 无重复字符的最长子串 ===")
    for i, (s, expected) in enumerate(test_cases, 1):
        result = length_of_longest_substring(s)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_76_minimum_window_substring():
    """
    LeetCode 76. 最小覆盖子串
    https://leetcode.com/problems/minimum-window-substring/
    
    给你一个字符串 s、一个字符串 t。返回 s 中涵盖 t 所有字符的最小子串。
    如果不存在符合条件的子串，则返回空字符串 ""。
    
    示例：
        输入: s = "ADOBECODEBANC", t = "ABC"
        输出: "BANC"
        解释: 最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'
    """
    def min_window(s: str, t: str) -> str:
        """
        使用滑动窗口 + 字符计数
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # 统计 t 中需要的字符
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        
        required = len(need)  # 需要满足的不同字符数
        formed = 0  # 当前已满足的字符数
        
        window_counts = defaultdict(int)
        left = 0
        min_len = float('inf')
        min_window_start = 0
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1
            
            # 检查是否满足某个字符的要求
            if char in need and window_counts[char] == need[char]:
                formed += 1
            
            # 收缩左边界，寻找最小窗口
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_start = left
                
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in need and window_counts[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        
        return s[min_window_start:min_window_start + min_len] if min_len != float('inf') else ""
    
    # 测试用例
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]
    
    print("\n=== LeetCode 76: 最小覆盖子串 ===")
    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = min_window(s, t)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: '{expected}', 实际: '{result}')")


def leetcode_438_find_all_anagrams():
    """
    LeetCode 438. 找到字符串中所有字母异位词
    https://leetcode.com/problems/find-all-anagrams-in-a-string/
    
    给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，返回这些子串的起始索引。
    异位词是指由相同字母重排列形成的字符串（包括相同的字符串）。
    
    示例：
        输入: s = "cbaebabacd", p = "abc"
        输出: [0, 6]
        解释: 起始索引等于 0 的子串是 "cba"，它是 "abc" 的异位词。
              起始索引等于 6 的子串是 "bac"，它是 "abc" 的异位词。
    """
    def find_anagrams(s: str, p: str) -> List[int]:
        """
        使用固定大小的滑动窗口 + 字符计数
        """
        if len(p) > len(s):
            return []
        
        p_count = [0] * 26
        window_count = [0] * 26
        
        # 初始化 p 的字符计数和窗口的初始状态
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window_count[ord(s[i]) - ord('a')] += 1
        
        result = []
        if window_count == p_count:
            result.append(0)
        
        # 滑动窗口
        for i in range(len(p), len(s)):
            # 移出左边的字符
            window_count[ord(s[i - len(p)]) - ord('a')] -= 1
            # 加入右边的字符
            window_count[ord(s[i]) - ord('a')] += 1
            
            if window_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
    
    # 测试用例
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
    ]
    
    print("\n=== LeetCode 438: 找到字符串中所有字母异位词 ===")
    for i, (s, p, expected) in enumerate(test_cases, 1):
        result = find_anagrams(s, p)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


# ============== 主函数 ==============

if __name__ == "__main__":
    print("滑动窗口 (Sliding Window) 算法实现")
    print("=" * 50)
    
    # 运行 LeetCode 题目
    leetcode_209_minimum_size_subarray_sum()
    leetcode_3_longest_substring_without_repeating()
    leetcode_76_minimum_window_substring()
    leetcode_438_find_all_anagrams()
