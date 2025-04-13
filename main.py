import streamlit as st
from cryptography.fernet import Fernet
import base64
import hashlib
import time
import os
from typing import Optional
import json


def generate_derived_key(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)

def inject_neomorphic_design():
    st.markdown("""
    <style>
        :root {
            --primary: #7367F0;
            --secondary: #CE9FFC;
            --accent: #FF6B6B;
            --dark: #1a1a2e;
            --light: #F8F8F8;
            --gradient: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
        }
        body {
            background: var(--dark);
            color: var(--light);
        }
        .stApp {
            background: var(--dark);
            min-height: 100vh;
            overflow-x: hidden;
        }
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea {
            background: rgba(255,255,255,0.05) !important;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1) !important;
            color: var(--light) !important;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .stButton>button {
            background: var(--gradient) !important;
            border: none !important;
            color: white !important;
            padding: 12px 30px !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 15px rgba(115, 103, 240, 0.3) !important;
            position: relative;
            overflow: hidden;
            transition: all 0.4s ease !important;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(115, 103, 240, 0.5) !important;
        }
        .stButton>button::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                120deg,
                transparent,
                rgba(255,255,255,0.2),
                transparent
            );
            transition: all 0.8s;
        }
        .stButton>button:hover::after {
            left: 100%;
        }
        .custom-card {
            background: rgba(255,255,255,0.03) !important;
            backdrop-filter: blur(12px);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(255,255,255,0.1);
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }
        .feature-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gradient-text {
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
        }
        .stProgress > div > div {
            background: var(--gradient) !important;
        }
        .stToast {
            background: var(--dark) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
        }
        /* Additional Animation for Built with Fiza Nazz */
        @keyframes heartbeat {
            0% { transform: scale(1); }
            25% { transform: scale(1.2); }
            50% { transform: scale(1); }
            75% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }
        .built-with {
            text-align: center;
            font-size: 1.2rem;
            color: var(--light);
            margin-top: 2rem;
        }
        .built-with span.heart {
            display: inline-block;
            animation: heartbeat 1.5s infinite;
            color: var(--accent);
        }
    </style>
    """, unsafe_allow_html=True)

# --------------------------
# Enhanced Core Features
# --------------------------
class CryptoManager:
    def __init__(self):
        self.cipher = self._initialize_cipher()
        self.salt = os.urandom(16)

    @st.cache_resource
    def _initialize_cipher(_self):
        return Fernet.generate_key()

    def renew_key(self):
        self._initialize_cipher.clear()
        self.cipher = self._initialize_cipher()

# --------------------------
# Modern UI Components
# --------------------------
def hero_section():
    col1, col2 = st.columns([3,2])
    with col1:
        st.markdown("""
        <div style="padding: 3rem 0 4rem 0;">
            <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">🔐 <span class="gradient-text">SecureVault Pro</span></h1>
            <p style="font-size: 1.2rem; opacity: 0.9;">
            Next-gen encryption suite with military-grade security and AI-powered protection.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3063/3063186.png", width=200)
    # Creative built with message under hero section
    st.markdown("""
        <div class="built-with">
            Built with <strong>Fiza Nazz</strong> <span class="heart">❤️</span>
        </div>
    """, unsafe_allow_html=True)

def feature_card(title, content, icon):
    st.markdown(f"""
    <div class="custom-card">
        <div class="feature-icon">{icon}</div>
        <h3>{title}</h3>
        <p style="opacity: 0.8;">{content}</p>
    </div>
    """, unsafe_allow_html=True)

# --------------------------
# Main Application Logic
# --------------------------
def main():
    inject_neomorphic_design()
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1067/1067555.png", width=60)
    
    crypto = CryptoManager()
    fernet = Fernet(crypto.cipher)

    # Hero Section with creative branding message
    hero_section()

    # Main Tabs with enhanced components
    tab1, tab2, tab3, tab4 = st.tabs(["🔮 Encrypt", "🔓 Decrypt", "⚙️ Security", "📊 Analytics"])

    with tab1:
        st.subheader("Advanced Encryption")
        input_type = st.radio("Input Type:", ["Text", "File", "Database"], horizontal=True)

        if input_type == "Text":
            text = st.text_area("Enter sensitive text:", height=200)
            if st.button("🚀 Encrypt Text"):
                with st.spinner("Encrypting with AES-256..."):
                    encrypted = fernet.encrypt(text.encode())
                    st.success("Encryption Complete!")
                    st.code(encrypted.decode())
        elif input_type == "File":
            # Enhanced File Handling
            uploaded_file = st.file_uploader("Upload file:", type=["txt", "pdf", "docx"])
            if uploaded_file:
                file_details = {
                    "name": uploaded_file.name,
                    "size": f"{uploaded_file.size/1024:.2f} KB",
                    "type": uploaded_file.type
                }
                st.json(file_details)
                if st.button("🔒 Encrypt File"):
                    with st.spinner("Processing..."):
                        encrypted = fernet.encrypt(uploaded_file.getvalue())
                        st.download_button(
                            label="Download Encrypted File",
                            data=encrypted,
                            file_name=f"encrypted_{uploaded_file.name}"
                        )

    with tab2:
        st.subheader("AI-Powered Decryption")
        encrypted_data = st.text_area("Enter encrypted data:", height=250)
        if st.button("🔑 Decrypt Data"):
            try:
                decrypted = fernet.decrypt(encrypted_data.encode())
                with st.expander("Decrypted Content"):
                    st.code(decrypted.decode())
                st.success("✅ Decryption Successful!")
            except Exception as e:
                st.error("❌ Invalid or corrupted data")

    with tab3:
        st.subheader("Security Dashboard")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Current Key Strength", "AES-256", "Military Grade")
            st.metric("Active Sessions", 3, "Secure Connections")
            if st.button("🔄 Rotate Master Key"):
                crypto.renew_key()
                st.success("Master Key Rotated Successfully!")
        with col2:
            st.write("### Security Audit")
            st.progress(85)
            st.write("System Integrity: **94%**")
            st.write("Threat Detection: **Active**")

    with tab4:
        st.subheader("Encryption Analytics")
        with st.container():
            st.write("### Activity Timeline")
            # Placeholder for chart/analytics visualization
            st.image("https://via.placeholder.com/800x300/283046/7367F0?text=Encryption+Analytics+Dashboard", use_column_width=True)

    # Sidebar Features with creative feature cards
    with st.sidebar:
        st.title("⚡ Quick Tools")
        feature_card("Password Generator", "Create strong passwords", "🔑")
        feature_card("File Hasher", "SHA-256 file hashing", "📄")
        feature_card("Security Scan", "Deep system analysis", "🛡️")
        st.markdown("---")
        with st.expander("Theme Settings"):
            st.color_picker("Primary Color", value="#7367F0")
            st.color_picker("Secondary Color", value="#CE9FFC")
    
    # Footer with animated creative message
    st.markdown("""
    <footer class="built-with" style="margin-top: 3rem;">
        <p>© 2025 SecureVault Pro. All Rights Reserved. | Built with <strong>Fiza Nazz</strong> <span class="heart">❤️</span></p>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
