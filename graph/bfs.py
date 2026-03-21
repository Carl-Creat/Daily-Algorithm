"""
图算法 - BFS 广度优先搜索 (Breadth-First Search)
时间复杂度: O(V + E) V=顶点数, E=边数
空间复杂度: O(V)
"""

from typing import List, Dict, Set, Tuple
from collections import deque


class Graph:
    """图的邻接表表示"""
    
    def __init__(self):
        self.adjacency: Dict[int, List[int]] = {}
    
    def add_edge(self, u: int, v: int, directed: bool = False) -> None:
        """添加边"""
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        
        self.adjacency[u].append(v)
        if not directed:
            self.adjacency[v].append(u)
    
    def bfs(self, start: int, target: int = None) -> Tuple[List[int], Dict[int, int]]:
        """
        广度优先搜索
        
        Args:
            start: 起始顶点
            target: 目标顶点 (可选, 用于找最短路径)
        
        Returns:
            (遍历顺序, 每个节点的父节点)
        """
        visited: Set[int] = set()
        parent: Dict[int, int] = {}  # 记录路径
        order: List[int] = []  # 遍历顺序
        queue = deque([start])
        
        visited.add(start)
        parent[start] = -1  # 起点没有父节点
        
        while queue:
            node = queue.popleft()
            order.append(node)
            
            # 找到目标, 可以提前返回
            if target and node == target:
                break
            
            # 遍历所有邻居
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        return order, parent
    
    def bfs_shortest_path(self, start: int, end: int) -> List[int]:
        """
        找最短路径
        
        Returns:
            从 start 到 end 的最短路径
        """
        _, parent = self.bfs(start, end)
        
        if end not in parent:
            return []  # 不可达
        
        # 从终点回溯到起点
        path = []
        current = end
        
        while current != -1:
            path.append(current)
            current = parent[current]
        
        return path[::-1]  # 反转得到从起点到终点的路径
    
    def bfs_levels(self, start: int) -> Dict[int, int]:
        """
        标记每个节点所在的层级
        
        Returns:
            {节点: 层级}
        """
        levels: Dict[int, int] = {start: 0}
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            current_level = levels[node]
            
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in levels:
                    levels[neighbor] = current_level + 1
                    queue.append(neighbor)
        
        return levels


def bfs_matrix(matrix: List[List[int]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    迷宫/网格矩阵中的 BFS
    
    适用于:
    - 迷宫寻路
    - 网格遍历
    - 岛屿数量统计
    
    Args:
        matrix: 0/1 矩阵, 1=可走, 0=障碍
        start: 起始位置 (row, col)
    
    Returns:
        可访问的位置列表
    """
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    # 四个方向: 上, 下, 左, 右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col = queue.popleft()
        result.append((row, col))
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if (0 <= nr < rows and 
                0 <= nc < cols and 
                (nr, nc) not in visited and
                matrix[nr][nc] == 1):
                visited.add((nr, nc))
                queue.append((nr, nc))
    
    return result


def bfs_shortest_path_in_grid(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    """
    网格中的最短路径长度
    
    Returns:
        最短路径步数, 不可达返回 -1
    """
    if not grid or not grid[0]:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    
    if grid[start[0]][start[1]] == 0 or grid[end[0]][end[1]] == 0:
        return -1
    
    visited = set([start])
    queue = deque([(start[0], start[1], 0)])  # row, col, steps
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        row, col, steps = queue.popleft()
        
        if (row, col) == end:
            return steps
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if (0 <= nr < rows and 
                0 <= nc < cols and 
                (nr, nc) not in visited and
                grid[nr][nc] == 1):
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    
    return -1  # 不可达


# ==================== 测试 ====================
if __name__ == "__main__":
    print("=" * 60)
    print("BFS 广度优先搜索 - 测试")
    print("=" * 60)
    
    # 测试1: 基本图遍历
    print("\n【测试1】基本图遍历")
    print("-" * 40)
    
    g = Graph()
    edges = [
        (1, 2), (1, 3), (2, 4), (2, 5), 
        (3, 6), (3, 7), (4, 8), (5, 8)
    ]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print("图结构:")
    for node, neighbors in g.adjacency.items():
        print(f"  {node} -> {neighbors}")
    
    order, parent = g.bfs(1)
    print(f"\n从节点1开始的BFS遍历顺序: {order}")
    print(f"每个节点的父节点: {parent}")
    
    # 测试2: 最短路径
    print("\n【测试2】最短路径")
    print("-" * 40)
    
    path = g.bfs_shortest_path(1, 8)
    print(f"从 1 到 8 的最短路径: {path}")
    
    # 测试3: 层级
    print("\n【测试3】节点层级")
    print("-" * 40)
    
    levels = g.bfs_levels(1)
    print(f"从节点1出发的层级: {levels}")
    
    # 测试4: 网格迷宫
    print("\n【测试4】网格迷宫最短路径")
    print("-" * 40)
    
    maze = [
        [1, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    
    start = (0, 0)
    end = (4, 4)
    
    print(f"迷宫 (1=路, 0=墙):")
    for row in maze:
        print(f"  {row}")
    print(f"\n从 {start} 到 {end} 的最短路径长度: {bfs_shortest_path_in_grid(maze, start, end)}")
    
    print("\n" + "=" * 60)
    print("✅ BFS 测试完成!")
    print("=" * 60)
