from ast import arg
import streamlit as st
from ui.widgets.samplingWidget import samplingWidget
from ui.widgets.sampling_with_fmax_widget import sampling_with_fmax_widget


class samplingSelectBox:
    def __init__(self):
        options = st.selectbox("Select Sampling Type", options=['Hertez', 'Max Frequency'])
        if options == 'Hertez':
            samplingWidget()
        else:
            sampling_with_fmax_widget()