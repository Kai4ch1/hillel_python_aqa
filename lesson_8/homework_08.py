class Student:
    def __init__(self, name, age, surname, average_score):
        self.name: str = name
        self.age: int = age
        self.surname: str = surname
        self.average_score: float = average_score

    def print_the_info(self):
        print("-----STUDENT--INFO--1980--STYLE-----")
        print(f"\n Name: {self.name}")
        print(f"\n Surname: {self.surname}")
        print(f"\n age: {self.age}")
        print(f"\n Average score: {self.average_score}")

    def change_the_score(self):
        while True:
            choice = input("\nPress 'a' to change the Student`s average score, press 'b' to display the current score:")
            if choice == 'a':
                new_average_score = input("Enter the new average score:\n")
                self.average_score = new_average_score
                print("✅ The score has been updated successfully")
            elif choice == "b":
                self.print_the_info()
            else:
                print("-"*200)
                print("\n\nOops... The entered option is an incorrect, restart the program and try again!")
                break


def main():
    student_1 = Student(name=str(input("\nInput Student`s name: ")),
                        age=int(input("\nEnter Student`s age: ")),
                        surname=str(input("\nInsert Student`s surname: ")),
                        average_score=float(input("\nPaste the Student`s average score: "))
                        )
    student_1.print_the_info()
    student_1.change_the_score()

if __name__ == "__main__":
    main()
