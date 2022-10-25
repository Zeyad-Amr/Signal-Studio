import streamlit as st
from stateManagement.stateManagement import stateManagement


class signalsListWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        self.signalsLst = []
        for signal in st.session_state.signals:
            self.signalsLst.append(signal['name'])

        st.radio("dd", self.signalsLst, key="selectedSignal")

        # if st.session_state.selectedSignal:
        #     state.on_change()
