# Quiz 046

## Paper Solution

## Flow Chart
![image](https://github.com/user-attachments/assets/798e656e-8726-499b-950d-1ac9286ff9c6)

## Code
```.py
class Citizen:
    def __init__(self, name: str, city: str, status: str):
        self.name = name
        self.city = city
        self.status = status

    def getName(self) -> str:
        return self.name

    def getCity(self) -> str:
        return self.city

    def getStatus(self) -> str:
        return self.status


class Employee(Citizen):
    def __init__(self, name: str, city: str, status: str, annual_salary: int):
        super().__init__(name, city, status)
        self.annual_salary = annual_salary

    def getSalary(self) -> int:
        return self.annual_salary


class PartTimeEmployee(Employee):
    def __init__(self, name: str, city: str, status: str, annual_salary: int, fraction: float, union_member: bool):
        super().__init__(name, city, status, annual_salary)
        self.fraction = fraction
        self.union_member = union_member

    def getFraction(self) -> float:
        return self.fraction

    def isUnionMember(self) -> bool:
        return self.union_member


citizen = Citizen(name="Annie", city="HCMC", status="Resident")
print(f"Citizen Name: {citizen.getName()}")
print(f"Citizen City: {citizen.getCity()}")
print(f"Citizen Status: {citizen.getStatus()}")
part_time_employee = PartTimeEmployee(
        name="Charlie",
        city="Chicago",
        status="Part-Time",
        annual_salary=30000,
        fraction=0.5,
        union_member=True
    )

print(f"Part-Time Employee Name: {part_time_employee.getName()}")
print(f"Part-Time Employee City: {part_time_employee.getCity()}")
print(f"Part-Time Employee Status: {part_time_employee.getStatus()}")
print(f"Part-Time Employee Annual Salary: {part_time_employee.getSalary()}")
print(f"Part-Time Employee Work Fraction: {part_time_employee.getFraction()}")
print(f"Part-Time Employee Union Member: {part_time_employee.isUnionMember()}")
```
## Proof of work
![image](https://github.com/user-attachments/assets/dc1acd34-ae14-4c84-bbee-289b9dca567e)
