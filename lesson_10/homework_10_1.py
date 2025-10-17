class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)


class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_lang, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_lang = programming_lang


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_lang, team_size):
        super().__init__(name=name,
                        salary=salary,
                        department=department,
                        programming_lang=programming_lang)
        self.team_size = team_size


    def __mro__(self):
        return self.name, self.salary, self.department, self.programming_lang, self.team_size

    def __str__(self):
        return (f"name={self.name}, "
              f"salary={self.salary}, "
              f"department={self.department}, "
              f"team_size={self.team_size}, "
              f"programming_lang={self.programming_lang}")


def print_n_debug():
    tl = TeamLead("Vitya", 134500, "Delivery", "Python", 32)
    print("\n", "-"*200)
    print(f"\nTeam Lead info:\n{tl}")

    return tl
def main():
    print_n_debug()

if __name__ == "__main__":
    main()