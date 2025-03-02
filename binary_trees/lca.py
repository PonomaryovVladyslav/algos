class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root  # Если `p` и `q` в разных поддеревьях, `root` — LCA

    return left if left else right  # LCA в одном из поддеревьев

tree = TreeNode(3,
    TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
    TreeNode(1, TreeNode(0), TreeNode(8))
)

p = tree.left  # 5
q = tree.right  # 1
print(lowest_common_ancestor(tree, p, q).val)  # 3

p = tree.left  # 5
q = tree.left.right.right  # 4
print(lowest_common_ancestor(tree, p, q).val)  # 5
