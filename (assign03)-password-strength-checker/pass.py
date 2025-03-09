import streamlit as st
import re

st.set_page_config(page_title="🔒 Password Strength Analyzer", page_icon="🔐")

st.title("🔐 Password Strength Analyzer")
st.markdown("""
## Welcome to the Password Strength Analyzer! 🛡️
Ensure your password is **secure** and **strong** using this tool.
We'll provide **valuable insights** to enhance your password security. 🔑
""")

password = st.text_input("🔑 Enter your password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("⚠️ Your password should be at least **8 characters long**.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔠 Include **both uppercase and lowercase** letters for better security.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔢 Add at least **one number** to strengthen your password.")

    if re.search(r'[!@#$%&*]', password):
        score += 1
    else:
        feedback.append("🔣 Use at least **one special character** (!@#$%&*) to enhance security.")

    if score == 4:
        feedback.append("✅ **Strong Password!** Great job! 🎉")
    elif score == 3:
        feedback.append("⚠️ **Moderate Strength.** Consider making it stronger for better security.")
    else:
        feedback.append("❌ **Weak Password!** Your password is vulnerable. Please improve it.")

    st.markdown("## 🔍 Password Analysis")
    for tip in feedback:
        st.write(tip)

else:
    st.info("🔎 Enter your password above to analyze its strength.")
