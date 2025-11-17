import pytest
# 3)
# Список містить словники - дані співробітників фірми (прізвище, зарплата і стать).
# Скласти функцію, яка повертає тапл: а) прізвище особи, яка має найбільшу зарплату (якщо більше одного - перше по алфавіту);
# б) розмір найменшої зарплати чоловіків,
# в) розмір найвищої зарплати жінок


def process_the_list(test_dict: list[dict]):
    try:
        max_salary = max([x["salary"] for x in test_dict])
        people_with_max_salary = sorted([x["name"] for x in test_dict if x['salary'] == max_salary])
        human_with_max_salary = people_with_max_salary[0]
        min_man_salary = min([x["salary"] for x in test_dict if x["gender"] == "m"])
        max_woman_salary = max([x["salary"] for x in test_dict if x["gender"] == "f"])
        result = (human_with_max_salary, min_man_salary, max_woman_salary)
        return result
    except KeyError:
        f"You`ve passed the wrong key, the valid keys are: name, salary, gender"

@pytest.mark.parametrize(
    "input_data, test_name", [
        [
        {"name": "Azimova", "salary": 20000, "gender": "f"},
        {"name": "Borenko", "salary": 9000, "gender": "m"},
        {"name": "Vasilenko", "salary": 10000, "gender": "m"},
        {"name": "Zabolotna", "salary": 25000, "gender": "f"},
        {"name": "Koval", "salary": 35000, "gender": "f"},
        {"name": "Grach", "salary": 35000, "gender": "m"},
        {"name": "Neferova", "salary": 17000, "gender": "f"},
        {"name": "Smitр", "salary": 35000, "gender": "m"}, "happy_path"
    ],
    [
        {"name": "Borenko", "salary": 9000, "gender": "m"},
        {"name": "Vasilenko", "salary": 10000, "gender": "m"},
        {"name": "Smitр", "salary": 35000, "gender": "m"}, "man_only"
    ],
    [
        {"name": "Zabolotna", "salary": 25000, "gender": "f"},
        {"name": "Koval", "salary": 35000, "gender": "f"},
        {"name": "Neferova", "salary": 17000, "gender": "f"}, "female_only"

    ],
    [
        {"name": "Azimova", "salary": 20000, "gender": "f"},
        {"name": "Borenko", "salary": 9000, "gender": "m"},
        {"name": "Vasilenko", "salary": 35000, "gender": "m"},
        {"name": "Zabolotna", "salary": 25000, "gender": "f"},
        {"name": "Koval", "salary": 35000, "gender": "f"},
        {"name": "Grach", "salary": 35000, "gender": "m"},
        {"name": "Neferova", "salary": 17000, "gender": "f"},
        {"name": "Smitр", "salary": 35000, "gender": "m"}, "male_max_salary=female_max_salary"]
]
)
def test_the_processed_list(input_data, test_name):
    actual_result = process_the_list(input_data)
    expected_result = ('Grach', 9000, 35000)
    assert actual_result == expected_result, f"Caught mismatch of results, actual result={actual_result}, expected={expected_result}"