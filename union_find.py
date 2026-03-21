"""
并查集 (Union-Find / Disjoint Set Union)

并查集是一种树形数据结构，用于处理不相交集合的合并和查询操作。
常用于解决连通性问题，如网络连接、朋友圈分组等。

时间复杂度：
- 近乎 O(1)，使用路径压缩和按秩合并后接近常数时间

空间复杂度：O(n)
"""

from typing import List, Tuple, Optional


class UnionFind:
    """
    并查集实现
    
    Attributes:
        parent: 父节点数组
        rank: 秩（树的深度）
        count: 连通分量数量
    """
    
    def __init__(self, n: int):
        """初始化并查集"""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n
    
    def find(self, x: int) -> int:
        """
        查找元素所在集合的根节点
        
        使用路径压缩：将路径上的所有节点直接指向根节点
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        """
        合并两个集合
        
        使用按秩合并：让 rank 小的树连接到 rank 大的树上
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        self.count -= 1
    
    def connected(self, x: int, y: int) -> bool:
        """判断两个元素是否在同一集合"""
        return self.find(x) == self.find(y)


# ============== LeetCode 实战 ==============

def leetcode_547_number_of_provinces():
    """
    LeetCode 547. 省份数量
    https://leetcode.com/problems/number-of-provinces/
    
    有 n 个城市，其中一些彼此相连，另一些没有相连。
    如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，
    那么城市 a 与城市 c 间接相连。
    省份是由直接或间接相连的城市组成， 不与其他省份相连的城市组成了省份。
    
    示例：
        isConnected = [[1,1,0],[1,1,0],[0,0,1]]
        输出：2
        解释：0 和 1 在同一个省份，2 是独立的省份
    """
    def find_circle_num(is_connected: List[List[int]]) -> int:
        """
        使用并查集计算省份数量
        """
        n = len(is_connected)
        uf = UnionFind(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if is_connected[i][j] == 1:
                    uf.union(i, j)
        
        return uf.count
    
    # 测试用例
    test_cases = [
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
    ]
    
    print("=== LeetCode 547: 省份数量 ===")
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = find_circle_num(input_data)
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_684_redundant_connection():
    """
    LeetCode 684. 冗余连接
    https://leetcode.com/problems/redundant-connection/
    
    树可以看成是一个连通且无环的无向图。
    给定一个包含 n 个节点的有向图，找出最后一条导致图中出现环的边。
    
    示例：
        输入: edges = [[1,2],[1,3],[2,3]]
        输出: [2,3]
        解释: 边 [2,3] 使得图中出现环
    """
    def find_redundant_connection(edges: List[List[int]]) -> List[int]:
        """
        使用并查集找出冗余的边
        """
        n = len(edges)
        uf = UnionFind(n + 1)
        
        for edge in edges:
            if uf.connected(edge[0], edge[1]):
                return edge
            uf.union(edge[0], edge[1])
        
        return []
    
    # 测试用例
    test_cases = [
        ([[1,2],[1,3],[2,3]], [2,3]),
        ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
    ]
    
    print("\n=== LeetCode 684: 冗余连接 ===")
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = find_redundant_connection([e[:] for e in input_data])
        status = "✓" if result == expected else "✗"
        print(f"测试 {i}: {status} (期望: {expected}, 实际: {result})")


def leetcode_721_accounts_merge():
    """
    LeetCode 721. 账户合并
    https://leetcode.com/problems/accounts-merge/
    
    给定账户列表，每个账户 accounts[i] 是一个字符串列表，其中第一个元素是名称，
    其余元素是账户的邮箱。账户可以有关联。如果一个账户的邮箱与另一个账户的邮箱相同，
    则这些账户属于同一个用户。
    
    返回合并后的账户列表，每个账户的邮箱应该按字典序排列。
    """
    def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
        """
        使用并查集合并账户
        """
        email_to_index = {}
        email_to_name = {}
        
        # 建立邮箱到索引的映射
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_index:
                    email_to_index[email] = len(email_to_index)
                email_to_name[email] = account[0]
        
        uf = UnionFind(len(email_to_index))
        
        # 合并相同用户的邮箱
        for account in accounts:
            first_email = account[1]
            first_index = email_to_index[first_email]
            for email in account[2:]:
                uf.union(first_index, email_to_index[email])
        
        # 按连通分量分组
        index_to_emails = {}
        for email, index in email_to_index.items():
            root = uf.find(index)
            if root not in index_to_emails:
                index_to_emails[root] = []
            index_to_emails[root].append(email)
        
        # 构建结果
        result = []
        for emails in index_to_emails.values():
            emails.sort()
            name = email_to_name[emails[0]]
            result.append([name] + emails)
        
        return result
    
    # 测试用例
    test_cases = [
        ([["John","johnsmith@mail.com","john_new@mail.com"],
          ["John","johnsmith@mail.com","john00@mail.com"],
          ["Mary","mary@mail.com"],
          ["John","johnnybravo@mail.com"]],
         [["John","john00@mail.com","john_new@mail.com","johnsmith@mail.com"],
          ["Mary","mary@mail.com"],
          ["John","johnnybravo@mail.com"]]),
    ]
    
    print("\n=== LeetCode 721: 账户合并 ===")
    for i, (input_data, expected) in enumerate(test_cases, 1):
        result = accounts_merge(input_data)
        result_sorted = [sorted(r) for r in result]
        expected_sorted = [sorted(e) for e in expected]
        status = "✓" if result_sorted == expected_sorted else "✗"
        print(f"测试 {i}: {status}")


# ============== 主函数 ==============

if __name__ == "__main__":
    print("并查集 (Union-Find) 算法实现")
    print("=" * 50)
    
    # 运行 LeetCode 题目
    leetcode_547_number_of_provinces()
    leetcode_684_redundant_connection()
    leetcode_721_accounts_merge()
