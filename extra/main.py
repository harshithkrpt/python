from heapq import heappop, heappush, heapify


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)/2

    def insertKey(k):
        heappush(self.heap, k)
