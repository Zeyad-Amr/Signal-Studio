import streamlit as st
from stateManagement.stateManagement import stateManagement


class headerui:
    def __init__(self):

        # stateManagement
        state = stateManagement()

        headerCols = st.columns([1, 5, 2.5, 2.5, 2.5, 8, 2, 2.5, 3])

        if 'sideNav' not in st.session_state:
            st.session_state['sideNav'] = 0
        with headerCols[1]:
            st.subheader("Sampling Studio")
        # with headerCols[2]:
        #     st.button('Sampling', key="SamplingButton")

        # with headerCols[3]:
        #     st.button('Add Noise', key="AddNoiseButton")

        # with headerCols[4]:
        #     st.button('Add Signal', key="AddSignalButton")

        # with headerCols[7]:
        #     st.button('Delete', key="deleteSignalsButton")

        with headerCols[8]:
            # st.button('Export', key="ExportButton")
            st.download_button(label='Export', mime='text/csv', file_name=st.session_state.fileToDownloadName + '.csv',
                               data=st.session_state.fileToDownload, key="ExportButton")
        # st.write("---")
