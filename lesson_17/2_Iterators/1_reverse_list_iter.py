class IterTheList:

    def __init__(self, list_elements : list):
        self.list_elements = list_elements
        self.index = len(list_elements)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.list_elements[self.index]


if __name__ == "__main__":
    lst_1 = [True, "bruh", "tweaker", 13, -27]
    reverse_iter = IterTheList(lst_1)
    for var in reverse_iter:
        print(var)



