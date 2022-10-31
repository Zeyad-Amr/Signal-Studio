import streamlit as st
from ui.widgets.samplingWidget import samplingWidget
from ui.widgets.snrWidget import snrWidget
from ui.widgets.graphParams import graphParams
from ui.widgets.uploadWidget import uploadWidget
from ui.widgets.sampling_with_fmax_widget import sampling_with_fmax_widget


class operationsPanel:
    def __init__(self):

        # Upload Signal Panel Title

        st.write("Upload Signal")

        st.write("---")

        # Calling Upload Widget

        uploadWidget()

        st.write("---")

        # Calling Sanpling Widget

        samplingWidget()

        # Calling Sanpling with Fmax Widget

        sampling_with_fmax_widget()

        # Calling SNR Widget

        snrWidget()

        # Calling Graph Params Widget

        graphParams()
