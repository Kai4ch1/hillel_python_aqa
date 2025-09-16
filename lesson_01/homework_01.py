def task_1():
    # task 01 == Виправте синтаксичні помилки

    print("Task 1:")

    print("Hello", end = " ")
    print("World! \n")

def task_2():
    # task 02 == Виправте синтаксичні помилки

    print("Task 2:")

    hello = "Hello"
    world = "world"
    if True:
        print(f"{hello} {world}! \n")

def task_3():
    # task 03  == Вcтавте пропущену змінну у ф-цію print

    print("Task 3:")
    for letter in "Hello world!":
        print(f"{letter} \n")

def task_4():
    # task 04 == Зробіть так, щоб кількість бананів була
    # завжди в чотири рази більша, ніж яблук

    print("Task 4:")

    apples = 2
    banana = apples * 4
    print(f"the amount of bananas is: {banana}, and the amount of apples is: {apples} \n")

def tasks_5_and_6():
    # task 05 == виправте назви змінних

    print("Tasks 5 and 6:")

    side_1 = 1
    side_2 = 2
    side_3 = 3
    side_4 = 4

    # task 06 == Порахуйте периметр фігури з task 05
    # та виведіть його для користувача
    perimeter = side_1 + side_2 + side_3 + side_4
    print(f"the perimeter is: {perimeter} \n")

def task_7():
    # task 07
    """
    У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
    Скільки всього дерев посадили в саду?
    """

    print("Task 7:")

    apple_tree = 4
    pear_tree = apple_tree + 5
    plum_tree = apple_tree - 2
    tree_sum = apple_tree + pear_tree + plum_tree
    print(f"We`ve got {apple_tree} apple trees, {pear_tree} pear trees, and {plum_tree} plum trees, hence the total amount of trees is: {tree_sum} \n")

def task_8():
    # task 08
    """
    До обіду температура повітря була на 5 градусів вище нуля.
    Після обіду температура опустилася на 10 градусів.
    Надвечір потепліло на 4 градуси. Яка температура надвечір?
    """
    print("Task 8:")

    before_lunch_temperature = 5
    after_lunch_temperature = before_lunch_temperature - 10
    afternoon_temperature = after_lunch_temperature + 4
    print(f"In the beginning of the day temperature was {before_lunch_temperature} degrees,"
          f" after lunch temperature dropped by 10 degrees, so it was {after_lunch_temperature} degrees"
          f"in the afternoon temperature went up for 4 degrees, so the afternoon temperature was: {afternoon_temperature} \n")

def task_9():
    # task 09
    """
    Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
    1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
    Скількі сьогодні дітей у театральному гуртку?
    """

    print("Task 9:")

    amount_of_boys = 24
    amount_of_girls = amount_of_boys / 2
    today_amount_of_children = (amount_of_boys - 1) + (amount_of_girls -2)
    print(f"The amount of boys is 24 and amount of girls is 2 times lesser, hence amount of girls is: {amount_of_girls} "
          f"And 1 boy got sick, so he`s absent, amount of boys is {amount_of_boys - 1} today"
          f"We have 2 girls are absent today, so amount of girls is {amount_of_girls - 2} today "
          f"so the total amount of kids today, is the sum of boys and girls today: {today_amount_of_children} \n")


def task_10():
    # task 10
    """
    Перша книжка коштує 8 грн, друга - на 2 грн дорожче,
    а третя - як половина вартості першої та другої разом.
    Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
    """
    print("task 10:")

    first_book_cost = 8
    second_book_cost = first_book_cost + 2
    third_book_cost = (first_book_cost + second_book_cost) / 2
    all_books_cost = first_book_cost + second_book_cost + third_book_cost
    print("So first book costs 8 hrn "
          f"second book costs more for 2 hrn, so cost is: {second_book_cost} "
          f"The cost of the third book is division of sum of first and second book, (8 + 10) / 2, so the cost is {third_book_cost}. "
          f"and the total cost of all books is the sum of all books 8 + 10 + 9, so the total cost is: {all_books_cost}")


class Main:
    task_1()
    task_2()
    task_3()
    task_4()
    tasks_5_and_6()
    task_7()
    task_8()
    task_9()
    task_10()