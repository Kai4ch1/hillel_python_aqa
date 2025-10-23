import re


def task_1(text):
    processed_str = re.findall(r"h", text, re.IGNORECASE)

    return len(processed_str)

def task_2(value):

    lst2 = [x for x in value if isinstance(x, str)]

    return lst2

def task_3(x, y):
    return x / y