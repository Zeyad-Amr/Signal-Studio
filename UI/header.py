import streamlit as st


def on_click_btn(operation):
    print(f'Button Clicked to {operation}')


class headerUI:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        # Removing Streamlit hamburger and footer.
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        headerCols = st.columns([2, 2, 2, 2, 2, 10, 1, 2])

        with headerCols[1]:
            st.button('Add Signal', on_click=on_click_btn('add_signal'))
        with headerCols[2]:
            st.button('Add Noise', on_click=on_click_btn('add_noise'))
        with headerCols[3]:
            st.button('Sampling', on_click=on_click_btn('sampling'))
        with headerCols[4]:
            st.button('Clear', on_click=on_click_btn('clear'))
        with headerCols[6]:
            st.button('Export', on_click=on_click_btn('export'))
