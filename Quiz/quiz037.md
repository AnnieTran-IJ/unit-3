# Quiz 037

## Diagram
![image](https://github.com/user-attachments/assets/c97cbf52-3f0f-40e8-a9c1-c7d48115cca0)

## Code
```.py
from kivymd.app import MDApp

class quiz037(MDApp):
    def build(self):
        self.current_player = 'X'
        self.positions = [''] * 9
        self.colors = {'X': ("#9c2914", "#ffffff"), 'O': ("#eac590", "#000000")}

    def take_spot(self, position: int):
        if not self.positions[position]:
            button = self.root.ids[f"btn_{position}"]
            self.positions[position] = self.current_player
            bg_color, text_color = self.colors[self.current_player]
            button.md_bg_color = bg_color
            button.text_color = text_color
            button.text = self.current_player

            if self.check_winner():
                self.root.ids.turn.text = f"{self.current_player} Wins!"
                self.disable_all_buttons()
                return

            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.root.ids.turn.text = f"{self.current_player}'s turn."
        else:
            self.root.ids.error.text = "Spot already taken!"

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]             # diagonals
        ]
        for line in win_conditions:
            if self.positions[line[0]] == self.positions[line[1]] == self.positions[line[2]] != '':
                return True
        return False

    def disable_all_buttons(self):
        for i in range(9):
            self.root.ids[f"btn_{i}"].disabled = True

t = quiz037()
t.run()
```

quiz037.kv

```.py
Screen:
    MDBoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 20

        MDLabel:
            text: "Annie's Tic Tac Toe "
            halign: "center"
            font_style: "H3"

        MDLabel:
            id: turn
            text: "X's turn"
            halign: "center"

        MDLabel:
            id: error
            text: ""
            halign: "center"
            theme_text_color: "Error"

        GridLayout:
            cols: 3
            spacing: 10
            size_hint: None, None
            size: self.minimum_size
            halign: "center"
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

            MDRaisedButton:
                id: btn_0
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(0)

            MDRaisedButton:
                id: btn_1
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(1)

            MDRaisedButton:
                id: btn_2
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(2)

            MDRaisedButton:
                id: btn_3
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(3)

            MDRaisedButton:
                id: btn_4
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(4)

            MDRaisedButton:
                id: btn_5
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(5)

            MDRaisedButton:
                id: btn_6
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(6)

            MDRaisedButton:
                id: btn_7
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(7)

            MDRaisedButton:
                id: btn_8
                text: ""
                font_size: "34pt"
                size_hint: None, None
                size: 100, 100
                md_bg_color: "#1e2832"
                on_press: app.take_spot(8)
```
## Proof of work
![image](https://github.com/user-attachments/assets/712ea988-2c03-466e-9f20-ce3a62944686)

![image](https://github.com/user-attachments/assets/9bb207b8-252b-4237-87f9-ad43c3cf17dd)
