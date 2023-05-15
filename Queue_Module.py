import queue


customQueue = queue.Queue(maxsize=3)
print(customQueue.qsize())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())
print(customQueue)
print(customQueue.empty())
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
print(customQueue)


