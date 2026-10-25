# 📚 排序算法完整学习指南

> 本章对应 LeetCode Hot 100 中所有排序相关题目
> 建议学习时长：1周（每天2小时）

---

## 目录

1. [排序算法总览](#1-排序算法总览)
2. [冒泡排序](#2-冒泡排序)
3. [选择排序](#3-选择排序)
4. [插入排序](#4-插入排序)
5. [归并排序](#5-归并排序)
6. [快速排序](#6-快速排序)
7. [堆排序](#7-堆排序)
8. [计数排序](#8-计数排序)
9. [LeetCode 练习题](#9-leetcode-练习题)

---

## 1. 排序算法总览

### 常见排序算法分类

```
排序算法
├── 比较类排序（基于元素比较）
│   ├── O(n²) 基础排序
│   │   ├── 冒泡排序      ← 最简单
│   │   ├── 选择排序
│   │   └── 插入排序      ← 有序数组插入排序最快
│   │
│   └── O(n log n) 高效排序
│       ├── 归并排序      ← 稳定，分治思想
│       ├── 快速排序      ← 最常用，原地排序
│       └── 堆排序        ← 利用堆结构
│
└── 非比较类排序（不基于元素比较）
    ├── 计数排序      ← 整数排序，范围有限
    ├── 桶排序
    └── 基数排序
```

### 时间复杂度对比

| 算法 | 平均 | 最好 | 最坏 | 空间 | 稳定性 |
|------|------|------|------|------|------|
| 冒泡排序 | O(n²) | O(n) | O(n²) | O(1) | ✅ 稳定 |
| 选择排序 | O(n²) | O(n²) | O(n²) | O(1) | ❌ 不稳定 |
| 插入排序 | O(n²) | O(n) | O(n²) | O(1) | ✅ 稳定 |
| 归并排序 | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ 稳定 |
| 快速排序 | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ 不稳定 |
| 堆排序 | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ 不稳定 |

> **稳定性**：相等的元素排序后相对位置是否保持不变

---

## 2. 冒泡排序（Bubble Sort）

### 核心思想

相邻元素两两比较，如果顺序错误就交换，像气泡一样逐步浮到顶端。

```
原始数组: [5, 3, 8, 4, 2]

第1轮:
  [5, 3, 8, 4, 2] → 比较(5,3)，交换 → [3, 5, 8, 4, 2]
  [3, 5, 8, 4, 2] → 比较(5,8)，不交换
  [3, 5, 8, 4, 2] → 比较(8,4)，交换 → [3, 5, 4, 8, 2]
  [3, 5, 4, 8, 2] → 比较(8,2)，交换 → [3, 5, 4, 2, 8]
  最大值8已经冒到最右

第2轮: [3, 5, 4, 2, 8]
  → [3, 4, 5, 2, 8] → [3, 4, 2, 5, 8] → [3, 4, 2, 5, 8]
```

### 代码实现

```python
def bubble_sort(arr):
    """
    冒泡排序
    
    时间复杂度: O(n²)
    空间复杂度: O(1)
    稳定性: 稳定
    
    优化版本：提前终止（如果某轮没有交换，说明已经有序）
    """
    n = len(arr)
    for i in range(n):
        swapped = False  # 优化：记录是否有交换
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 如果没有交换，说明已经有序，提前结束
        if not swapped:
            break
    return arr


def bubble_sort_basic(arr):
    """基础版本（无优化）"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### 适用场景

- ✅ 教学演示（最简单）
- ✅ 小规模数据（n < 100）
- ✅ 已经基本有序的数据（最好情况 O(n)）

---

## 3. 选择排序（Selection Sort）

### 核心思想

每一轮从未排序部分选择最小（或最大）的元素，放到已排序部分的末尾。

```
原始数组: [64, 25, 12, 22, 11]

第1轮: 找到最小值11，与第1个位置交换
  [64, 25, 12, 22, 11] → [11, 25, 12, 22, 64]

第2轮: 在[25,12,22,64]中找最小值12，与第2个位置交换
  [11, 25, 12, 22, 64] → [11, 12, 25, 22, 64]

第3轮: 在[25,22,64]中找最小值22，与第3个位置交换
  [11, 12, 25, 22, 64] → [11, 12, 22, 25, 64]
```

### 代码实现

```python
def selection_sort(arr):
    """
    选择排序
    
    时间复杂度: O(n²) — 无论数据如何都要完整比较
    空间复杂度: O(1)
    稳定性: 不稳定（相等元素可能交换位置）
    
    特点：交换次数少，最坏情况只有 O(n) 次交换
    """
    n = len(arr)
    for i in range(n):
        # 找到未排序部分的最小值
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 将最小值放到已排序部分的末尾
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 适用场景

- ✅ 交换成本高的场景（因为交换次数少）
- ❌ 大规模数据（O(n²) 太慢）
- ❌ 需要稳定排序的场景

---

## 4. 插入排序（Insertion Sort）

### 核心思想

把数组分为"已排序"和"未排序"两部分，逐个将未排序的元素插入到已排序部分的正确位置。

```
原始数组: [12, 11, 13, 5, 6]

已排序: [12]        未排序: [11, 13, 5, 6]
插入11: [11, 12]    未排序: [13, 5, 6]
插入13: [11, 12, 13] 未排序: [5, 6]
插入5:  [5, 11, 12, 13] 未排序: [6]
插入6:  [5, 6, 11, 12, 13] ✅ 有序！
```

### 代码实现

```python
def insertion_sort(arr):
    """
    插入排序
    
    时间复杂度:
      - 最好: O(n) — 数组已经有序
      - 平均: O(n²)
      - 最坏: O(n²) — 数组逆序
    空间复杂度: O(1)
    稳定性: 稳定
    
    特点：对于基本有序的数组，效率很高！
    """
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # 待插入的元素
        j = i - 1
        
        # 在已排序部分从后往前找插入位置
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # 元素后移
            j -= 1
        
        arr[j + 1] = key  # 插入元素
    return arr


def insertion_sort_binary(arr):
    """二分查找优化版插入排序"""
    def binary_search(arr, target, left, right):
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i)
        arr[pos:i+1] = [key] + arr[pos:i]
    return arr
```

### 适用场景

- ✅ 小规模数据
- ✅ 基本有序的数据（接近 O(n)）
- ✅ 在线排序（数据不断追加）
- ✅ 链表排序（插入操作 O(1)）

---

## 5. 归并排序（Merge Sort）

### 核心思想

分治策略：将数组分成两半，分别排序后合并。

```
原始数组: [38, 27, 43, 3, 9, 82, 10]

分解:
[38, 27, 43, 3]  [9, 82, 10]
[38, 27]  [43, 3]  [9, 82]  [10]
[38] [27] [43] [3] [9] [82] [10]  ← 单元素

合并（排序）:
[27, 38]  [3, 43]  [9, 82]  [10]
[3, 27, 38, 43]  [9, 10, 82]
[3, 9, 10, 27, 38, 43, 82] ✅ 有序！
```

### 代码实现

```python
def merge_sort(arr):
    """
    归并排序
    
    时间复杂度: O(n log n) — 分解 log n 次，每次合并 O(n)
    空间复杂度: O(n) — 需要额外数组
    稳定性: 稳定
    
    优点：性能稳定，不受数据影响
    缺点：需要额外空间
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """合并两个有序数组"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # 注意：<= 保证稳定性
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # 添加剩余元素
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr):
    """原地归并排序（空间优化版）"""
    def merge_range(arr, left, mid, right):
        """合并两个相邻子数组"""
        left_copy = arr[left:mid + 1]
        right_copy = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_copy) and j < len(right_copy):
            if left_copy[i] <= right_copy[j]:
                arr[k] = left_copy[i]
                i += 1
            else:
                arr[k] = right_copy[j]
                j += 1
            k += 1
        
        while i < len(left_copy):
            arr[k] = left_copy[i]
            i += 1
            k += 1
        
        while j < len(right_copy):
            arr[k] = right_copy[j]
            j += 1
            k += 1
    
    def sort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        sort(arr, left, mid)
        sort(arr, mid + 1, right)
        merge_range(arr, left, mid, right)
    
    sort(arr, 0, len(arr) - 1)
    return arr
```

### 适用场景

- ✅ 需要稳定排序
- ✅ 大规模数据
- ✅ 外部排序（数据太大无法放入内存）

---

## 6. 快速排序（Quick Sort）

### 核心思想

选择一个基准元素（pivot），将数组分为两部分：小于 pivot 和 大于 pivot，然后递归排序。

```
原始数组: [10, 7, 8, 9, 1, 5]
选择基准: pivot = 5

分区过程:
[10, 7, 8, 9, 1, 5]
 小pivot: [1]        大pivot: [10, 7, 8, 9]
加入5: [1, 5]  +  [7, 8, 9]  +  [10]
          ↓
       [1, 5, 7, 8, 9, 10] ✅ 有序！
```

### 代码实现

```python
import random

def quick_sort(arr):
    """
    快速排序
    
    时间复杂度:
      - 平均: O(n log n)
      - 最坏: O(n²) — 基准选择不当（数据基本有序）
    空间复杂度: O(log n) — 递归栈空间
    稳定性: 不稳定
    
    优点：实践中最快，原地排序
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr):
    """原地快速排序（节省空间）"""
    def partition(arr, left, right):
        """
        分区：返回 pivot 最终位置
        """
        # 选择基准（随机化避免最坏情况）
        rand_idx = random.randint(left, right)
        arr[right], arr[rand_idx] = arr[rand_idx], arr[right]
        pivot = arr[right]
        
        i = left - 1  # i 是小于基准区域的最后一个位置
        
        for j in range(left, right):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # 将基准放到正确位置
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1
    
    def sort(arr, left, right):
        if left >= right:
            return
        
        pivot_idx = partition(arr, left, right)
        sort(arr, left, pivot_idx - 1)
        sort(arr, pivot_idx + 1, right)
    
    sort(arr, 0, len(arr) - 1)
    return arr


def quick_sort_three_way(arr):
    """
    三路划分快速排序
    适用于大量重复元素的数组
    """
    def sort(arr, left, right):
        if left >= right:
            return
        
        lt = left      # [left, lt): 小于 pivot
        gt = right     # [gt, right]: 大于 pivot
        i = left       # [lt, i): 等于 pivot
        pivot = arr[left]
        
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1
        
        sort(arr, left, lt - 1)
        sort(arr, gt + 1, right)
    
    sort(arr, 0, len(arr) - 1)
    return arr
```

### 基准选择策略

| 策略 | 说明 | 适用场景 |
|------|------|---------|
| 首元素 | 选第一个 | 简单，但有序数据会退化为 O(n²) |
| 尾元素 | 选最后一个 | 同上 |
| **随机基准** | 随机选一个 | 推荐，避免最坏情况 |
| 三数取中 | 首、中、尾的中位数 | 更稳定 |

---

## 7. 堆排序（Heap Sort）

### 核心思想

利用堆这种数据结构，先建最大堆，然后逐个取出堆顶最大元素。

```
原始数组: [4, 10, 3, 5, 1]

建堆过程（完全二叉树）:
          4
        /   \
       10    3
      /  \
     5    1

调整为最大堆:
          10
        /   \
        5    3
       /  \
      4    1

排序过程:
第1步: 取出10，放到最后 → [1, 5, 3, 4, 10]
第2步: 调整堆 → [5, 4, 3, 1, 10]
... 重复直到完成
```

### 代码实现

```python
def heap_sort(arr):
    """
    堆排序
    
    时间复杂度: O(n log n) — 建堆 O(n) + 排序 O(n log n)
    空间复杂度: O(1) — 原地排序
    稳定性: 不稳定
    
    特点：最坏情况也是 O(n log n)，且是原地排序
    """
    n = len(arr)
    
    def heapify(arr, n, i):
        """将以 i 为根的子树调整为最大堆"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    
    # 1. 建最大堆（从最后一个非叶子节点开始）
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 2. 逐个取出堆顶元素
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # 将最大元素移到末尾
        heapify(arr, i, 0)  # 调整剩余堆
    
    return arr


class MaxHeap:
    """最大堆类（用于理解原理）"""
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)
    
    def extract_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._sift_down(0)
        return max_val
    
    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)
    
    def _sift_down(self, i):
        while self.left(i) < len(self.heap):
            largest = i
            if self.heap[self.left(i)] > self.heap[largest]:
                largest = self.left(i)
            if self.right(i) < len(self.heap) and self.heap[self.right(i)] > self.heap[largest]:
                largest = self.right(i)
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break
```

### 适用场景

- ✅ 需要 O(n log n) 且原地排序
- ✅ 找第 K 大/小元素（部分排序）
- ✅ 优先队列实现

---

## 8. 计数排序（Counting Sort）

### 核心思想

统计每个元素出现的次数，然后按顺序输出。

```
原始数组: [2, 5, 3, 0, 2, 3, 1, 3, 2]

计数数组:
索引:  0  1  2  3  4  5
计数: [1, 1, 3, 3, 0, 1]

前缀和:  [1, 2, 5, 8, 8, 9]

输出（稳定排序）:
[0, 1, 2, 2, 2, 3, 3, 3, 5] ✅ 有序！
```

### 代码实现

```python
def counting_sort(arr):
    """
    计数排序（非比较类排序）
    
    时间复杂度: O(n + k) — k 为元素范围
    空间复杂度: O(k)
    稳定性: 稳定
    
    前提：数据是非负整数，且范围不太大
    """
    if not arr:
        return arr
    
    # 找到范围
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # 计数数组
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    # 前缀和（保证稳定性）
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # 输出数组
    result = [0] * len(arr)
    for num in reversed(arr):
        result[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return result


def counting_sort_for_radix(arr, exp):
    """
    基数排序的辅助函数（按第 exp 位排序）
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # 统计每个数字出现的次数
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
    
    # 前缀和
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # 输出（从后往前保证稳定）
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    return output


def radix_sort(arr):
    """
    基数排序
    
    时间复杂度: O(d * (n + k)) — d 为位数，k 为进制
    空间复杂度: O(n + k)
    稳定性: 稳定
    """
    if not arr:
        return arr
    
    # 找到最大数
    max_val = max(arr)
    
    # 从最低位到最高位进行排序
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr
```

### 适用场景

- ✅ 整数排序，范围较小（如 0-10000）
- ✅ 需要稳定排序
- ✅ 数据量大但范围有限

---

## 9. LeetCode 练习题

### 入门必做题（按难度）

| 题目 | 难度 | 考察点 | 推荐指数 |
|------|------|--------|---------|
| [912. 排序数组](https://leetcode.cn/problems/sort-an-array/) | 🟡 中等 | 所有排序算法 | ⭐⭐⭐⭐⭐ |
| [215. 数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | 🟡 中等 | 快速排序/堆排序 | ⭐⭐⭐⭐⭐ |
| [347. 前K个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) | 🟡 中等 | 堆排序/桶排序 | ⭐⭐⭐⭐ |
| [75. 颜色分类](https://leetcode.cn/problems/sort-colors/) | 🟡 中等 | 三路快排 | ⭐⭐⭐⭐ |
| [88. 合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) | 🟢 简单 | 归并排序思想 | ⭐⭐⭐⭐ |

### 进阶练习题

| 题目 | 难度 | 考察点 |
|------|------|--------|
| [493. 翻转对](https://leetcode.cn/problems/reverse-pairs/) | 🔴 困难 | 归并排序变形 |
| [327. 区间和的个数](https://leetcode.cn/problems/count-of-range-sum/) | 🔴 困难 | 归并排序 + 前缀和 |
| [164. 最大间距](https://leetcode.cn/problems/maximum-gap/) | 🔴 困难 | 桶排序 |
| [220. 存在重复元素 III](https://leetcode.cn/problems/contains-duplicate-iii/) | 🔴 困难 | 桶排序/滑动窗口 |

---

## 📊 算法选择决策树

```
需要排序吗？
    │
    ├── 整数排序 & 范围有限？
    │       └── → 计数排序 / 桶排序
    │
    ├── 数据量大 & 需要稳定排序？
    │       └── → 归并排序
    │
    ├── 数据量大 & 需要原地排序？
    │       └── → 快速排序（随机基准）
    │
    ├── 数据基本有序？
    │       └── → 插入排序
    │
    └── 教学/小规模？
            └── → 冒泡排序 / 选择排序
```

---

## 🎯 本周任务清单

| 任务 | 状态 | 说明 |
|------|------|------|
| 理解 7 种排序算法的核心思想 | ⬜ | 理解「怎么做」 |
| 实现所有排序算法的 Python 代码 | ⬜ | 动手写一遍 |
| 完成 LeetCode 入门必做 5 题 | ⬜ | 检验学习效果 |
| 整理自己的「排序算法模板」 | ⬜ | 面试常用 |

---

## 🔗 相关资源

- **可视化演示**: https://visualgo.net/zh/sorting
- **代码随想录（排序讲解）**: https://programmercarl.com/排序算法总结.html
- **OI Wiki**: https://oi-wiki.org/basic/sort-intro/

---

> 💡 **提示**：不要只看不写！每学一个算法，一定要自己动手实现一遍。
> 建议按顺序学习：冒泡 → 插入 → 选择 → 归并 → 快排 → 堆排
