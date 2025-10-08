class Student:

   def __init__(self, name, surname, average_score):
        self.name:str = name
        self.surname:str = surname
        self.average_score = average_score


call = Student(name=input("Enter Student`s name:\n"),
               surname=input("Enter Student`s surname:\n"),
               average_score=input("Enter Student`s average score:\n"))

print("-"*200)
print(f"Student name:\n{call.name}, Student surname:\n{call.surname},"
      f"Average score is:\n{call.average_score}")

choice = input("-"*200 + "\nPress 'a' to change the average score, press 'b' to display Student info:\n")

if choice == "a":
    x = input("Enter new average score:")
    call.average_score = x
elif choice == "b":
    print("-"*200, f"\n Student info: \n{call.name}, \n{call.surname},"
                   f"\n{call.average_score}")
else:
    print("You have chosen the wrong button, try reload the program and start again")

print("-"*200,
      f"\nStudent name: -> {call.name};"
      f"\nStudent surname: -> {call.surname};"
      f"\nAverage score is: -> {call.average_score}")

print("-"*200)
