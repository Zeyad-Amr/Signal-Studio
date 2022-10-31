import streamlit as st


class graphParams:
    def __init__(self):

        #  view Signal Switch
        signalButton = st.checkbox("Signal", value=True)

        #  view Sampling Switch
        sampleButton = st.checkbox("Sampling", value=True)

        #  view Reconstructed Signal Switch
        reconstructedButton = st.checkbox("Reconstruction", value=True)

        # setting values to state
        st.session_state.signalView = signalButton
        st.session_state.sampleView = sampleButton
        st.session_state.reconstructedview = reconstructedButton
