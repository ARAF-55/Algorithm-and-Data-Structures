from collections import deque


customQueue = deque(maxlen=3)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)

customQueue.popleft()

print(customQueue)
