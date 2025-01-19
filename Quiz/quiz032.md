# Quiz 032

## Code
```.py
class HumanResources:
    def __init__(self, name:str, occupation: str):
        self.name = name
        self.occupation = occupation
        self.email = None
        self.nationality = None

    def get_email(self):
        if self.email is not None:
            return f"{self.name}'s email is: {self.email}"
        else:
            self.set_email()

    def set_email(self):
        name_parts = self.name.split()
        if len(name_parts) >= 2:
            first_name = name_parts[1]
            last_name = name_parts[0]
            self.email = f"{last_name.lower()}.{first_name.lower()}@gmail.com"
            print(f"Email for {self.name} has been set to: {self.email}")
        else:
            print("Invalid name format. Please ensure the name has both first and last name.")

    def greet(self):
        return f"WELCOME TO THE COMPANY, {self.name.upper()}"

    def set_nationality(self):
        self.nationality = input(f"Please enter {self.name}'s nationality: ")
        print(f"Nationality for {self.name} has been set to: {self.nationality}")
```

test.py
```.py

from quiz.quiz032 import HumanResources

test = HumanResources("Annie Tran", "student ")
print(test.greet())
print(test.get_email())
print(test.set_nationality())

```
## Proof of work
![image](https://github.com/user-attachments/assets/a150c9d4-396d-49c9-93c5-f57a09687b54)

