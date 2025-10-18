class Logic:
    @staticmethod
    def parse_the_list(list_1: list[str]):
        for x in list_1:
            try:
                parsed_list = x.split(",")
                num = [int(num.strip()) for num in parsed_list if num.strip()]
                result = sum(num)
                print(result)
            except ValueError:
                print("I can`t do it")


def main():
    list_1 = (["1,2,3,4",
                    "1,2,3,4,50",
                    "qwerty1,2,3",
                    "5,5,5,5",
                    "7,7,7,,,7,",
                    "32, 32, 32"])

    Logic.parse_the_list(list_1)
if __name__ == "__main__":
    main()