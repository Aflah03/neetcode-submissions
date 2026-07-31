class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []


    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            currMin = self.minst[-1]
            self.minst.append(min(currMin, val))
    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
