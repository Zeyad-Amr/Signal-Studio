import streamlit as st

from stateManagement.stateManagement import stateManagement


class generateWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        freqVal = st.number_input("Frequency (HZ)", step=0.25, on_change=self.change_value)
        ampVal = st.number_input("Amplitude", step=0.25, on_change=self.change_value)
        phaseVal = st.number_input("Phase", step=0.25, on_change=self.change_value)

        if (st.session_state.isGenerateMode == True):
            state.set_generated_signal(phase=phaseVal, amp=ampVal, freq=freqVal)

    def change_value(self):
        st.session_state.isGenerateMode = True