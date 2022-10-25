import streamlit as st

from stateManagement.stateManagement import stateManagement


class generateWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        with st.form("generate_signal", clear_on_submit=True):
            freqVal = st.number_input("Frequency (HZ)", step=0.25)
            ampVal = st.number_input("Amplitude", step=0.25)
            phaseVal = st.number_input("Phase", step=0.25)

            submitted = st.form_submit_button("Generate")
            if submitted:
                try:
                    siganlObject = st.session_state.signalObject.generate_signal(
                        ampVal, freqVal, phaseVal)
                    sObject = {
                        "name": "Untitled {}".format(st.session_state.signalCounter),
                        "signal": siganlObject
                    }
                    state.add_signal(sObject)
                    st.session_state.generatedSignals.append(
                        sObject)
                    st.session_state.signalCounter += 1
                    st.success("Generated Successfully")
                except:
                    st.error(
                        "Can't Generate Signal with these values...")
