"""
拓扑排序 (Topological Sort)

算法原理：
拓扑排序是对有向无环图（DAG）的顶点进行排序的一种算法。
排序后的序列满足：对于图中的每一条有向边 (u, v)，u 在排序后的序列中都出现在 v 之前。

应用场景：
- 任务调度（确定任务执行顺序）
- 课程安排（确定课程先修关系）
- 依赖解析（编译依赖、包管理）
- 死锁检测

实现方法：
1. Kahn 算法（BFS 思想）：基于入度的贪心算法
2. DFS 算法：基于深度优先搜索，利用回溯顺序

时间复杂度：O(V + E)，V 为顶点数，E 为边数
空间复杂度：O(V + E)，存储图的邻接表和入度数组
"""

from typing import List, Dict, Optional
from collections import defaultdict, deque


def topological_sort_kahn(graph: Dict[int, List[int]], n: int) -> Optional[List[int]]:
    """
    Kahn 算法实现拓扑排序（BFS 思想）
    
    算法步骤：
    1. 计算所有顶点的入度
    2. 将入度为 0 的顶点加入队列
    3. 每次从队列取出一个顶点，加入结果序列
    4. 将该顶点的所有邻居入度减 1，若入度变为 0 则加入队列
    5. 重复直到队列为空
    6. 若结果序列长度等于顶点数，则排序成功；否则图中有环
    
    参数:
        graph: 邻接表表示的有向图 {u: [v1, v2, ...]} 表示 u -> v1, u -> v2
        n: 顶点数量（顶点编号为 0 到 n-1）
    
    返回:
        拓扑排序结果，若图中有环则返回 None
    """
    # 计算入度
    in_degree = [0] * n
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # 将入度为 0 的顶点加入队列
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # 遍历所有邻居，入度减 1
        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # 检查是否有环
    if len(result) == n:
        return result
    return None


def topological_sort_dfs(graph: Dict[int, List[int]], n: int) -> Optional[List[int]]:
    """
    DFS 算法实现拓扑排序
    
    算法步骤：
    1. 对每个未访问的顶点执行 DFS
    2. 在 DFS 回溯时，将顶点加入结果序列
    3. 最终将结果序列反转即为拓扑排序
    4. 使用三个状态标记：未访问、访问中、已完成，用于检测环
    
    参数:
        graph: 邻接表表示的有向图
        n: 顶点数量
    
    返回:
        拓扑排序结果，若图中有环则返回 None
    """
    # 状态标记：0=未访问, 1=访问中, 2=已完成
    state = [0] * n
    result = []
    has_cycle = [False]  # 用列表包装以便在嵌套函数中修改
    
    def dfs(u: int) -> None:
        """DFS 遍历"""
        if has_cycle[0]:
            return
        
        state[u] = 1  # 标记为访问中
        
        for v in graph.get(u, []):
            if state[v] == 0:
                dfs(v)
            elif state[v] == 1:
                # 遇到访问中的节点，说明有环
                has_cycle[0] = True
                return
        
        state[u] = 2  # 标记为已完成
        result.append(u)
    
    for i in range(n):
        if state[i] == 0:
            dfs(i)
    
    if has_cycle[0]:
        return None
    
    return result[::-1]  # 反转结果


# ============================================================
# LeetCode 实战题目
# ============================================================

"""
题目1: 课程表 (LeetCode 207)
难度: 中等

题目描述:
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses-1。
在选修某些课程之前需要一些先修课程。给你一个数组 prerequisites，
其中 prerequisites[i] = [ai, bi]，表示如果要学习课程 ai 则必须先学习课程 bi。
请你判断是否可能完成所有课程的学习？

示例:
输入: numCourses = 2, prerequisites = [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。这是可能的。

输入: numCourses = 2, prerequisites = [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0；
      学习课程 0 之前，你还应先完成课程 1。这是不可能的。
"""


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    判断是否能完成所有课程（检测图中是否有环）
    
    时间复杂度: O(V + E)
    空间复杂度: O(V + E)
    """
    # 构建邻接表
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 使用 Kahn 算法
    result = topological_sort_kahn(graph, num_courses)
    return result is not None


"""
题目2: 课程表 II (LeetCode 210)
难度: 中等

题目描述:
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，
你只要返回任意一种就可以了。如果不可能完成所有课程，返回一个空数组。

示例:
输入: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出: [0,2,1,3] 或 [0,1,2,3]
解释: 总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。
      课程 1 和课程 2 都应该排在课程 0 之后。
"""


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    返回课程学习顺序（拓扑排序）
    
    时间复杂度: O(V + E)
    空间复杂度: O(V + E)
    """
    # 构建邻接表
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # 使用 Kahn 算法进行拓扑排序
    result = topological_sort_kahn(graph, num_courses)
    return result if result else []


"""
题目3: 找到最终的安全状态 (LeetCode 802)
难度: 中等

题目描述:
在有向图中，以某个节点为起始节点，从该节点开始每一步沿着有向边走。
如果最终能走到一个终端节点（没有出边的节点），则该节点是安全的。
返回一个由所有安全节点组成的数组（升序排列）。

示例:
输入: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出: [2,4,5,6]
解释: 节点 5、6 是终端节点，节点 2、4 能走到终端节点，所以它们是安全的。
"""


def eventual_safe_nodes(graph: List[List[int]]) -> List[int]:
    """
    找到所有安全节点
    
    思路：安全节点 = 不在环中的节点
    方法：反图 + 拓扑排序
    
    时间复杂度: O(V + E)
    空间复杂度: O(V + E)
    """
    n = len(graph)
    
    # 构建反图
    reverse_graph = defaultdict(list)
    out_degree = [0] * n
    
    for u in range(n):
        out_degree[u] = len(graph[u])
        for v in graph[u]:
            reverse_graph[v].append(u)
    
    # 从出度为 0 的节点开始 BFS
    queue = deque([i for i in range(n) if out_degree[i] == 0])
    safe = []
    
    while queue:
        u = queue.popleft()
        safe.append(u)
        
        for v in reverse_graph[u]:
            out_degree[v] -= 1
            if out_degree[v] == 0:
                queue.append(v)
    
    return sorted(safe)


# ============================================================
# 测试代码
# ============================================================

if __name__ == "__main__":
    # 测试拓扑排序
    print("=" * 50)
    print("拓扑排序测试")
    print("=" * 50)
    
    # 测试用例 1: 无环图
    graph1 = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    n1 = 4
    
    result_kahn = topological_sort_kahn(graph1, n1)
    result_dfs = topological_sort_dfs(graph1, n1)
    print(f"图1 (无环):")
    print(f"Kahn 算法结果: {result_kahn}")
    print(f"DFS 算法结果: {result_dfs}")
    
    # 测试用例 2: 有环图
    graph2 = {
        0: [1],
        1: [2],
        2: [0]
    }
    n2 = 3
    
    result_kahn2 = topological_sort_kahn(graph2, n2)
    result_dfs2 = topological_sort_dfs(graph2, n2)
    print(f"\n图2 (有环):")
    print(f"Kahn 算法结果: {result_kahn2}")
    print(f"DFS 算法结果: {result_dfs2}")
    
    # 测试 LeetCode 207
    print("\n" + "=" * 50)
    print("LeetCode 207: 课程表测试")
    print("=" * 50)
    
    print(f"can_finish(2, [[1,0]]): {can_finish(2, [[1,0]])}")
    print(f"can_finish(2, [[1,0],[0,1]]): {can_finish(2, [[1,0],[0,1]])}")
    
    # 测试 LeetCode 210
    print("\n" + "=" * 50)
    print("LeetCode 210: 课程表 II 测试")
    print("=" * 50)
    
    print(f"find_order(4, [[1,0],[2,0],[3,1],[3,2]]): {find_order(4, [[1,0],[2,0],[3,1],[3,2]])}")
    print(f"find_order(2, [[1,0],[0,1]]): {find_order(2, [[1,0],[0,1]])}")
    
    # 测试 LeetCode 802
    print("\n" + "=" * 50)
    print("LeetCode 802: 安全节点测试")
    print("=" * 50)
    
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    print(f"eventual_safe_nodes({graph}): {eventual_safe_nodes(graph)}")
