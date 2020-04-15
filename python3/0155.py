class MinStack:
    """最小栈
    思路：辅助栈，同步操作，
    1. push，栈顶推入数据，同时辅助栈推入当前最小值
    2. pop，两栈同步推出栈顶
    3. top，返回普通栈顶的值
    4. getmin，返回辅助栈顶的值    
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minstack) == 0 or x < self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
