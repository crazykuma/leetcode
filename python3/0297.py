# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # BFS
        if not root:
            return None
        res = []
        queue = [root]
        # FIFO 运用队列的思想进行层次遍历
        # 首先遍历父节点，得到父节点的序列化结果res和子节点的队列结果
        # 再将子节点作为父节点判断是否存在，如果存在，将其子节点加入队列，并将父节点的值加入序列化；
        # 如果不存在，该节点的序列化结果为None，起到占位符作用
        while queue:
            node = queue.pop(0)
            if node is None:
                res.append(None)
            else:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        res = ','.join(str(i) for i in res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        queue = [root]
        idx = 1
        # 同样使用队列来进行层次遍历
        # 首先取出序列化结果首位作为初始根节点
        # 按顺序遍历序列化结果，每两个数据一组对应节点的左右子节点
        # 如果左右子节点为None值，则不将子节点加入队列，且指定左右子节点为None
        # 如果左右子节点的值不为None，则根据左右子节点的值新建节点，并将左右节点指向新建的节点，然后将该子节点加入队列
        while queue:
            node = queue.pop(0)
            if data[idx] != 'None':
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            else:
                node.left = None
            idx += 1
            if data[idx] != 'None':
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            else:
                node.right = None
            idx += 1

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
