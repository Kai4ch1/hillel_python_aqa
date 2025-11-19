class FibonacciRowToEnteredValue:

    def __init__(self, num: int):
        self.num : int = num
        self.a, self.b = 0, 1

    def return_fibonacci_before_entered_num(self):
        while self.a <= self.num:
            yield self.a
            self.a, self.b = self.b, self.a + self.b

if __name__ == "__main__":
    find_num = FibonacciRowToEnteredValue(int(input("Enter your value:\n")))
    for number in find_num.return_fibonacci_before_entered_num():
        print(number)