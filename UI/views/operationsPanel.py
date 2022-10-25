import streamlit as st
from ui.widgets.samplingWidget import samplingWidget
from ui.widgets.snrWidget import snrWidget


class operationsPanel:
    def __init__(self):

        samplingWidget()
        snrWidget()
