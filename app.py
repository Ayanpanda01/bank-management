# app.py
import streamlit as st
from Main import Bank

Bank.load_data()
st.title("🏦 Simple Banking System")

menu = st.sidebar.selectbox("Choose an action", [
    "Create Account", "Deposit", "Withdraw", "Show Details", "Update Details", "Delete Account"
])

if menu == "Create Account":
    st.header("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")
    if st.button("Create"):
        info = Bank.create_account(name, age, email, pin)
        if info:
            st.success("Account created successfully!")
            st.write(info)
        else:
            st.error("Failed to create account. Must be 18+ and PIN must be 4 digits.")

elif menu == "Deposit":
    st.header("Deposit Money")
    acNo = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)
    if st.button("Deposit"):
        balance = Bank.deposit(acNo, pin, amount)
        if balance is not None:
            st.success(f"Deposited successfully! New balance: ₹{balance}")
        else:
            st.error("Invalid credentials or amount.")

elif menu == "Withdraw":
    st.header("Withdraw Money")
    acNo = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=0)
    if st.button("Withdraw"):
        balance = Bank.debit(acNo, pin, amount)
        if balance is not None:
            st.success(f"Withdrawn successfully! New balance: ₹{balance}")
        else:
            st.error("Invalid credentials or insufficient balance.")

elif menu == "Show Details":
    st.header("Account Details")
    acNo = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    if st.button("Show"):
        user = Bank.find_user(acNo, pin)
        if user:
            st.json(user)
        else:
            st.error("Invalid account number or PIN.")

elif menu == "Update Details":
    st.header("Update Account Info")
    acNo = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    field = st.selectbox("Field to update", ["email", "pin"])
    new_value = st.text_input(f"New {field}")
    if st.button("Update"):
        success = Bank.update_details(acNo, pin, field, new_value)
        if success:
            st.success("Details updated successfully.")
        else:
            st.error("Update failed. Check credentials and field.")

elif menu == "Delete Account":
    st.header("Delete Account")
    acNo = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    if st.button("Delete"):
        success = Bank.delete_account(acNo, pin)
        if success:
            st.success("Account deleted successfully.")
        else:
            st.error("Invalid account number or PIN.")