# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

if __name__ == "__main__":
    # 构造示例二叉树: [1, null, 2, 3]
    #    1
    #     \
    #      2
    #     /
    #    3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solu = Solution()
    result = solu.inorderTraversal(root)
    print(f"中序遍历结果：{result}")
    # 预期输出[1, 3, 2]