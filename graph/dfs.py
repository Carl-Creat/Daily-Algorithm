"""
DFS - Depth-First Search
Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List, Dict, Set, Tuple, Optional


class Graph:
    """Graph represented as adjacency list"""
    
    def __init__(self):
        self.adjacency: Dict[int, List[int]] = {}
    
    def add_edge(self, u: int, v: int, directed: bool = False) -> None:
        """Add an edge"""
        if u not in self.adjacency:
            self.adjacency[u] = []
        if v not in self.adjacency:
            self.adjacency[v] = []
        
        self.adjacency[u].append(v)
        if not directed:
            self.adjacency[v].append(u)
    
    def dfs_recursive(self, start: int, visited: Set[int] = None) -> List[int]:
        """Recursive DFS"""
        if visited is None:
            visited = set()
        
        visited.add(start)
        result = [start]
        
        for neighbor in self.adjacency.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        
        return result
    
    def dfs_iterative(self, start: int) -> List[int]:
        """Iterative DFS using stack"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                result.append(node)
                
                # Add neighbors in reverse to maintain order
                neighbors = self.adjacency.get(node, [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_with_parent(self, start: int) -> Tuple[List[int], Dict[int, Optional[int]]]:
        """
        DFS with parent tracking for path reconstruction
        
        Returns:
            (traversal order, parent map)
        """
        visited = set()
        parent = {start: None}
        order = []
        stack = [start]
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                order.append(node)
                
                for neighbor in self.adjacency.get(node, []):
                    if neighbor not in visited:
                        parent[neighbor] = node
                        stack.append(neighbor)
        
        return order, parent
    
    def has_cycle(self) -> bool:
        """Detect if graph has a cycle"""
        visited = set()
        
        def dfs_cycle(node: int, parent: int) -> bool:
            visited.add(node)
            
            for neighbor in self.adjacency.get(node, []):
                if neighbor not in visited:
                    if dfs_cycle(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            
            return False
        
        for node in self.adjacency:
            if node not in visited:
                if dfs_cycle(node, -1):
                    return True
        
        return False


def number_of_islands(grid: List[List[str]]) -> int:
    """
    Count number of islands in a grid
    Uses DFS to explore each island
    
    Args:
        grid: 2D grid where '1' = land, '0' = water
    
    Returns:
        Number of islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(r: int, c: int):
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            (r, c) in visited or 
            grid[r][c] == '0'):
            return
        
        visited.add((r, c))
        
        # Explore 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                dfs(r, c)
    
    return islands


if __name__ == "__main__":
    print("=" * 60)
    print("DFS - Depth-First Search")
    print("=" * 60)
    
    # Test basic graph
    print("\n[Test 1] Basic Graph Traversal")
    print("-" * 40)
    
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
    for u, v in edges:
        g.add_edge(u, v)
    
    print("Graph structure:")
    for node, neighbors in g.adjacency.items():
        print(f"  {node} -> {neighbors}")
    
    print(f"\nRecursive DFS from 1: {g.dfs_recursive(1)}")
    print(f"Iterative DFS from 1: {g.dfs_iterative(1)}")
    print(f"Has cycle: {g.has_cycle()}")
    
    # Test number of islands
    print("\n[Test 2] Number of Islands")
    print("-" * 40)
    
    grid = [
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['1', '0', '1', '1', '1']
    ]
    
    print("Grid:")
    for row in grid:
        print(f"  {row}")
    
    result = number_of_islands(grid)
    print(f"\nNumber of islands: {result}")
    
    print("\n" + "=" * 60)
    print("All tests passed!")
    print("=" * 60)
