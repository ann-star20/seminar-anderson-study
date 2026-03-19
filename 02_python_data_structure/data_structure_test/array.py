import time
import collections

# 1. Array (Python List) & Stack
arr = [i for i in range(1000000)] # 100만 개 데이터

# Access (인덱스 접근): O(1)
start = time.time()
_ = arr[999999]
print(f"Array Access O(1): {time.time() - start:.8f}s")

# Insertion at start: O(n)
start = time.time()
arr.insert(0, -1)
print(f"Array Insert at Start O(n): {time.time() - start:.8f}s")

# 2. Queue (collections.deque 활용)
# 일반 list.pop(0)은 O(n)이지만, deque는 O(1)입니다.
queue = collections.deque(arr)
start = time.time()
queue.popleft()
print(f"Queue PopLeft O(1): {time.time() - start:.8f}s")