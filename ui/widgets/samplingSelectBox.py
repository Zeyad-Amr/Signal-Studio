from ast import arg
import streamlit as st
from UI.widgets.samplingWidget import samplingWidget
from UI.widgets.sampling_with_fmax_widget import sampling_with_fmax_widget


class samplingSelectBox:
    def __init__(self):
        options = st.selectbox("Select Sampling Type", options=['Hertez', 'Max Frequency'])
        if options == 'Hertez':
            samplingWidget()
        else:
            sampling_with_fmax_widget()