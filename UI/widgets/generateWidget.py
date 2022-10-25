import streamlit as st

from stateManagement.stateManagement import stateManagement


class generateWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        freqVal = st.number_input("Frequency (HZ)", step=0.25)
        ampVal = st.number_input("Amplitude", step=0.25)
        phaseVal = st.number_input("Phase", step=0.25)

        state.set_generated_signal(phase=phaseVal, amp=ampVal, freq=freqVal)
        # print(freqVal, " ", ampVal, " ", phaseVal)
