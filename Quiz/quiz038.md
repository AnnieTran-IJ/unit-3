# Quiz 038

## Code

```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class mystery(MDApp):
    def build(self):
        return

class MysteryPageA(MDScreen):
    def next(self):
        self.parent.current = "MysteryPageB"

class MysteryPageB(MDScreen):
    def next(self):
        self.parent.current = "MysteryPageA"

t = mystery()
t.run()
```

from mystery.kv
```.py
ScreenManager:
    id: scr_manager
    MysteryPageA:
        name: "MysteryPageA"
    MysteryPageB:
        name: "MysteryPageB"

<MysteryPageA>:
    MDCard:
        orientation: "vertical"
        size_hint: .8, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        radius: [20]
        md_bg_color: "#2e353d"

        MDLabel:
            text: "This is mystery page A. You pressed the button"
            font_style: "H3"
            size_hint: 1, None
            halign: "center"
            color: "#f5b130"



        MDFillRoundFlatButton:
            text: "Click Me"
            md_bg_color: "#6a4c3c"
            on_release: root.next()
            pos_hint: {"center_x": 0.5}

<MysteryPageB>:
    MDCard:
        orientation: "vertical"
        size_hint: .8, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        radius: [20]
        md_bg_color: "#2e353d"

        MDLabel:
            text: "This is mystery page B. You pressed the button"
            font_style: "H3"
            size_hint: 1, None
            halign: "center"
            color: "#f5b130"


        MDFillRoundFlatButton:
            text: "Click Me"
            md_bg_color: "#6a4c3c"
            on_release: root.next()
            pos_hint: {"center_x": 0.5}

```
## Proof of work
![image](https://github.com/user-attachments/assets/e17e8bf9-d7bb-4ed2-98e6-e3519487380b)

