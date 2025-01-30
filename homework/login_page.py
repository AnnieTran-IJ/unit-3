from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from my_lib import DatabaseManager

class LoginScreen(Screen):
    def try_login(self):
        print("the user tried to login")

class SignupScreen(Screen):
    def try_register(self):
        username = self.ids.signup_name.text
        email = self.ids.signup_email.text
        pw1 = self.ids.signup_password.text
        pw2 = self.ids.confirm_password.text

        #validation
        #1/ is user and password unique?
        check1_query = f"SELECT * from user where username = 'username' or email = '{email}'"
        db =  DatabaseManager(name="login.sql")
        results = db.search(query=check1_query)
        db.close()
        print(results)

        if len(results)>0:
            #user or email already used
            self.ids.signup_name.error = True
            self.ids.signup_name.helper_text = "username or email already in use"
            return

        #2/does password match?
        if pw1 != pw2:
            self.ids.signup_password.error = True
            self.ids.signup_name.helper_text = "Passwords don't align. Please check again"
            return

        #3/ check if the field is not empty
        if username is None or pw1 is None or pw2 is None or email is None:
            self.ids.signup_name.error = True
            self.ids.signup_name.helper_text = "All information needs to be fill out"
            return
        #4/ check if email has the @ mark

class login_page(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Light"
        query_table = """
        create table if not exists user(
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            email text unique not null,
            password VARCHAR(256)

        )
        """

        x = DatabaseManager(name = "login.sql")
        x.run_save(query=query_table)
        x.close()

    def switch_to_signup(self):
        self.root.ids.scr_manager.current = "SignupScreen"

    def switch_to_login(self):
        self.root.ids.scr_manager.current = "LoginScreen"

t = login_page()
t.run()