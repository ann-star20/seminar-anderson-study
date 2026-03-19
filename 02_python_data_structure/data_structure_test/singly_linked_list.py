class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # 삽입: O(1) - 끝점을 알 때 기준
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # 마지막 노드까지 탐색 (O(n))
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def search(self, target): # 탐색: O(n)
        curr = self.head
        while curr:
            if curr.data == target: return True
            curr = curr.next
        return False