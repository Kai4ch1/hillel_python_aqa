def task_6_4():
    lst = [2, 1, -9, 17, 20, 22, 50, 99, -1]
    lst_2 = 0

    for x in lst:
        if x%2 == 0:
            lst_2 += x
    print(lst_2)
    return lst_2

if __name__ == "__main__":
    task_6_4()
