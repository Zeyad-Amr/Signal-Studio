import streamlit as st
from stateManagement.stateManagement import stateManagement


class headerui:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        headerCols = st.columns([1, 5, 20, 2.5, 2.5, 1.5])

        with headerCols[1]:
            st.subheader("Sampling Studio")

        with headerCols[3]:
            saveButton = st.button('Save', key="saveBtnKey")

        with headerCols[4]:
            st.download_button(label='Export', mime='text/csv', file_name="st.session_state.fileToDownloadName" + '.csv',
                               data="st.session_state.fileToDownload", key="ExportButton")
            # TODO: Export
        # st.write("---")

        if saveButton:
            state.save_signal()