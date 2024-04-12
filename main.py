import streamlit as st
import sqlite3
from plyer import notification

# Create or connect to a SQLite database
conn = sqlite3.connect('food_order.db')
cursor = conn.cursor()

# Create a table to store orders if it doesn't exist
query = ('''
    CREATE TABLE IF NOT EXISTS orders (
        table_no TEXT,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT,
        quantity INTEGER,
        price INTEGER
    )
''')
cursor.execute(query)
conn.commit()

# Title
st.title("Smart Ordering System")
st.sidebar.header("Select your Table")
table_no = st.sidebar.selectbox("Delivery table:", ["Table 1", "Table 2", "Table 3", "Table 4"])

st.sidebar.header("Menu")
# Define menu items
menu_items = {
    "Veg Puff": 15,
    "Egg Puff": 20,
    "Chicken Puff": 25,
    "Veg Roll": 25,
    "Chicken Roll": 25,
    "Cake piece": 15,
    "Bread Chilli": 25,
    "Cutlet": 25,
}

# Initialize cart
cart = []

# Display menu items
for item, price in menu_items.items():
    qty = st.sidebar.number_input(f"Qty {item}", min_value=0, max_value=10, value=0)
    if qty > 0:
        cart.append({"item": item, "quantity": qty, "price": price * qty})

# Show cart
st.sidebar.header("Your Cart")
for item in cart:
    st.sidebar.write(f"{item['item']} x{item['quantity']} - ₹{item['price']}")

# Calculate total price
total_price = sum(item["price"] for item in cart)

# Display total price
st.sidebar.subheader(f"Total Price: ₹{total_price}")

# Order button

# Display order details
st.write("## Order Details")
for item in cart:
    st.write(f"{item['item']} x{item['quantity']} - ₹{item['price']}")

st.write(f"**Total Price: ₹{total_price}**")

if st.sidebar.button("Place Order"):
    st.sidebar.success("Pay to confirm your order!")



# payment
st.write("## To confirm your order, choose the payment methods")
payment_method = st.selectbox("Payment Method:", ["Credit Card", "Debit Card", "UPI"])

if st.button("Confirm Order"):
    # Add the order to the database
    for item in cart:
        insert_query = "INSERT INTO orders (table_no, item, quantity, price) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_query, (table_no, item['item'], item['quantity'], item['price']))
        conn.commit()

    # Display notification for the confirmation
    notification_title = f"New Order at {table_no}"
    notification_text = f"New item added: {item['quantity']} x {item['item']}"

    # Send desktop notification
    notification.notify(
        title=notification_title,
        message=notification_text,
        app_icon=None,  # e.g., 'C:\\icon_32x32.ico'
        timeout=10,  # seconds
    )

    st.success("Your order has been confirmed")

# Close the database connection
conn.close()
