import streamlit as st
from stateManagement.stateManagement import stateManagement


class snrWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        noiseSNR = st.slider("SNR", min_value=1, max_value=100, value=100)

        state.set_noised_signal((noiseSNR*0.5)**(noiseSNR*0.025))
