import pytest

def task_1_is_palindrome(i):
    if i == i[::-1]:
        return True
    else:
        return False


@pytest.mark.parametrize(
    "test_data, result", [
        ("aqa", True),
        ("121", True),
        ("1qwe1", False),
        ("", True)

    ]
)
def test_task_1(test_data, result):
    actual_result = task_1_is_palindrome(test_data)
    expected_result = result
    assert actual_result == expected_result
