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

        # sampling
        with st.container():
            slider_val = st.slider("Sampling")
            if slider_val:
                print(slider_val)
            st.button("Reconstruct", on_click=self.on_clicked)

        # add noise
        st.write("Add Noise")
        noiseSNR = st.slider("SNR")
        if noiseSNR:
            # TODO: SNR change function
            print("SNR change function: ", noiseSNR)

    def on_clicked(self):
        print("Clicked")
