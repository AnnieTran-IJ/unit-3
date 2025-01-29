# Quiz 036

## Code
```.py
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager


class ScreenOne(MDScreen):
    def next(self):
        self.parent.current = "ScreenTwo"


class ScreenTwo(MDScreen):
    def next(self):
        self.parent.current = "ScreenOne"


class quiz036(MDApp):
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name="ScreenOne"))
        screen_manager.add_widget(ScreenTwo(name="ScreenTwo"))

        return screen_manager

# Run the app
t = quiz036()
t.run()
```
From quiz036.kv

```.py
ScreenManager:
    id: scr_manager
    ScreenOne:
        name: "ScreenOne"
    ScreenTwo:
        name: "ScreenOne"

# Screen 1 - Light Mode
<ScreenOne>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            text: "Annie"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            font_style: "H3"
            size_hint: None, None
            size: 500, 500
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Dark Mode"
            md_bg_color: 0, 0, 1, 1
            size_hint: None, None
            size: 200, 50
            pos_hint: {"x": 0, "y": 0}
            on_release: root.next()


# Screen 2 - Dark Mode
<ScreenTwo>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size

        MDLabel:
            text: "Annie"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H3"
            size_hint: None, None
            size: 500, 500
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDRaisedButton:
            text: "Light Mode"
            md_bg_color: 1, 0, 1, 1
            size_hint: None, None
            size: 200, 50
            pos_hint: {"x": 0, "y": 0}
            on_release: root.next()

```
## Proof of work
![image](https://github.com/user-attachments/assets/7881305f-b59d-44c5-82e6-5b303dfec079)


