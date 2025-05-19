This is a GUI-based Restaurant Billing System built with Python using Tkinter. It provides a smooth, user-friendly interface for creating customer bills with support for itemized ordering, automatic VAT and discount calculations, and saving receipts.

🚀 Features
Object-Oriented Programming (OOP) architecture

Menu item and order management

Subtotal, discount, VAT, and final total calculation

GUI built with Tkinter

Real-time error handling for invalid inputs

Save bill as a .txt file

Random reference number generation for each bill

Predefined menu with dynamic quantity entry

🧠 Tech Stack
Language: Python 3

GUI Library: Tkinter (standard Python GUI package)

📦 Menu Items (default)
Item	Price (Tk)
Chicken Burger	160
Beef Burger	180
French Fries	80
Soft Drink	20

🖼️ GUI Overview
Left Panel: Input area for quantities, VAT, and discount

Right Panel: Bill display area

Buttons:

Generate Bill: Creates a detailed bill

Save Bill: Saves the generated bill to a text file

🧩 Project Structure
MenuItem: Represents a single menu item

OrderItem: Wraps a MenuItem with a quantity and cost

Order: Holds multiple OrderItems and computes the subtotal

Bill: Calculates total amount after applying VAT and discounts

BillingSystemGUI: Manages all GUI components and user interactions

⚙️ How to Run
Ensure Python 3 is installed.

Run the script:

bash
Copy
Edit
python restaurant.py
The GUI will open. Input order quantities, VAT, and discount values.

Click Generate Bill to view.

Click Save Bill to export as .txt.

❗ Validations
Quantity cannot be negative

VAT and Discount must be numerical

Alerts shown for incorrect inputs

📂 Saving Bills
Bills can be saved using a file dialog

File format: .txt

Includes itemized list, VAT, discount, and total

✍️ Author
Developed by [Your Name Here]. Contributions welcome.

📄 License
This project is open-source. Use it freely or customize it to fit your own restaurant system.

