import streamlit as st
from stateManagement.stateManagement import stateManagement


class snrWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        noiseSNR = st.slider("SNR", min_value=0, max_value=50)
        print(noiseSNR)
        if noiseSNR:
            state.setNoisedSignal(noiseSNR)
