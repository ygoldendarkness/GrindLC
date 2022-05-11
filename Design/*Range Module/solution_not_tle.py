class SegmentTree:
    def __init__(self, start, end, value = False):
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None
    
    def query(self, start, end):
        if end < self.start or start > self.end:
            return True
        
        if (start <= self.start and end >= self.end) or not self.left:
            return self.value
        
        return self.left.query(start, end) and self.right.query(start, end)
    
    def update(self, start, end, value):
        if end < self.start or start > self.end:
            return
        
        if start <= self.start and end >= self.end:
            self.value = value
            self.left, self.right = None, None
            return

        if not self.left:
            mid = self.start + (self.end - self.start) // 2
            self.left = SegmentTree(self.start, mid, self.value)
            self.right = SegmentTree(mid + 1, self.end, self.value)
        self.left.update(start, end, value)
        self.right.update(start, end, value)
        self.value = self.left.value and self.right.value
            
        
        
class RangeModule:
    def __init__(self):
        self.st = SegmentTree(1, 10**9-1)

    def addRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.st.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.st.update(left, right - 1, False)
        



# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)