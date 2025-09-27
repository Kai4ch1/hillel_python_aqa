def task_6_2():
    user_input = input("Print the word which contains 'h' Or 'H:\n")
    print(user_input)
    char_h = "h" or "H"

    if char_h in user_input:
        print("Congrats your Input contains 'ashes' hu-hu, Just kidding H-s fine :)")
    else:
        print("Your input does not contains 'H' or 'h' try again")

if __name__ == "__main__":
    task_6_2()