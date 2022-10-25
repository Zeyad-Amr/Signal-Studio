import streamlit as st
from stateManagement.stateManagement import stateManagement


class uploadWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        uploadedSignals = st.file_uploader(
            "Upload Signal", type=["csv"], key='uploadButton', )

        if uploadedSignals is not None:
            path = state.save_file(uploadedSignals)
            state.set_uploaded_signal(path=path)
