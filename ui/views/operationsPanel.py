import streamlit as st
from UI.widgets.snrWidget import snrWidget
from UI.widgets.graphParams import graphParams
from UI.widgets.uploadWidget import uploadWidget
from UI.widgets.samplingSelectBox import samplingSelectBox


class operationsPanel:
    def __init__(self):

        # Upload Signal Panel Title

        st.write("Upload Signal")

        st.write("---")

        # Calling Upload Widget

        uploadWidget()

        st.write("---")

        samplingSelectBox()

        st.write("---")

        # Calling SNR Widget

        snrWidget()

        # Calling Graph Params Widget

        graphParams()
