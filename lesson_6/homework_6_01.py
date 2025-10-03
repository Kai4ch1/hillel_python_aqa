
def task_1():
    print("Hello! Enter your text down below:")
    user_input = input()

    altered_user_input = set(user_input)
    print(f"- Amount of unique chars is: {altered_user_input}\n- Amount of the unique symbols is: {len(altered_user_input)}")
    print("-"*201)

    if len(altered_user_input) > 10:
        return True
    else:
        return False

if __name__ == "__main__":
    result = task_1()
    print(f"\n The final Result is: {result}")


