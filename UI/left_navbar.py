import streamlit as st


class leftNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        st.radio("Signals", ("Signal 1", "Signal 2", "Signal 3", "Signal 4", "Signal 5", "Signal 6"))
        st.radio("Noises", ("Noise 1","Noise 2", "Noise 3","Noise 4","Noise 5","Noise 6"))
