import streamlit as st
from ui.widgets.samplingWidget import samplingWidget
from ui.widgets.snrWidget import snrWidget
from ui.widgets.graphParams import graphParams
from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.sampling_with_fmax_widget import sampling_with_fmax_widget



class operationsPanel:
    def __init__(self):
        snrWidget()
        samplingWidget()
        sampling_with_fmax_widget()
        graphParams()
