# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_record = ('Nate', 'Owens', 19, 'Cyclist', 'Seoul')
people_records.insert(0, my_record)

print("Task 1:\n", people_records)

#Index swapping (Fully custom method using Notes from the lesson)

def index_swapping_method_1():
    print("\n Task 2: ")

    my_list = people_records
    x = my_list[1]
    y = my_list[5]
    my_list.pop(5)
    my_list.pop(1)

    my_list.insert(5, x)
    my_list.insert(1, y)

    print(x, "\n", y, "\n", my_list)


#Shorter way, with Gemini AI (the function index_swapping_method_1 should be commented to get the proper results)
def index_swapping_method_2():
    print("\n Task 2 another method: ")

    list_2 = people_records
    list_2[1], list_2[5] = list_2[5], list_2[1]
    print(f"Element 1: {list_2[1]}, "
          f"\n Element 5: {list_2[5]}, "
          f"\n swapped list: {list_2}")

    return people_records

def task_3():
    print("\n Task 3:")
    print(people_records)


    y = all([people_records[6][2] >= 30,
             people_records[10][2] >= 30,
             people_records[13][2] >= 30 ])
    print(f"The answer is: {y}")

    #SandBox:
    sand_box_method = [x[2]>=30 for x in [people_records[6], people_records[10], people_records[13]]]

    print(sand_box_method)
    print(people_records)

if __name__ == "__main__":
    index_swapping_method_1()
    #index_swapping_method_2()
    task_3()


