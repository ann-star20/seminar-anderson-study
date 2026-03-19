# from collections import deque
#
# stack = deque()
# stack.append(1) # push
# stack.append(2)
# stack.append(3)
# stack.pop() # 반환 ( O(1))
# print(stack) # deque([1,2])

from collections import deque
import heapq

# 우선순위 큐(heapq사용)
pq = []
heapq.heappush(pq,3)
heapq.heappush(pq,4)
heapq.heappush(pq,5)
heapq.heappop(pq) # 반환(최소값)