Smart Ordering System

Database Setup:
It creates or connects to a SQLite database named 'food_order.db'.
Defines a table named 'orders' to store order details such as table number, item, quantity, and price.

User Interface:
Displays a title "Smart Ordering System".
Provides a sidebar for users to select their table and order items from the menu.
The menu items and their respective prices are displayed, and users can input the quantity of each item they want to order.
Shows the cart with selected items and their prices.
Calculates and displays the total price of the order.

Order Placement:
Provides a button to place the order.
Upon placing the order, it adds the order details to the database.
Sends a desktop notification about the new order.
Displays a success message confirming the order.

Payment Confirmation:
Allows users to select a payment method (Credit Card, Debit Card, or UPI).
Provides a button to confirm the order.

Database Management:
Closes the database connection after order confirmation.

"Smart Ordering System" is a Streamlit-based application enabling users to select menu items, place orders, and confirm payments.
It utilizes SQLite for order storage and Plyer for desktop notifications, streamlining the ordering process for efficiency and convenience.
