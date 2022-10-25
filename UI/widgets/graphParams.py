import streamlit as st


class graphParams:
    def __init__(self):

        signalButton = st.checkbox("Signal", value=True)
        sampleButton = st.checkbox("Sampling", value=True)
        reconstructedButton = st.checkbox("Reconstruction", value=True)

        st.session_state.signalView = signalButton
        st.session_state.sampleView = sampleButton
        st.session_state.reconstructedview = reconstructedButton
