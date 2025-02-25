# Quiz 043

## Paper Solution

## Flow Chart
## Code
```.py
class palNum():
    def __init__(self, A:int, B:int):
        self.A = A
        self. B = B

    def get_pal_list(self):
        palindromic_numbers = []
        for num in range(self.A, self.B + 1):
            str_num = str(num)
            if str_num == str_num[::-1]:
                palindromic_numbers.append(num)
        return palindromic_numbers

print(palNum(1,9).get_pal_list())
print(palNum(10,199).get_pal_list())
```
## Proof of work
![image](https://github.com/user-attachments/assets/2a9ae4a0-12ac-45ce-bd0e-7e11ffcc8c68)
