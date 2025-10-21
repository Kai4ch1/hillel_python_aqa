class Logic:
    @staticmethod
    def sym_number_in_str(str_of_num: str):
        try:
            numbers = str_of_num.split(",")
            result = sum([int(num.strip()) for num in numbers])
            print(result)
            return result
        except ValueError:
            print("I can`t do it")

if __name__ == "__main__":
    list_1 = (["1,2,3,4",
                    "1,2,3,4,50",
                    "qwerty1,2,3",
                    "5,5,5,5",
                    "7,7,7,,,7,",
                    "32, 32, 32"])
    for _str in list_1:
        Logic.sym_number_in_str(_str)