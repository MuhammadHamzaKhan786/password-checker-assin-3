import re 
import streamlit as st

# page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")

# custom css
st.markdown("""
<style>
    .stApp {
        background: #0a192f;
    }
    
    .stMarkdown p, .stText p {
        color: white !important;
    }
    
    h1 {
        color: white !important;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .stTextInput > div > div > input {
        background-color: white;
        color: black;
        border: 2px solid #64ffda;
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
        text-align: center;
        width: 100%;
    }
    
    .stTextInput > div > div > input:focus {
        box-shadow: 0 0 5px #64ffda;
        border-color: #64ffda;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #666;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #64ffda;
        color: black;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton button:hover {
        background-color: #45b69c;
    }
    
    /* Status Messages */
    .stSuccess, .stInfo, .stError {
        color: white 
        background-color: transparent 
        border: 1px solid #64ffda 
    }
    
    .streamlit-expanderHeader {
        color: white !important;
        background-color: transparent 
        border: 1px solid #64ffda 
    }
    
    .social-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 2rem;
    }
    
    .social-links a {
        color: #64ffda;
        text-decoration: none;
        padding: 5px 15px;
        border: 1px solid #64ffda;
        border-radius: 5px;
    }
    
    .social-links a:hover {
        background-color: rgba(100, 255, 218, 0.1);
    }
    
    .footer {
        text-align: center;
        color: white;
        margin-top: 2rem;
        font-size: 14px;
    }
    
    .stTextInput label, .stTextInput .help-text {
        color: white
    }
</style>             
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password is **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase(a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number**.")

    if re.search(r"[@#$%^&*()_+={}|\\:;<>,.?/]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (@#$%^&*(),.)**.")

    if score == 4:
        st.success("✅ Password is **strong** - Your password is secure and meets all the requirements! 🎉")
    elif score == 3:
        st.info("⚠️ Password is **medium** - try to include uppercase, lowercase, numbers, and special characters! 🔨")
    else:
        st.error("❌ Password is **weak** - follow the instructions below to improve it! 🛠️")

    if feedback:
        with st.expander("🔍 **Improve your password** 📝"):
            for item in feedback:
                st.write(item)

st.title("🔐 Password Strength Generator")
st.write("Enter your password to check its strength. 🔍")

password = st.text_input(
    "Enter your password",
    type="password",
    help="Enter your password to check its strength 🔒",
    placeholder="Type your password here..."
)

if st.button("🔐 Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.error("⚠️ Please enter a password to check its strength! 🔑")

st.markdown("""
<div class="social-links">
    <a href="https://github.com/MuhammadHamzaKhan786" target="_blank">📚 GitHub</a>
    <a href="https://www.linkedin.com/in/muhammad-hamza-khan-6234772bb/" target="_blank">💼 LinkedIn</a>
    <a href="https://personal-portfolio-hamza.vercel.app/" target="_blank">🌐 Portfolio</a>
</div>
<div class="footer">
    Developed with ❤️ by Muhammad Hamza Khan
</div>
""", unsafe_allow_html=True)
        

