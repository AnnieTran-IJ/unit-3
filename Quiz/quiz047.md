# Quiz 047

## Paper Solution

## Code
```.py
class CalorieCount:
    def __init__(self, daily_limit: int):
        self.daily_limit = daily_limit
        self.daily_intake = 0
        self.protein = 0
        self.carbs = 0
        self.fat = 0

    def addMeal(self, cal, pro, car, fat):
        self.daily_intake += cal
        self.protein += pro
        self.carbs += car
        self.fat += fat

    def getProteinPercentage(self) -> float:
        if self.daily_intake == 0:
            return self.daily_intake
        else:
            return 4* self.protein/self.daily_intake

    def onTrack(self) -> bool:
        return self.daily_intake <= self.daily_limit

sunday = CalorieCount(1500)

sunday.addMeal(716, 38, 38, 45)
sunday.addMeal(230, 16, 8, 16)
sunday.addMeal(568, 38, 50, 24)

print(sunday.onTrack())
print(sunday.getProteinPercentage())
```
## Proof of work
![image](https://github.com/user-attachments/assets/03b3a3d4-6402-41d8-a185-5a9974290fb0)
