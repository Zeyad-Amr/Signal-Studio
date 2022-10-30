import streamlit as st
from stateManagement.stateManagement import stateManagement


class sampling_with_fmax_widget:
    def __init__(self):

        # stateManagement
        self.state = stateManagement()

        self.sampling_val = st.slider(
            "Sampling with Max Frequency", key="sampling_slider_with_fmax", min_value=0.25, max_value=5.0, value=2.0, step=0.25, on_change=self.change_value)

        if st.session_state.SamplingMode == 1:
            self.state.set_sampled_signal(sampleRate=self.sampling_val, max_freq = True)
            self.state.set_reconstructed_signal()
    
    def change_value(self):
        st.session_state.SamplingMode = 1
    

