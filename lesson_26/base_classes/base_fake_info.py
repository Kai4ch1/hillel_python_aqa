from faker import Faker

class BaseFakeInfo:
    def __init__(self) -> None:
        self.faker = Faker()
        self.firstname = self.faker.first_name()
        self.lastname = self.faker.last_name()
        self.password = self.faker.password()
        self.email = self.faker.email()

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_password(self) -> str:
        return self.password

    def get_email(self) -> str:
        return self.email

    def get_full_info(self) -> dict[str, str]:
        full_fake_user = {
            "Firstname": self.firstname,
            "Lastname": self.lastname,
            "Email": self.email,
            "Password": self.password
        }
        return full_fake_user

    def __repr__(self) -> str:
        return f"{self.firstname}, {self.lastname}, {self.password}, {self.email}"