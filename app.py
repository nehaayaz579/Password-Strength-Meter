import streamlit as st
import string
import random

# Function to generate a random strong password
def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(12))  # 12 character length
    return password

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check if the password contains both uppercase and lowercase letters
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Check if the password contains a digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check if the password contains a special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")

    # Check if the password is not common (blacklist)
    common_passwords = ["password123", "123456", "qwerty", "letmein", "welcome", "12345", "password"]
    if password.lower() in common_passwords:
        score = 1  # Reset score to weak if it's a common password
        feedback.append("Password is too common. Try a unique password.")

    # Determine password strength
    if score == 4:
        return "Strong", feedback
    elif score == 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# Streamlit UI setup
st.title("🔐 Password Strength Meter")

# Input for the password
password = st.text_input("Enter a password to check its strength:")

# Button to check the password strength
if password:
    strength, feedback = check_password_strength(password)

    # Display results
    st.subheader(f"Password Strength: {strength}")
    for f in feedback:
        st.write(f"- {f}")

    # Suggest improvements if weak
    if strength == "Weak":
        st.write("Here are some suggestions to make your password stronger:")
        st.write("- Use at least 8 characters.")
        st.write("- Include both uppercase and lowercase letters.")
        st.write("- Add a digit (0-9).")
        st.write("- Include a special character (!@#$%^&*).")

    # Add an option to generate a strong password
    if strength == "Weak" or strength == "Moderate":
        if st.button("Generate a Strong Password"):
            strong_password = generate_password()
            st.subheader("Suggested Strong Password:")
            st.text(strong_password)

# Display instructions
st.sidebar.title("📋 Instructions")
st.sidebar.write("""
**🔐Password Strength Criteria:**
1. 🔢 At least 8 characters long.
2. 🔢 Contains both uppercase & lowercase letters.
3. 🔢 Contains at least one digit (0-9).
4. ✨ Contains at least one special character (!@#$%^&*).

**⚖️ Scoring System:**
- ❌ Weak: Score 1-2 → Short or missing key elements.
- ⚖️ Moderate: Score 3-4 → Missing some security features.
- 💪 Strong: Score 5 → Meets all criteria.

**💡Additional Features:**
- 🔑 Password generator to suggest strong passwords.
- 🚫 Blacklist of common passwords to reject weak ones.

""")
