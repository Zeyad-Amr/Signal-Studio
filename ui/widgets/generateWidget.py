from email.policy import default
import streamlit as st

from stateManagement.stateManagement import stateManagement


class generateWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        freqVal = st.number_input("Frequency (HZ)", min_value=0.0, step=0.1, value=0.1, on_change=self.change_value)
        ampVal = st.number_input("Amplitude", min_value=0.0, step=0.25, value=1.0, on_change=self.change_value)
        phaseVal = st.number_input("Phase", step=0.5, on_change=self.change_value)

        if (st.session_state.Mode == 0):
            state.set_generated_signal(phase=phaseVal, amp=ampVal, freq=freqVal)

    def change_value(self):
        st.session_state.Mode = 0