import sqlite3
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog, dialog
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDCheckbox

from quiz.secure_password import check_password

Window.size = (380, 640)
class HomeScreen(Screen):
    last_click_time = NumericProperty(0)
    def on_logo_click(self):
        current_time = time.time()
        print(f"Logo clicked at: {current_time}, Last click was at: {self.last_click_time}")

        if current_time - self.last_click_time < 0.5:  # Check for double-click
            print("Double-click detected. Switching to SignInSecretScreen.")
            app = MDApp.get_running_app()
            app.root.ids.scr_manager.current = "SignInSecretScreen"
        else:
            print("Single click detected. Waiting for the next click.")

        self.last_click_time = current_time


    selected_flavors = DictProperty({})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.flavor_menu = None

    def create_flavor_menu(self, dropdown_item, product_name):
        # Define the flavor options
        flavors = ["Select Flavor", "Vanilla", "Chocolate", "Caramel", "Mint", "Mango"]

        max_menu_height = min(Window.height * 0.5, len(flavors) * dp(400))

        menu_items = [
            {
                "text": flavor,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=flavor: self.set_flavor(dropdown_item, product_name, x),
            }
            for flavor in flavors
        ]

        self.flavor_menu = MDDropdownMenu(
            caller=dropdown_item,
            items=menu_items,
            width_mult=4,
            max_height=max_menu_height
        )
        self.flavor_menu.open()

    def set_flavor(self, dropdown_item, product_name, flavor):
        if flavor == "Select Flavor":
            if product_name in self.selected_flavors:
                del self.selected_flavors[product_name]
                print(f"Flavor deselected for {product_name}. Current selections: {self.selected_flavors}")
                dropdown_item.text = flavor
                self.flavor_menu.dismiss()
        else:
            dropdown_item.text = flavor
            self.selected_flavors[product_name] = flavor
            print(f"Selected flavors: {self.selected_flavors}")
            self.flavor_menu.dismiss()

    def add_to_cart(self):
        if not self.selected_flavors:
            dialog = MDDialog(
                title="Please choose at least 1 preferred flavor",
                size_hint=(0.8, 0.3),
                buttons=[MDRaisedButton(text="OK", on_release=lambda obj: self.close_dialog(dialog, obj))]
            )
            dialog.open()
            print("No items selected to add to the cart.")
            return

        product_list_str = ", ".join([f"{product}: {flavor}" for product, flavor in self.selected_flavors.items()])

        try:
            con = sqlite3.connect('sugarbliss_database.db')
            cursor = con.cursor()
            cursor.execute("""
                INSERT INTO order_table (customer_name, product_list)
                VALUES (?, ?)
            """, ("", product_list_str))

            con.commit()
            print(f"Order added to the database: {product_list_str}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            dialog = MDDialog(
                title="Your preference has been saved",
                text="Edit your option or view order to make payment!",
                size_hint=(0.8, 0.3),
                buttons=[MDRaisedButton(text="OK", on_release=lambda obj: self.close_dialog(dialog, obj))]
            )
            dialog.open()
            con.close()

    def add_to_saved_order(self):
        if not self.selected_flavors:
            dialog = MDDialog(
                title="Please choose at least 1 preferred flavor",
                size_hint=(0.8, 0.3),
                buttons=[MDRaisedButton(text="OK", on_release=lambda obj: self.close_dialog(dialog, obj))]
            )
            dialog.open()
            print("No items selected to save.")
            return

        product_list_str = ", ".join([f"{product}: {flavor}" for product, flavor in self.selected_flavors.items()])
        try:
            con = sqlite3.connect('sugarbliss_database.db')
            cursor = con.cursor()

            cursor.execute("""
                INSERT INTO order_table (customer_name, product_list)
                VALUES (?, ?)
            """, ("", product_list_str))

            con.commit()  # Save changes to the database
            print(f"Order saved to the database: {product_list_str}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            con.close()
            # # Reset dropdowns
            # self.selected_flavors.clear()
            # self.reset_dropdowns()

        # Navigate to the saved order screen
        app = App.get_running_app()
        app.root.ids.scr_manager.current = "ViewOrderScreen"

    def reset_dropdowns(self):
        flavor_dropdown_ids = [
            self.ids.flavor_dropdown_1,
            self.ids.flavor_dropdown_2,
            self.ids.flavor_dropdown_3,
            self.ids.flavor_dropdown_4
        ]

        for dropdown in flavor_dropdown_ids:
            dropdown.text = "Select Flavor"

        self.selected_flavors.clear()  # Clear selected flavors dictionary
        print("Cart has been cleared, all dropdowns reset.")

    def close_dialog(self, dialog, obj):
        dialog.dismiss()

class ViewOrderScreen(Screen):
    def on_enter(self, *args):
        self.load_latest_order()

    def load_latest_order(self):
        try:
            con = sqlite3.connect('sugarbliss_database.db')
            cursor = con.cursor()
            cursor.execute("""
                SELECT product_list FROM order_table
                ORDER BY ID DESC LIMIT 1
            """)
            result = cursor.fetchone()

            if not result:
                # If no orders exist
                self.ids.total_price.text = "$0.00"
                self.show_no_orders_message()
                return

            product_list = result[0]
            container = self.ids.product_list_container
            container.clear_widgets()
            total_price = 0.0
            for item in product_list.split(", "):
                product, flavor = item.split(": ")
                price = self.get_product_price(product)
                total_price += price
                cursor.execute("SELECT ID FROM order_table ORDER BY ID DESC LIMIT 1")
                latest_order = cursor.fetchone()

                if latest_order:
                    latest_order_id = latest_order[0]

                    cursor.execute("""
                                                UPDATE order_table
                                                SET total_price = ?
                                                WHERE ID = ?
                                            """, (total_price, latest_order_id))

                    con.commit()
                    print(f"A total price of '{total_price}' saved to order ID {latest_order_id}.")
                container.add_widget(self.create_product_row(product, flavor, price))

            self.ids.total_price.text = f"${total_price:.2f}"

        except Exception as e:
            print(f"An error occurred while loading the order: {e}")

        finally:
            con.close()

    def create_product_row(self, product, flavor, price):
        row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="40dp")
        row.add_widget(MDLabel(text=f"{product} ({flavor})", halign="left", font_name= "Poppins-Regular", font_size= 17))
        row.add_widget(MDLabel(text=f"${price:.2f}", halign="right", font_name= "Poppins-Regular", font_size= 17))
        return row

    def get_product_price(self, product):
        product_prices = {
            "Ice Cream": 5.00,
            "Rainbow Sorbet": 3.00,
            "Fruit Tart": 6.00,
            "Mousse Cake": 25.00
        }
        return product_prices.get(product, 0.0)

    def show_no_orders_message(self):

        container = self.ids.product_list_container
        container.clear_widgets()
        container.add_widget(MDLabel(text="No orders found.", halign="center"))

class PersonalInfoScreen(Screen):
    selected = StringProperty(None)

    def on_pre_enter(self):
        self.populate_address_grid()

    def populate_address_grid(self):
        self.ids.address_grid.clear_widgets()

        connection = sqlite3.connect("sugarbliss_database.db")
        cursor = connection.cursor()
        query = "SELECT ID, customer_name, phone_number, address FROM customer_database"
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            address_id, customer_name, phone_number, address = row

            layout = MDBoxLayout(orientation="horizontal", spacing=dp(10), size_hint_y=None, height=dp(56))

            # Checkbox
            checkbox = MDCheckbox(group="addresses", size_hint=(None, None), size=(dp(48), dp(48)))
            checkbox.bind(active=lambda instance, value, a_id=address_id: self.set_selected_address(value, a_id))

            # Label for address details
            label = MDLabel(
                text=f"{customer_name}\n{phone_number}\n{address}",
                font_name= "Poppins-Regular",
                font_size= 17,
                size_hint_x=1
            )

            # Add widgets to the layout
            layout.add_widget(checkbox)
            layout.add_widget(label)


            self.ids.address_grid.add_widget(layout)

    def set_selected_address(self, active, address_id):

        if active:
            self.selected = str(address_id)
            print(f"Selected address ID: {self.selected}")

    def confirm_information(self):
        print("Information confirmed!")

        if self.selected:
            try:
                con = sqlite3.connect("sugarbliss_database.db")
                cursor = con.cursor()


                cursor.execute("""
                        SELECT customer_name FROM customer_database WHERE ID = ?
                    """, (self.selected,))
                customer_info = cursor.fetchone()

                if customer_info:
                    customer_name = customer_info[0]
                    cursor.execute("SELECT ID FROM order_table ORDER BY ID DESC LIMIT 1")
                    latest_order = cursor.fetchone()

                    if latest_order:
                        latest_order_id = latest_order[0]
                        cursor.execute("""
                                UPDATE order_table
                                SET customer_name = ?
                                WHERE ID = ?
                            """, (customer_name, latest_order_id))

                        con.commit()
                        print(f"Customer name '{customer_name}' saved to order ID {latest_order_id}.")
                        self.show_confirmation_popup()
                    else:
                        print("No orders found in the database.")
                        self.show_error_popup()
                else:
                    print(f"No customer found for address_id {self.selected}.")
                    self.show_error_popup()

            except sqlite3.Error as e:
                print(f"Database error: {e}")
                self.show_error_popup()
            finally:
                con.close()
        else:
            self.show_error_popup()
    def close_dialog(self, dialog, obj, go_home=False):
        dialog.dismiss()
        if go_home:
            app = App.get_running_app()
            app.switch_to_home()
    def show_confirmation_popup(self):
        dialog = MDDialog(
            title="Success",
            text="Order successfully placed!",
            size_hint=(0.8, 0.3),
            buttons=[MDRaisedButton(text="OK", on_release=lambda obj: self.close_dialog(dialog, obj, go_home=True))],
        )
        dialog.open()

    def show_error_popup(self):
        """Shows an error popup if no address is selected."""
        dialog = MDDialog(
            title="Error",
            text="Please select an address set.",
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(text="Close", on_release=lambda obj: self.close_dialog(dialog, obj))
            ],
        )
        dialog.open()

class LogInScreen(Screen):

    def validate_login(self):
        username = self.ids.username_field.text
        phoneno = self.ids.phoneno_field.text
        address = self.ids.address_field.text


        if not username or not phoneno or not address:
            self.show_error_popup("Please fill in all fields.")
            return

        if not phoneno.isdigit():
            self.show_error_popup("Phone number should only contain digits.")
            return
        if self.check_if_exists(username, phoneno, address):
            self.show_error_popup("This information already exists. Please change the information.")
        else:
            self.save_to_database(username, phoneno, address)
            self.show_success_popup()

    def check_if_exists(self, username, phoneno, address):
        try:
            con = sqlite3.connect('sugarbliss_database.db')
            cursor = con.cursor()

            cursor.execute("""
                SELECT * FROM customer_database 
                WHERE customer_name = ? AND phone_number = ? AND address = ?
            """, (username, phoneno, address))
            result = cursor.fetchone()

            return result is not None

        except Exception as e:
            print(f"An error occurred while checking if data exists: {e}")
            return False

        finally:
            con.close()

    def save_to_database(self, username, phoneno, address):
        try:
            con = sqlite3.connect('sugarbliss_database.db')  # Connect to the customer database
            cursor = con.cursor()

            cursor.execute("""
                INSERT INTO customer_database(customer_name, phone_number, address)
                VALUES (?, ?, ?)
            """, (username, phoneno, address))

            con.commit()
            print(f"User data saved: {username}, {phoneno}, {address}")

        except Exception as e:
            print(f"An error occurred:  {e}")

        finally:
            con.close()

    def show_success_popup(self):

        dialog = MDDialog(
            title="Login Successful",
            text="Welcome! Your address has been saved.",
            size_hint=(0.8, 0.3),
            buttons=[MDRaisedButton(text="Close", on_release=lambda obj: self.close_dialog(dialog))]
        )
        dialog.open()
        self.clear_info()
        app = MDApp.get_running_app()
        app.switch_to_personal_info()  # Assuming this switches to a personal info screen.

    def show_error_popup(self, message):
        dialog = MDDialog(
            title="Error",
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[MDRaisedButton(text="Close", on_release=lambda obj: self.close_dialog(dialog))]
        )
        dialog.open()

    def close_dialog(self, dialog):
        dialog.dismiss()

    def clear_info(self):
        self.ids.username_field.text = ""
        self.ids.phoneno_field.text = ""
        self.ids.address_field.text = ""


class SignInSecretScreen(Screen):
    passcode = StringProperty("")

    def update_passcode(self, digit):
        self.passcode += digit
        self.ids.passcode_display.text = "*" * len(self.passcode)

    def validate_passcode(self):
        pin_is_correct = check_password("$pbkdf2-sha256$30000$8H7POcfY2/u/9x7DGOO81w$bn3RmvUVz8IsUbrE4p7lWZPtaOcpm6V0ILt16za3eUY", self.passcode)
        if pin_is_correct:
            app = MDApp.get_running_app()
            self.clear_passcode()
            app.switch_to_admin()
            Clock.schedule_once(self.clear_passcode, 1)
        else:
            self.ids.passcode_display.text = "Incorrect!"
            Clock.schedule_once(self.clear_passcode, 1)

    def clear_passcode(self, *args):
        self.passcode = ""
        self.ids.passcode_display.text = ""

class AdminScreen(Screen):
    def on_pre_enter(self, *args):
        Window.size = (700, 640)
        self.populate_admin_dashboard()
        self.load_data_table()
        self.update_statistics()

    def connect_to_db(self):
        try:
            con = sqlite3.connect("sugarbliss_database.db")
            return con
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def populate_admin_dashboard(self):
        con = self.connect_to_db()
        if not con:
            return

        try:
            cursor = con.cursor()

            cursor.execute("SELECT customer_name, product_list, total_price FROM order_table")
            orders = cursor.fetchall()

            dashboard_data = []
            for customer_name, product_list, total_price in orders:
                if total_price is None:
                    print(f"Error: Missing total_price for order: {customer_name}")
                    continue

                order_list = product_list
                profit = int(total_price * 0.3)
                dashboard_data.append((customer_name, order_list, total_price, profit, "Order Received"))

            cursor.executemany("""
                INSERT INTO admin_dashboard (customer_name, order_list, total_payment, profit, progress)
                VALUES (?, ?, ?, ?, ?)
            """, dashboard_data)

            con.commit()
        except sqlite3.Error as e:
            print(f"Error populating admin_dashboard: {e}")
        finally:
            con.close()

    def fetch_admin_dashboard_data(self):
        con = self.connect_to_db()
        if not con:
            return [], 0, 0, "N/A"

        try:
            cursor = con.cursor()
            cursor.execute("SELECT ID, customer_name, order_list, total_payment, profit, progress FROM admin_dashboard")
            data = cursor.fetchall()

            cursor.execute("SELECT order_list, COUNT(*) FROM admin_dashboard GROUP BY order_list ORDER BY COUNT(*) DESC LIMIT 1")
            popular_product = cursor.fetchone()
            most_popular = popular_product[0] if popular_product else "N/A"

            cursor.execute("SELECT SUM(total_payment), SUM(profit) FROM admin_dashboard")
            totals = cursor.fetchone()
            total_revenue, total_profit = totals if totals else (0, 0)

            return data, total_revenue, total_profit, most_popular
        except sqlite3.Error as e:
            print(f"Error fetching admin dashboard data: {e}")
            return [], 0, 0, "N/A"
        finally:
            con.close()

    def load_data_table(self):
        data, _, _, _ = self.fetch_admin_dashboard_data()

        column_data = [
            ("ID", dp(30)),
            ("Progress", dp(50)),
            ("Customer Name", dp(40)),
            ("Order List", dp(60)),
            ("Total Payment", dp(30)),
            ("Profit", dp(30))
        ]
        row_data = [
            (
                str(row[0]),  row[5], row[1], row[2],
                f"${row[3]:.2f}", f"${row[4]:.2f}"
            )
            for row in data
        ]

        self.data_table = MDDataTable(
            size_hint=(0.9, 0.5),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            column_data=column_data,
            row_data=row_data,
            check=True
        )


        self.data_table.bind(on_row_press=self.on_row_press)
        self.add_widget(self.data_table)

    def on_row_press(self, instance_table, instance_row):
        selected_row = instance_table.get_row_checks()
        if selected_row:
            row_data = selected_row[0]  # Get the selected row
            self.show_progress_dropdown(row_data)

    def show_progress_dropdown(self, row_data):
        menu_items = [
            {"text": "Order Received", "on_release": lambda x="Order Received": self.update_progress(row_data, x)},
            {"text": "Done Cooking", "on_release": lambda x="Done Cooking": self.update_progress(row_data, x)},
            {"text": "Delivered", "on_release": lambda x="Delivered": self.update_progress(row_data, x)},
        ]
        self.progress_menu = MDDropdownMenu(
            caller=self.data_table,
            items=menu_items,
            width_mult=4
        )
        self.progress_menu.open()

    def update_progress(self, row_data, new_status):
        order_id = int(row_data[0])  # Assuming the first column is the ID
        con = self.connect_to_db()
        if not con:
            return

        try:
            cursor = con.cursor()
            cursor.execute(
                "UPDATE admin_dashboard SET progress = ? WHERE ID = ?", (new_status, order_id)
            )
            con.commit()
            print(f"Updated order {order_id} to {new_status}")
        except sqlite3.Error as e:
            print(f"Error updating progress: {e}")
        finally:
            con.close()

        # Refresh the data table
        self.load_data_table()

    def update_statistics(self):
        data, total_revenue, total_profit, most_popular = self.fetch_admin_dashboard_data()

        self.ids.most_popular_label.text = most_popular
        self.ids.total_revenue_label.text = f"${total_revenue:.2f}"
        self.ids.total_profit_label.text = f"${total_profit:.2f}"
class sugarbliss(MDApp):
    def build(self):
        return

    # switching pages functions
    def switch_to_saved_order(self):
        self.root.ids.scr_manager.current = "ViewOrderScreen"
    def switch_to_personal_info(self):
        self.root.ids.scr_manager.current = "PersonalInfoScreen"
    def switch_to_home(self):
        self.root.ids.scr_manager.current = "HomeScreen"
    def switch_to_login(self):
        self.root.ids.scr_manager.current = "LogInScreen"
    def switch_to_admin(self):
        self.root.ids.scr_manager.current = "AdminScreen"
    def switch_to_secret_screen(self):
        self.root.ids.scr_manager.current = "SignInSecretScreen"


t = sugarbliss()
t.run()