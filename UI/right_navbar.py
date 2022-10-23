import streamlit as st
from asyncio.windows_events import NULL
import pandas as pd
import time


class rightNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        if "sampling_slider" not in st.session_state:
            st.session_state["sampling_slider"] = 0

        if "SNR_slider" not in st.session_state:
            st.session_state["SNR_slider"] = 0

        # sampling
        with st.container():
            slider_val = st.slider(
                "Sampling", key="sampling_slider", min_value=0, max_value=150)
            if slider_val:
                try:
                    if slider_val != 0:
                        st.session_state.sampledSignal = st.session_state.signalObject.sample_signal(
                            st.session_state.signal, slider_val)
                        st.session_state.graphWidget.draw_sampled_signal()
                        st.session_state["SNR_slider"] = 0

                    else:
                        st.error("Sample Rate Can't be 0 ...")
                except:
                    st.session_state.graphWidget.error_occur()
                    st.error(
                        "Error Occur in sampling, please check and try again...")

            reconstructButton = st.button("Reconstruct")
            if reconstructButton:
                try:
                    if 'sampledSignal' in st.session_state:
                        st.session_state["SNR_slider"] = 0
                        if st.session_state.sampledSignal.empty:
                            st.error("Nothing to reconstruct this signal...")
                            st.session_state.graphWidget.error_occur()
                        else:
                            st.session_state.signal = st.session_state.signalObject.reconstruct_signal(
                                st.session_state.sampledSignal)
                            st.session_state.leftNav.add_button({
                                'name': 'Reconstructed Signal {}'.format(st.session_state.recCounter),
                                'signal': st.session_state.signal
                            })
                            st.session_state.recCounter += 1
                            st.session_state.graphWidget.draw_signal()
                except:
                    st.error("Can't Reconstruct this signal...")
                    st.session_state.graphWidget.error_occur()

        # add noise
        st.write("---")
        st.write("Add Noise")
        noiseSNR = st.slider("SNR", key="SNR_slider",
                             min_value=0, max_value=50)
        if noiseSNR != 0:
            st.session_state["sampling_slider"] = 0
        if noiseSNR:
            try:
                st.session_state.signalWithNoise = st.session_state.signalObject.add_noise(st.session_state.siganl,
                                                                                           noiseSNR)
                st.session_state.graphWidget.draw_signal_with_noise()

            except Exception as e:
                st.error("Can't Add Noise to This Signal...")
                st.session_state.graphWidget.error_occur()

        # add signals
        with st.container():
            st.write("---")
            st.write("Add Signals")
            selectedSignals = []
            for signal in st.session_state.generatedSignals:
                checkboxVal = st.checkbox(signal['name'], key=signal['name'])
                if checkboxVal:
                    selectedSignals.append(signal['signal'])

        addSingalBtn = st.button("Add")
        if addSingalBtn:
            try:
                if len(selectedSignals) == 0:
                    st.error("Nothing to add...")
                    st.session_state.graphWidget.error_occur()
                else:
                    firstSignal = selectedSignals[0]
                    for i in selectedSignals[1:]:
                        firstSignal = st.session_state.signalObject.add_signals(
                            firstSignal, i)

                    # st.session_state.signal = firstSignal
                    sObject = {
                        'name': 'Mixture Signal {}'.format(st.session_state.mixCounter),
                        'signal': firstSignal
                    }
                    st.session_state.leftNav.add_button(sObject)
                    # st.session_state.generatedSignals.append(sObject)
                    st.session_state.mixCounter += 1
                    st.session_state.graphWidget.draw_signal()

            except:
                st.error("Can't Add These Signals...")
                st.session_state.graphWidget.error_occur()
