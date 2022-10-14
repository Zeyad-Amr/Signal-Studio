import streamlit as st

class AppUi:
    def __init__(self):
        st.set_page_config(page_title='Sampling Studio')
        st.title("Coming Soon...")

        # Removing Streamlit hamburger and footer.
        st.markdown("""
        <style>
            .css-9s5bis.edgvbvh3 {
                visibility : hidden;
            }
            .css-1q1n0ol.egzxvld0 {
                visibility : hidden;
            }
        </style>
        """, unsafe_allow_html=True)