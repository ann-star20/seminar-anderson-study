import time
import collections

class SimpleHashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value): # Insertion: O(1)
        idx = self._hash(key)
        self.table[idx] = value

    def get(self, key): # Search: O(1)
        idx = self._hash(key)
        return self.table[idx]

# Python dict는 고도로 최적화된 Hash Table입니다.
h_table = {}
start = time.time()
h_table["key_999"] = "value" # 삽입
_ = h_table.get("key_999") # 탐색
print(f"Hash Table Search O(1): {time.time() - start:.8f}s")