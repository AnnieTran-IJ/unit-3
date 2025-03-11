# Unit 3: A Food Ordering Application
![image](https://github.com/user-attachments/assets/d7fd685c-2ace-4ff2-87b0-2c121f76b2ef)

## Criteria A: Planning

### Problem definition
My client runs a small restaurant with limited seating, which creates challenges during peak hours when many customers are turned away or face long wait times. She wants to introduce a take-out system to better serve customers who cannot dine in. However, the current process for take-out orders is inefficient and prone to errors. Customers must call in their orders, which often leads to miscommunication about menu items, quantities, and order details. There’s no system for customers to review or save their orders, nor is there a way to store personal information for future use, requiring them to repeatedly provide the same details.

The restaurant staff also struggles to manage order tracking. They lack a system for keeping track of which order is made and which are not, and the owner does not receive timely notifications of new orders, delaying food preparation. Additionally, the owner needs a secure way to manage administrative tasks, like monitoring revenue and other business data, but there’s no system in place to ensure she alone can access this information. These challenges are causing inefficiencies, errors, and frustration for both the customers and the restaurant staff.

### Proposed Solution
My proposed solution is a GUI-based application designed to address both the customer and client's challenges in the transition of the take-out process. The system will display all menu items on the main page, allowing users to specify product quantities and place orders remotely. Customers can save orders, review receipts before checkout, and store personal information profiles for future use. Notifications will be sent to the owner when orders are placed, and customers will be informed when their food is ready for pick-up. To ensure security, only the owner will access the administrative side using a passcode.

I chose Python as the programming language for its readable syntax, extensive libraries, and cross-platform compatibility, making it ideal for GUI development. The KivyMD framework, a Material Design extension for Kivy, will be used to create modern and responsive interfaces with pre-designed components.

SQLite is the preferred data storage solution due to its lightweight, serverless nature, making it suitable for local hosting. Unlike CSV files or MySQL, SQLite ensures structured, efficient data management with minimal dependencies and no need for a server.

By integrating Python, KivyMD, and SQLite, this solution delivers a user-friendly, efficient, and secure application tailored to the client’s needs.

### Success Criteria
1. The solution provides a way for the user to add and delete food items from their order.
→ Issue tackled: "Customers often call in their orders, which often leads to miscommunication about menu items  and order details."
2. The solution provides a way for the user to save, view orders, and see the total price before purchasing.
→ Issue tackled: "There’s no system for customers to review or save their orders."
3. The solution allows the user to save personal information, such as their username, address, and phone number, in a database for future use.
→ Issue tackled: "There’s no system to store personal information for future use, requiring customers to repeatedly provide the same details."
4. The solution sends order details to the restaurant owners once the user places the order. 
→ Issue tackled: "The owner does not receive timely notifications of new orders, delaying food preparation."
5. The solution allows the restaurant owner to keep track of the progress using checkboxes.
→ Issue tackled: "They lack a system for keeping track of which order is made and which are not.”

#### Client Approval of Success Criteria
![Documentation Project 3  Comp SCi](https://github.com/user-attachments/assets/6d822f41-8217-4184-b3dd-bff03434c07a)
**Fig 1.** Email conversation thread with the client.

### Criteria B: Design
#### System Diagram
![Documentation Project 3  Comp SCi (1)](https://github.com/user-attachments/assets/685b4c0e-a8da-4068-b3fb-c2e6fb683eec)
**Fig 2.** System Diagram

#### UML Diagram
**Fig 3.** UML Diagram
![image](https://github.com/user-attachments/assets/c8c81dd4-c08a-4976-84ba-ab4e71253020)

#### ER Diagram
![image](https://github.com/user-attachments/assets/25185a99-3a71-4537-b769-f1982ac4d5d9)
**Fig 4.** ER Diagram

#### Flow Diagrams
![flowchart drawio-3](https://github.com/user-attachments/assets/af0169a9-687c-48ae-b766-1de5db341895)
**Fig 5.** Function create_product_row() and load_latest_order() in class ViewOrder:
![flowchart drawio-2](https://github.com/user-attachments/assets/475b83f8-2140-4cf7-836a-fb614d30fb96)
**Fig 6.** Function create_flavor_menu() andadd_to_saved_order() in class HomeScreen
![flowchart drawio-1](https://github.com/user-attachments/assets/06667f55-8cc5-4800-bf26-7f3fba9b786b)
**Fig 7.** Function validate_login() and save_to_database() in class LoginScreen
#### Database Picture:
*Screenshot taken from file sugarbliss_database.db*
1. Table customer_database:
![image](https://github.com/user-attachments/assets/ab192359-4390-4828-8296-0ebbe344c5c6)

2.Table order_table:
![image](https://github.com/user-attachments/assets/16522848-dfb2-4921-acfb-7bcd8720746d)

3. Table admin_dashboard:
![image](https://github.com/user-attachments/assets/56e90d7b-389b-47bd-a301-83f1d7fd20c5)

#### Record of Task
| **No.** | **Planned Action**                                            | **Planned Outcome **                                                                                                                                                            | **Time estimate** | **Completion date** | **Criteria** |
|---------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|---------------------|--------------|
| 1       | Meet with client                                              | Understand the client’s needs and write a problem definition                                                                                                                    | 40mins            | February 1          | A            |
| 2       | Suggest and finalize success criteria with the client         | Meet with the client again and receive feedback on proposed success criteria for the solution                                                                                   | 30 mins           | February 4          | A            |
| 3       | Design the wireframe of the program                           | Have an overview of the layout of the whole program                                                                                                                             | 35 mins           | February 5          | B            |
| 4       | Create flow diagrams                                          | Envision for each class and each screen will include and function                                                                                                               | 25mins            | February 6          | B            |
| 5       | Create all the diagrams required                              | Envision the backend structure and gave ER and UML diagram ready for feedback                                                                                                   | 45mins            | February 9          | B            |
| 6       | Develop interface for the HomeScreen                          | Set layout for the heading, 2 navigation buttons at the bottom and dropdown for selection                                                                                       | 30mins            | February 10         | B            |
| 7       | Develop interface for ViewOrderScreen                         | Imitate a receipt layout and add total text fields and navigation bar at the bottom                                                                                             | 30mins            | February 11         | B            |
| 8       | Develop interface for the LogInScreen                         | Set layout for the screen that allows user to create their new set of personal information (LogInScreen) + checkbox for user to choose their preferred set (PersonalInfoScreen) | 25mins            | February 15         | C            |
| 9       | Develop an interface for the admin end                        | Create a PIN-entry screen + layout for admin dashboard with statistics part                                                                                                     | 35mins            | February 17         | C            |
| 10      | Write function to switch screen                               | Decide on the flow of the program and create functions for the program to switch screen accordingly                                                                             | 15mins            | February 23         | C            |
| 11      | Write functions for HomeScreen and ViewOrderScreen            | Create a function for the user to open the dropdown flavor and save the order to database                                                                                       | 30mins            | February 23         | C            |
| 12      | Write functions for PersonalInfoScreen and LogInScreen        | Create a function to validate the user’s input, save to the customer’s database, and load data dynamically on screen                                                            | 120mins           | February 25         | C            |
| 13      | Start debugging for dynamic function and validation algorithm | Fix the program issue with saving data into the database and retrieving it to display on screen + enhanced layers of validation for LogInScreen                                 | 30mins            | February 26         | C            |
| 14      | Write functions for admin-side screens                        | Hash the access PIN, add validation, and display data dynamically to admin dashboard                                                                                            | 55mins            | February 28         | C            |
| 15      | Debug data fetching process for AdminScreen                   | Fix the issue with the admin database when accessing to other tables and found a null value                                                                                     | 40mins            | March 01            | C            |
| 16      | Write function to calculate statistics for admin              | Write functions to calculate the profit, revenue, and best-selling product on the menu                                                                                          | 45mins            | March 02            | C            |
| 17      | Outline the documentation for Criteria C                      | List all techniques used in Criteria C and outline for detailed explanation                                                                                                     | 20mins            | March 05            | C            |
| 18      | Final touch on user interface                                 | Design brand logo, change kivy font and color scheme                                                                                                                            | 35mins            | March 08            | B & C        |
| 19      | Create test plan and test the system                          | Ensure the progrm is fully functional and user-friendly                                                                                                                         | 35 mins           | March 09            | C            |
| 20      | Write a detailed explanation for the development part         | Outline and draft explanation paragraph for top 3 functions in the program using technical knowledge and creativity                                                             | 50 mins           | March 11            | C            |
| 21      | Record demonstration video                                    | Create a 4-min video demonstrate how the program work using Test Plan and Success Criteria                                                                                      | 10mins            | March 11            | D            |
#### Test Plan:
| Success Criteria Addressed                                                                                                                     | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Output                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. The solution provides a way for the user to add and delete food items from their order.                                                     | 1. Run the program sugarbliss.py<br>2. From the Home screen, select the flavor “Vanilla” for the option “Ice Cream.”<br>3. Select “Caramel” for the option “Rainbow Sorbet”<br>4. Click “View Order” button to check the list of products selected <br>5. Click on “<-” button to return to HomeScreen<br>6. Delete item “Ice Cream” by selecting flavor “Select Flavor”<br>7. Click “View Order” button to check the updated list of products after deletion | Home Screen displays a list of food including Ice Cream, Rainbow Sorbet, Fruit Tart, Mousse Cake, and a dropdown with lists of flavor to choose from<br>After step 4, The screen “Your Order” shows 2 rows of Ice Cream and Rainbow Sorbet as its flavor.<br>After step 7, The screen “Your Order” shows only 1 row for Rainbow Sorbet                                   |
| 2. The solution provides a way for the user to save, view orders, and see the total price before purchasing.                                   | Run the program sugarbliss.py<br>From the Home screen, select "Mousse Cake" flavor as "Chocolate" ($25). <br>Click button “ Add to cart” to save current selection<br>Click popup message’s “OK” button<br>Click button “View order” to switch to screen                                                                                                                                                                                                      | After step 2, a message pops up that says “Your preference has been saved. Edit your option or view order to make payment!”<br>After step 4,  View Order screen displays the order with 1 row for Mousse Cake as the selected product and a total price of 25$ at the bottom of the screen                                                                               |
| 3. The solution allows the user to save personal information, such as their username, address, and phone number, in a database for future use. | Run the program sugarbliss.py<br>From the Home screen, choose at least 1 flavor from the list of desserts<br> Click on “View Order” button, “Proceed” button and then “Add New” button<br>Enter "Anything" as the username, "ISAK" as the address, and "987654321" as the phone number. <br>Click “Save”<br>Select the option with the username of Anything that has just been added to screen Personal Information<br>Select “Confirm”                       | After step 3, screen switches to “User Registration Screen”<br>After step 5, a message pops up saying, "Login Successful. Welcome! Your address has been saved."<br>Entered details are visible upon the Personal Information Screen.<br>After step 7, a message pops up saying, “Success. Order successfully placed”                                                    |
| 4. The solution sends order details to the restaurant owners once the user places the order.                                                   | Run the program sugarbliss.py<br>From the Home screen, double-click on the logo positioned at the top of the screen<br>Click on button “2”,  “8”, “9” and “7” respectively and screen<br> Click button “Confirm”                                                                                                                                                                                                                                              | After step 2, Screen switches to Admin Screen<br>After step 3, The screen switches to Admin Dashboard after entering the correct code (“2897”)<br>After step 3, the Admin Dashboard screen displays all saved orders (order list, customer name, purchase) and statistics (most popular product, profit and revenue) including that just has been saved in previous test |
| 5. The solution allows the restaurant owner to keep track of the progress using checkboxes.                                                    | Run the program sugarbliss.py<br>From the Home screen, double-click on the logo positioned at the top of the screen<br>Click on button “2”,  “8”, “9” and “7” respectively and screen<br> Click button “Confirm”<br>Hover over the first order, click the box under the column “Progress” and choose the option “Done Cooking                                                                                                                                 | After step 5, the status of the first order is changed to “Done cooking” which is visible to the admin.                                                                                                                                                                                                                                                                  |
## Criteria C: Development

#### Techniques Used:
1. Object-Oriented Programming (OOP): Classes are used for each screen with related functions and attributes. Inheritance is also used (from Screen and MDApp)
2. Connection with Database: The program interacts with an SQLite database for storing and retrieving data
3. Interface with Dynamic updates: Based on user input and database changes, such as updating dropdowns, loading orders, and displaying data tables, the screen changes to display information accordingly
4. Event-oriented programming: Handlers like on_release, on_enter, and on_pre_enter are used to respond to user inputs and screen transitions.
5. Error handling using try-except-finally blocks

#### Development:
_**1. validate_passcode():**_
The client requires the program to have a separation between user-level and administrator-level functionality. Instead of allowing anyone to directly access the administrative interface, I decided to create the SignInSecreet screen, and this function ensures that only individuals with the correct PIN can proceed.

Instead of creating a conventional username-password system, I wanted to simplify the user experience by utilizing a PIN-entry mechanism, making it both intuitive and secure. Additionally, I make the design restrict input to an on-screen numeric keypad, minimizing the risk of keylogging and enhancing security against unauthorized access. Notably, to further improve security, only the hashed version of the PIN is stored. Hence, even if the source code or database is leaked, I ensure the original access PIN remains undiscoverable.

The process begins by retrieving the user's entered PIN (self.passcode) 
```.py
pin_is_correct = check_password("$pbkdf2-sha256$30000$8H7POcfY2/u/9x7DGOO81w$bn3RmvUVz8IsUbrE4p7lWZPtaOcpm6V0ILt16za3eUY", self.passcode)
```

Then, it compares its hash to a pre-stored hash value using the check_password function.

```.py
pwd_config = CryptContext(schemes=["pbkdf2_sha256"],
                         default = "pbkdf2_sha256",
                         pbkdf2_sha256__default_rounds = 30000)


def encrypt_password(user_password):
       return pwd_config.hash(user_password)


def check_password(hashed_password, user_password):
   return pwd_config.verify(user_password, hashed_password)


hash = encrypt_password("2897")
```

This function internally rehashes the input using the same cryptographic hashing algorithm (pbkdf2_sha256) with 30,000 iterations and compares the resulting hash against the stored hash value. 

If the two hashes match, the function comes to a conclusion that the entered PIN is correct and grants access by switching the application to the administrative screen using the app.switch_to_admin() method.
```.py
if pin_is_correct:
  	app = MDApp.get_running_app()
app.switch_to_admin()
```

Besides ensuring user-friendliness, I also want to maintain a clean and secure user experience. Hence, I make sure all characters in the input would be converted to an asterisk. 
```.py self.ids.passcode_display.text = "*" * len(self.passcode)```

In addition, it also calls out the function self.clear_passcode() to erase any visible or residual input from the PIN field. Similarly, the Clock.schedule_once method is a secondary protection used to ensure the passcode input is cleared after 1 second, regardless of whether the user proceeds or fails authentication.
```.py
def clear_passcode(self, *args):
   self.passcode = ""
   self.ids.passcode_display.text = ""


Clock.schedule_once(self.clear_passcode, 1)
```

If the PIN does not match the stored hash, the function informs the user of the failed attempt by showing an "Incorrect!" message. 

The same scheduling mechanism is applied here with Clock.schedule_once to clear the input field after a short delay,
```.py
else:
   self.ids.passcode_display.text = "Incorrect!"
   Clock.schedule_once(self.clear_passcode, 1)
```
I specifically use this method of hashed PIN validation because it provides a strong balance between security and simplicity, which aligns with the needs of the client. Hashing is a one-way cryptographic process that ensures the original PIN cannot be reversed or extracted, even if someone gains access to the source code or stored data. By hashing the PIN using the pbkdf2_sha256 algorithm with 30,000 iterations, I make it computationally expensive to brute-force or guess the PIN. So, in this case, this method allows the program to secure the PIN and validate user input without ever exposing the actual value. In other words, even if someone inspects the program or database, they will see only the hash and not the PIN itself. 

The use of salting and iteration stretching in this algorithm ensures that identical PINs result in different hashes and that attempts to crack the code would require significant computational effort. This approach ensures a secure and efficient solution for protecting administrative access, meeting the client’s requirements while adhering to best practices in cryptographic security.

_**2. populate_address_grid():**_
I designed the populate_address_grid() function because the client required a system where users could save and manage multiple sets of personal information for future use. Unlike conventional systems that assume a one-to-one relationship between users and their saved information, this solution offers flexibility by allowing users to store multiple addresses or contact details. This is particularly useful when users need to make purchases or orders for others, as it eliminates the need to repeatedly input new information for each transaction. 

The process begins by clearing any existing widgets in the address_grid layout to make sure the interface is refreshed every time new data is added.


```.py self.ids.address_grid.clear_widgets()```

It then connects to SQLite database and is told to fetch necessary information securely. The function iterates over the retrieved rows using a for loop. For each row, variables (address_id, customer_name, phone_number, and address) are unpacked and used to dynamically create a horizontal layout (MDBoxLayout) to visually represent the data and a checkbox (MDCheckbox) to allow the user to select an address.
``` .py
query = "SELECT ID, customer_name, phone_number, address FROM customer_database"
cursor.execute(query)
rows = cursor.fetchall()
connection.close()

for row in rows:
   address_id, customer_name, phone_number, address = row
   layout = MDBoxLayout(orientation="horizontal", spacing=dp(10), size_hint_y=None, height=dp(56))
```

The checkbox is grouped (using group="addresses") to ensure that only one address can be selected at a time, mimicking the behavior of radio buttons. The checkbox is also bound to the set_selected_address(). It is binded by the lambda function that dynamically passes parameters (value and a_id) to the set_selected_address method. This allows the address_id (specific to the current checkbox) to be passed along with the checkbox's active state.

checkbox = MDCheckbox(group="addresses", size_hint=(None, None), size=(dp(48), dp(48)))
checkbox.bind(active=lambda instance, value, a_id=address_id: self.set_selected_address(value, a_id))

This method allows a flexible approach to UI rendering, enabling real-time updates as new data is added or removed from the database. Requiring a smooth transition between both backend and frontend processing, this combination ensures a secure, efficient, and user-friendly solution for managing multiple sets of personal information.


**_3. add_to_cart():_**
I created this function to meet the client’s demand for a system where users could save their preferences before proceeding to checkout. By allowing users to save their preferences, this function ensures that they have the flexibility to review their selections, make adjustments if needed, and confidently proceed to checkout. Compared to conventional systems, where the ordering process is often linear and rigid, the user needs to make their decision in one sitting; hence, it makes the whole process feel rushed or incomplete. This function introduces a more dynamic and user-centered flow where users have the flexibility to review their selections, make adjustments if needed, and confidently proceed to checkout.

The process begins by checking if the selected_flavors dictionary, which holds the user’s choices, is empty. If no flavors have been selected, the function halts further execution and provides immediate feedback to the user by displaying an error message in a dialog box. This step guarantees that invalid or incomplete data does not proceed further, maintaining data integrity.
```.py
if not self.selected_flavors:
   dialog = MDDialog(
       title="Please choose at least 1 preferred flavor",
```
Then, the dictionary, which pairs product names with selected flavors, is converted into a comma-separated string using Python's join() method. The serialized data is then inserted into the SQLite database. SQL placeholders (?) are also used to prevent SQL injection, a security concern that we want to address.

```.py
con = sqlite3.connect('sugarbliss_database.db')
cursor = con.cursor()
cursor.execute("""
   INSERT INTO order_table (customer_name, product_list)
   VALUES (?, ?)
""", ("", product_list_str))
```
All of the above works are nested in a try-except-finally block as I want to minimize resource leaks or application crashes as much as possible. Specifically, while the ‘try’ block are those lines that potentially create an issue, the ’except’ block catches exceptions and return responses in a controlled way instead of letting the whole program crash completely the ‘finally’ block is used to ensure that resources are cleaned up and released, regardless of whether an error occurred or not.
```.py
try:
   con = sqlite3.connect('sugarbliss_database.db')
   cursor = con.cursor()
   cursor.execute("""
       INSERT INTO order_table (customer_name, product_list)
       VALUES (?, ?)
   """, ("", product_list_str))

   con.commit()  # Save changes to the database
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
```
In conclusion, the add_to_cart() is an exemplar of one of many bridges between the database (backend) and user interface (frontend) I use throughout the application. It also demonstrates effective error handling method that I applied for many other parts of my program, making the application resilient to potential failures and allowing for seamless user experience, even when things don't go as planned.

## Criteria D: Planning
Video Link: https://drive.google.com/file/d/1hL_YvaSnrb0M_N4ggP4SDR7T1_g3fX12/view?usp=sharing 

