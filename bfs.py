"""BFS 广度优先搜索"""
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# 测试
if __name__ == "__main__":
    graph = {
        1: [2, 3], 2: [4, 5], 3: [6, 7],
        4: [8], 5: [8], 6: [8], 7: [8]
    }
    print(bfs(graph, 1))
    # 输出: [1, 2, 3, 4, 5, 6, 7, 8]
