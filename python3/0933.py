class RecentCounter:

    def __init__(self):
        self.record = []
        self.left = 0
        self.right = 0

    def ping(self, t: int) -> int:
        self.record.append(t)
        self.right += 1
        t -= 3000

        while self.record[self.left] < t:
            self.left += 1

        return self.right-self.left


if __name__ == "__main__":
    # Your RecentCounter object will be instantiated and called as such:
    # obj = RecentCounter()
    # param_1 = obj.ping(t)
    inputs = [[1], [100], [3001], [3002]]
    res = ['null']
    obj = RecentCounter()
    for time in inputs:
        res.append(obj.ping(time[0]))

    print(res)
