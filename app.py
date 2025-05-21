import streamlit as st
import sqlite3
import hashlib

#🔹 Professional Streamlit UI
#🚀 Enhancing the Login & Registration UI

st.set_page_config(page_title="MediSync - Smart Healthcare", page_icon="🩺", layout="wide")

# Sidebar Navigation

st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Home", "Register", "Login"])

if menu == "Home":
    st.title("🚀 Welcome to MediSync - Intelligent Healthcare!")
    st.image("https://via.placeholder.com/600", caption="AI-Powered Patient Management")
    
    st.button("🔹 **Book Appointments** ")
    st.write("Redirecting to appointment booking...")

    st.button("🔹 **AI Health Insights** ")
    
    st.button("🔹 **Secure Payments** ")
    st.write("Redirecting to payment processing...")

elif menu == "Register":
    st.title("📝 Register for MediSync")
    st.text_input("Enter your name")
    st.text_input("Enter email")
    st.button("Submit")
    
elif menu == "Login":
    st.title("🔐 Login to MediSync")
    st.text_input("Username")
    st.text_input("Password", type="password")
    st.button("Login")

#🔹 Updating User Registration & Login
#🔹 Database Schema for Authentication

conn = sqlite3.connect("medisync.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()
conn.close()     

#🔹 Register User with SHA512 Secure it

def register_user(name, email, password):
    conn = sqlite3.connect("medisync.db")
    cursor = conn.cursor()

    hashed_pw = hash_password(password)
    cursor.execute("INSERT INTO Users (name, email, password) VALUES (?, ?, ?)", (name, email, hashed_pw))

    conn.commit()
    conn.close()
    return "User Registered Successfully!"

#🔹 Secure Login System
   
def login_user(email, password):
    conn = sqlite3.connect("medisync.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM Users WHERE email = ?", (email,))
    user_record = cursor.fetchone()

    conn.close()

    if user_record and verify_password(password, user_record[0]):
        return "✅ Login Successful!"
    return "❌ Incorrect Email or Password."


#🚀 Secure Authentication with SHA512
#🔹 Implementing SHA512 Hashin


def hash_password(password):
    """Securely hash the password using SHA512."""
    return hashlib.sha512(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    """Verify if the input password matches the stored hashed password."""
    return hash_password(password) == hashed_password