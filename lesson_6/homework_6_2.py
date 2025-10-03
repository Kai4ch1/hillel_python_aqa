def task_6_2():
    while True:
        user_input = input("Enter the word which contains 'h' Or 'H:\n")
        print(user_input)

        if "h" in user_input.lower():
            print("Congrats your Input contains 'ashes' hu-hu, Just kidding H-s fine :)")
            break
        else:
            print("Your input does not contains 'H' or 'h' try again")

if __name__ == "__main__":
    task_6_2()