import streamlit as st
from UI.widgets.samplingWidget import samplingWidget
from UI.widgets.snrWidget import snrWidget
from UI.widgets.graphParams import graphParams


class operationsPanel:
    def __init__(self):

        snrWidget()
        samplingWidget()
        graphParams()
