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
### UML Diagram
### ER Diagram
### Flow Diagram
### Database Picture
### Record of Task:
### Test Plan:
