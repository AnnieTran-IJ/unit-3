# Quiz 035

## Code
```.py
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Student(Person):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade
    def get_grade(self):
        return self.grade
```
## Proof of work
![image](https://github.com/user-attachments/assets/be3f6058-eca8-4ee2-9aa2-2dabb31a627d)

