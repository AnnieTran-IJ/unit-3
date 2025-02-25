# Quiz 044

## Paper Solution

## Flow Chart
![image](https://github.com/user-attachments/assets/bc28cfb2-3a3b-4a2f-b699-1b0dd039114a)

## Code
```.py
class RainDrop:
    def pour(self, n)-> str:
        result = ""
        details = []

        if n % 3 == 0:
            result += "Pling"
            details.append("divisible by 3")
        if n % 5 == 0:
            result += "Plang"
            details.append("divisible by 5")
        if n % 7 == 0:
            result += "Plong"
            details.append("divisible by 7")

        if not details:
            return f"{n} is not divisible by 3, 5, or 7, so the result is \"{n}\""

        divisors_text = ", ".join(details)
        return f"{n} is {divisors_text}, so the result is {result}"

print(RainDrop().pour(28))
print(RainDrop().pour(30))
print(RainDrop().pour(34))
```
## Proof of work
![image](https://github.com/user-attachments/assets/0f20b7c6-7c97-4b25-8523-c03c66fb30d9)
