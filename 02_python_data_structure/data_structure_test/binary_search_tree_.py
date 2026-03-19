class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def insert(self, root, key): # 삽입: O(log n)
        if root is None: return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key): # 탐색: O(log n)
        if root is None or root.key == key: return root
        if key < root.key: return self.search(root.left, key)
        return self.search(root.right, key)

# 데이터가 100만 개일 때, log2(1,000,000)은 약 20번의 비교만 필요합니다.