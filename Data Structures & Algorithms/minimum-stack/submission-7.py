class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimumstack=[]

# [5,4,3,2] min=3

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimumstack:
            self.minimumstack.append(val)

        else:
            if self.minimumstack[-1]>val:
                self.minimumstack.append(val)
            else:
                self.minimumstack.append(self.minimumstack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minimumstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumstack[-1]

        
