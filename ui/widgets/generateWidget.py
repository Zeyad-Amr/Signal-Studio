from email.policy import default
import streamlit as st

from stateManagement.stateManagement import stateManagement


class generateWidget:
    def __init__(self):

        # stateManagement
        self.state = stateManagement()

        self.freqVal = st.number_input("Frequency (HZ)", min_value=0.0, step=1.0, value=1.0, on_change=self.change_value)
        self.ampVal = st.number_input("Amplitude", min_value=0.0, step=0.25, value=1.0, on_change=self.change_value)
        self.phaseVal = st.number_input("Phase", step=0.5, on_change=self.change_value)
            

    def change_value(self):
        st.session_state.Mode = 0
        self.state.set_generated_signal(phase=self.phaseVal, amp=self.ampVal, freq=self.freqVal)