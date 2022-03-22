class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        # popleft : pop(0)과 같지만, O(1)의 시간복잡도를 가짐 // pop(0)은 O(n)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return len(self.q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()