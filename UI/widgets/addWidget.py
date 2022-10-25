import streamlit as st
from stateManagement.stateManagement import stateManagement


class addWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        selectedSignals = []
        for signal in st.session_state.signalsList:
            checkboxVal = st.checkbox(
                signal['name'], key=signal['name'])
            if checkboxVal:
                selectedSignals.append(signal)

        st.session_state.selectedSignals = selectedSignals

        if len(selectedSignals) == 0:
            st.session_state.Mode = 0
        else:
            st.session_state.Mode = 2

        if st.session_state.Mode == 2:
            state.set_add_signals()
            # if addSingalBtn:
            #     try:
            #         if len(selectedSignals) == 0:
            #             st.error("Nothing to add...")

            #             state.draw_empty_graph()
            #         else:
            #             firstSignal = selectedSignals[0]
            #             for i in selectedSignals[1:]:
            #                 firstSignal = st.session_state.signalObject.add_signals(
            #                     firstSignal, i)

            #             sObject = {
            #                 'name': 'Mixture Signal {}'.format(st.session_state.mixCounter),
            #                 'signal': firstSignal
            #             }

            #             st.session_state.signalsPanel.add_signal(sObject)
            #             st.session_state.generatedSignals.append(sObject)
            #             st.session_state.mixCounter += 1

            #             state.draw_signal()
            #     except:
            #         st.error("Can't Add These Signals...")
            #         state.draw_empty_graph()
            #     st.experimental_rerun()
