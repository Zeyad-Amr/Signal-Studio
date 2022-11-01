import streamlit as st
from ui.widgets.snrWidget import snrWidget
from ui.widgets.graphParams import graphParams
from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.samplingSelectBox import samplingSelectBox


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
