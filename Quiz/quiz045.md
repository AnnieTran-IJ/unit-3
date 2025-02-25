# Quiz 045

## Paper Solution

## Flow Chart
![image](https://github.com/user-attachments/assets/0adfd0cc-ce53-4dc5-898a-29ffc21d32ff)

## Code
```.py
class WordCounter:
    def __init__(self, text:str):
        self.text = text
        self.count = {}

    def wordcounter(self):
        words = self.text.split()
        for word in words:
            word = word.lower().strip(".,!?;:")
            if word in self.count:
                self.count[word] += 1
            else:
                self.count[word] = 1
        for word, count in self.count.items():
            print(f"{word}: {count}")


text = "This is a sample text. It contains some words that will be counted."
t = WordCounter(text)
print(t.wordcounter())
```
## Proof of work
![image](https://github.com/user-attachments/assets/f2bf7d92-52f8-47a3-8eb4-1795b542a22b)
