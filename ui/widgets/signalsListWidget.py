import streamlit as st
from stateManagement.stateManagement import stateManagement


class signalsListWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()
        
        selectedSignals = []
        signalsList = []

        for signal in st.session_state.signalsList:
            signalsList.append(signal['name'])

        options = st.multiselect("Signals", options=(signalsList))

        if(len(options) > 0):
            for name in options:
                for signal in st.session_state.signalsList:
                    if(name == signal['name']):
                        selectedSignals.append(signal)
        st.session_state.selectedSignals = selectedSignals

        if len(selectedSignals) > 0:
            st.session_state.Mode = 2

        if st.session_state.Mode == 2:
            state.set_add_signals()

        if len(st.session_state.signalsList):
            deleteBtn = st.button("Delete")
            if deleteBtn:
                st.session_state.Mode = 0
                state.delete_signals(selectedSignals)
