import streamlit as st


class leftNavBar:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()
        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["Upload", "Generate"])

        with tab1:
            # signal file upload
            uploadSignal = st.file_uploader("Upload Signal", type=["csv"])
            if uploadSignal:
                # TODO: Browse signal function
                print("Browse signal function: ", uploadSignal)

        with tab2:
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

        st.radio("Signals", ("Signal 1", "Signal 2", "Signal 3", "Signal 4", "Signal 5", "Signal 6"))
        # st.radio("Noises", ("Noise 1","Noise 2", "Noise 3","Noise 4","Noise 5","Noise 6"))
