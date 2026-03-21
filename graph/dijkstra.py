"""
Dijkstra 最短路径算法

算法原理：
Dijkstra 算法是一种贪心算法，用于求解带权有向图中单源最短路径问题。
该算法适用于所有边权非负的图。

核心思想：
1. 维护一个距离数组 dist，dist[i] 表示从起点到顶点 i 的最短距离
2. 每次选择距离最小的未访问顶点，更新其邻居的距离
3. 使用优先队列（最小堆）优化选择过程

算法步骤：
1. 初始化：起点距离设为 0，其他顶点距离设为无穷大
2. 将起点加入优先队列
3. 循环：从队列取出距离最小的顶点 u
   - 如果 u 已访问，跳过
   - 标记 u 为已访问
   - 对于 u 的每个邻居 v：如果 dist[u] + weight(u,v) < dist[v]，更新 dist[v]
4. 重复直到队列为空

时间复杂度：O((V + E) log V)，使用优先队列实现
空间复杂度：O(V + E)，存储图和距离数组

局限性：
- 不能处理负权边（负权边应使用 Bellman-Ford 算法）
"""

from typing import List, Dict, Tuple
from collections import defaultdict
import heapq


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int, n: int) -> List[int]:
    """
    Dijkstra 算法求单源最短路径
    
    参数:
        graph: 邻接表表示的带权有向图
               {u: [(v1, w1), (v2, w2), ...]} 表示 u->v1 权重 w1, u->v2 权重 w2
        start: 起点顶点编号
        n: 顶点总数
    
    返回:
        dist: dist[i] 表示从起点到顶点 i 的最短距离，若不可达则为 -1
    """
    # 初始化距离数组
    dist = [float('inf')] * n
    dist[start] = 0
    
    # 优先队列：(距离, 顶点)
    pq = [(0, start)]
    
    # 已访问标记
    visited = [False] * n
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # 如果已访问，跳过
        if visited[u]:
            continue
        
        visited[u] = True
        
        # 更新邻居的距离
        for v, w in graph.get(u, []):
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    # 将不可达的距离设为 -1
    return [d if d != float('inf') else -1 for d in dist]


def dijkstra_with_path(graph: Dict[int, List[Tuple[int, int]]], start: int, end: int, n: int) -> Tuple[int, List[int]]:
    """
    Dijkstra 算法求最短路径及路径本身
    
    参数:
        graph: 邻接表表示的带权有向图
        start: 起点顶点编号
        end: 终点顶点编号
        n: 顶点总数
    
    返回:
        (最短距离, 路径列表)
        若不可达，返回 (-1, [])
    """
    # 初始化
    dist = [float('inf')] * n
    dist[start] = 0
    prev = [-1] * n  # 记录前驱节点
    
    pq = [(0, start)]
    visited = [False] * n
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if visited[u]:
            continue
        
        visited[u] = True
        
        # 提前终止：已找到到终点的最短路径
        if u == end:
            break
        
        for v, w in graph.get(u, []):
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    
    # 无法到达终点
    if dist[end] == float('inf'):
        return -1, []
    
    # 重建路径
    path = []
    curr = end
    while curr != -1:
        path.append(curr)
        curr = prev[curr]
    
    return dist[end], path[::-1]


# ============================================================
# LeetCode 实战题目
# ============================================================

"""
题目1: 网络延迟时间 (LeetCode 743)
难度: 中等

题目描述:
有 n 个网络节点，标记为 1 到 n。给定列表 times，表示信号经过有向边的传递时间。
times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点，wi 是传递时间。
我们从某个节点 K 发出一个信号，需要多久才能使所有节点都收到信号？
如果不能使所有节点收到信号，返回 -1。

示例:
输入: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出: 2
解释: 节点 2 发出信号，到达节点 1 需要 1 时间，到达节点 4 需要 2 时间。
"""


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """
    Dijkstra 求网络延迟时间
    
    时间复杂度: O((V + E) log V)
    空间复杂度: O(V + E)
    """
    # 构建邻接表（节点编号从 1 开始，转换为从 0 开始）
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u - 1].append((v - 1, w))
    
    # Dijkstra 求最短距离
    dist = dijkstra(graph, k - 1, n)
    
    # 最大距离即为所有节点收到信号的时间
    max_dist = max(dist)
    return max_dist if max_dist != -1 else -1


"""
题目2: 从第一个节点出发到最后一个节点的受限路径数 (LeetCode 1786)
难度: 中等

题目描述:
给定一个带权无向图，有 n 个节点，节点编号从 1 到 n。
受限路径：路径上每个节点的最短距离严格小于前一个节点的最短距离。
求从节点 1 到节点 n 的受限路径数量。

示例:
输入: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
输出: 3
"""


def count_restricted_paths(n: int, edges: List[List[int]]) -> int:
    """
    先用 Dijkstra 求各点到终点的最短距离，再用动态规划求受限路径数
    
    时间复杂度: O((V + E) log V + E)
    空间复杂度: O(V + E)
    """
    MOD = 10**9 + 7
    
    # 构建无向图邻接表
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    
    # Dijkstra 求各点到节点 n-1 的最短距离
    dist = [float('inf')] * n
    dist[n - 1] = 0
    pq = [(0, n - 1)]
    visited = [False] * n
    
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    
    # 按距离从小到大排序节点
    nodes = sorted(range(n), key=lambda x: dist[x])
    
    # 动态规划求受限路径数
    dp = [0] * n
    dp[n - 1] = 1  # 终点只有一种路径
    
    for u in nodes:
        if u == n - 1:
            continue
        for v, _ in graph[u]:
            # 如果 v 的距离小于 u 的距离，v 可以到达 u
            if dist[v] < dist[u]:
                dp[u] = (dp[u] + dp[v]) % MOD
    
    return dp[0]


"""
题目3: 到达目的地的方案数 (LeetCode 1976)
难度: 中等

题目描述:
在一个无向图中，节点编号从 0 到 n-1，求从节点 0 到节点 n-1 的最短路径的方案数。
由于答案可能很大，返回对 10^9 + 7 取余的结果。

示例:
输入: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
输出: 4
解释: 从 0 到 6 的最短路径长度为 7，共有 4 种方案。
"""


def count_paths(n: int, roads: List[List[int]]) -> int:
    """
    Dijkstra + 动态规划求最短路径方案数
    
    时间复杂度: O((V + E) log V)
    空间复杂度: O(V + E)
    """
    MOD = 10**9 + 7
    
    # 构建邻接表
    graph = defaultdict(list)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Dijkstra
    dist = [float('inf')] * n
    dist[0] = 0
    ways = [0] * n  # ways[i] 表示从 0 到 i 的最短路径方案数
    ways[0] = 1
    
    pq = [(0, 0)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # 如果当前距离大于已记录的最短距离，跳过
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            new_dist = dist[u] + w
            
            if new_dist < dist[v]:
                # 找到更短路径
                dist[v] = new_dist
                ways[v] = ways[u]
                heapq.heappush(pq, (new_dist, v))
            elif new_dist == dist[v]:
                # 相同长度路径
                ways[v] = (ways[v] + ways[u]) % MOD
    
    return ways[n - 1]


# ============================================================
# 测试代码
# ============================================================

if __name__ == "__main__":
    # 测试 Dijkstra 算法
    print("=" * 50)
    print("Dijkstra 最短路径测试")
    print("=" * 50)
    
    # 构建测试图
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }
    
    dist = dijkstra(graph, 0, 4)
    print(f"从节点 0 到各节点的最短距离: {dist}")
    
    # 测试带路径的版本
    distance, path = dijkstra_with_path(graph, 0, 3, 4)
    print(f"从节点 0 到节点 3 的最短路径: 距离={distance}, 路径={path}")
    
    # 测试 LeetCode 743
    print("\n" + "=" * 50)
    print("LeetCode 743: 网络延迟时间测试")
    print("=" * 50)
    
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n, k = 4, 2
    print(f"times={times}, n={n}, k={k}")
    print(f"网络延迟时间: {network_delay_time(times, n, k)}")
    
    # 测试 LeetCode 1976
    print("\n" + "=" * 50)
    print("LeetCode 1976: 最短路径方案数测试")
    print("=" * 50)
    
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], 
             [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]
    n = 7
    print(f"n={n}, roads={roads}")
    print(f"最短路径方案数: {count_paths(n, roads)}")
