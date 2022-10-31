from ui.widgets.generateWidget import generateWidget
from ui.widgets.signalsListWidget import signalsListWidget
import streamlit as st


class signalsPanel:
    def __init__(self):

        # Generate Signal Panel Title

        st.write("Generate Signal")
        st.write("---")

        # Calling Generate Widget
        generateWidget()

        #  Signal Panel Title
        st.write("Signals")
        st.write("---")

        # Calling SignalList Widget
        signalsListWidget()
