class ReturnEven:

    def __init__(self, num : int):
        self.num = num
        self.temp = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.temp < self.num:
            self.temp += 1
            if self.temp % 2 == 0:
                return self.temp
        raise StopIteration




if __name__ == "__main__":
    parse_the_num = ReturnEven(10)
    for i in parse_the_num:
        print(i)