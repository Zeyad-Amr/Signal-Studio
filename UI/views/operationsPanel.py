import streamlit as st
from ui.widgets.samplingWidget import samplingWidget
from ui.widgets.snrWidget import snrWidget
from ui.widgets.graphParams import graphParams


class operationsPanel:
    def __init__(self):

        snrWidget()
        samplingWidget()
        graphParams()
