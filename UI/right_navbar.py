import streamlit as st


class rightNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)
        if 'recCounter' not in st.session_state:
            st.session_state.recCounter = 0

        # sampling
        with st.container():
            slider_val = st.slider("Sampling")
            if slider_val:
                try:
                    if slider_val != 0:
                        st.session_state.sampledSignal = st.session_state.signalObject.sample_signal(
                            st.session_state.signal, slider_val)
                        st.session_state.graphWidget.draw_sampled_signal()
                    else:
                        st.error("Sample Rate Can't be 0 ...")
                except:
                    st.session_state.graphWidget.error_occur()
                    st.error("Error Occur in sampling, please check and try again...")

            reconstructButton = st.button("Reconstruct")
            if reconstructButton:
                if 'sampledSignal' in st.session_state:
                    st.session_state.signal = st.session_state.signalObject.reconstruct_signal(
                        st.session_state.sampledSignal)
                    st.session_state.leftNav.add_button({
                        'name': 'Reconstructed Signal {}'.format(st.session_state.recCounter),
                        'signal': st.session_state.signal
                    })
                    st.session_state.recCounter += 1
                    st.session_state.graphWidget.draw_signal()

        # add noise
        st.write("---")
        st.write("Add Noise")
        noiseSNR = st.slider("SNR")
        if noiseSNR:
            st.session_state.signalWithNoise = st.session_state.signalObject.add_noise(st.session_state.siganl,
                                                                                       noiseSNR)
            st.session_state.graphWidget.draw_signal_with_noise()

        # add signals
        with st.container():
            st.write("---")
            st.write("Add Signals")
            selectedSignals = []
            for signal in st.session_state.signals:
                checkboxVal = st.checkbox(signal['name'], key=signal['name'])
                if checkboxVal:
                    selectedSignals.append(signal['name'])
        addSingalBtn = st.button("Add")
        if addSingalBtn:
            print(selectedSignals)
