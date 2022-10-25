import streamlit as st
from stateManagement.stateManagement import stateManagement


class snrWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        noiseSNR = st.slider("SNR", min_value=0, max_value=50)
        print(noiseSNR)
        if noiseSNR:
            try:
                st.session_state.signalWithNoise = st.session_state.signalObject.add_noise(st.session_state.signal,
                                                                                           noiseSNR)

                state.draw_signal_with_noise()
            except Exception as e:
                st.error("Can't Add Noise to This Signal...")

                state.draw_empty_graph()
