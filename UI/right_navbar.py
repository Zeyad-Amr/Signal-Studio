import streamlit as st


class rightNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        with st.form("sampling_form"):
            slider_val = st.slider("Sampling")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Reconstruct")
            if submitted:
                st.success("Reconstructed Successfully")

        

