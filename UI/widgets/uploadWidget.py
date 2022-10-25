import streamlit as st
from stateManagement.stateManagement import stateManagement


class uploadWidget:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        uploadedSignals = st.file_uploader(
            "Upload Signal", type=["csv"], key='uploadButton', accept_multiple_files=True)

        # submitted = st.form_submit_button("Upload")

        # if submitted and uploadedSignals is not None:
        #     for signal in uploadedSignals:
        #         try:
        #             path = state.save_file(signal)
        #             siganlDict = st.session_state.signalObject.reading_signal(
        #                 path)
        #             st.session_state.signal = siganlDict['signal']

        #             state.draw_signal()
        #             state.add_signal(siganlDict)
        #         except:
        #             st.error("Error Occur with importing of signal...")
