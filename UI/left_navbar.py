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

        with st.form("signals"):
            submitted = st.form_submit_button("Add")
            if submitted:
                # TO-DO add signals
                print('Add checked signals')

            st.checkbox("Signal 1")
            st.checkbox("Signal 2")
            st.checkbox("Signal 3")
            st.checkbox("Signal 4")
            st.checkbox("Signal 5")
            st.checkbox("Signal 6")
            st.checkbox("Signal 7")
            st.checkbox("Signal 8")


