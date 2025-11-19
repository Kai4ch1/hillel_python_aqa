class ReturningNoOddNums:

    def __init__(self, num: int):
        self.num : int = num

    def return_not_odd_nums(self):
        var = (x for x in range(0, self.num) if x % 2 ==0)
        return var


if __name__ == "__main__":
    find_num = ReturningNoOddNums(13)
    for number in find_num.return_not_odd_nums():
        print(number)




