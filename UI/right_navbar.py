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

        # sampling
        with st.form("sampling_form"):
            slider_val = st.slider("Sampling")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Reconstruct")
            if submitted:
                st.success("Reconstructed Successfully")

        # signal file upload
        uploadSignal = st.file_uploader("Upload Signal", type=["csv"])
        if uploadSignal:
            # TODO: Browse signal function
            print("Browse signal function: ", uploadSignal)

        # generate signal
        with st.form("generate_signal"):
            st.write("Generate Signal")
            signalTitle = st.text_input("Signal Title")

            freqVal = st.number_input("Frequency")
            ampVal = st.number_input("Amplitude")
            phaseVal = st.number_input("Phase")

            submitted = st.form_submit_button("Generate")
            if submitted:
                # TODO: Generate signal function
                print(signalTitle, ", ", freqVal, ", ", ampVal, ", ", phaseVal)
                st.success("Generated Successfully")
        with st.container():
            # add noise
            st.write("Add Noise")
            noiseSNR = st.slider("SNR")
            if noiseSNR:
                # TODO: SNR change function
                    print("SNR change function: ", noiseSNR)
