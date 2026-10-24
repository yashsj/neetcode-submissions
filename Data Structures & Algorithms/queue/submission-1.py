class Deque:
    
    def __init__(self):
        self.queue=[]


    def isEmpty(self) -> bool:
        if not self.queue:
            return True
        return False
        
    def append(self, value: int) -> None:
        self.queue.append(value)

    def appendleft(self, value: int) -> None:
        self.queue.insert(0,value)

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()
        return -1
        

    def popleft(self) -> int:
        num=-1
        if self.queue:
            num=self.queue[0]
            self.queue.remove(num)
        return num
