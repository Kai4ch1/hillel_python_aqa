
def task_6_3():
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    print(f"Here is the raw list:\n{lst1}")
    lst2 = []

    for x in lst1:
        if isinstance(x, str):
            lst2.append(x)

    print(f"Here strings from the list lst1: {lst2}")

if __name__ == "__main__":
    task_6_3()
