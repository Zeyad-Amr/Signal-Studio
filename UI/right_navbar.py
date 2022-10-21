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

        with st.form("sampling_form"):
            slider_val = st.slider("Sampling")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Reconstruct")
            if submitted:
                st.success("Reconstructed Successfully")

        # file upload
        uploadSignal = st.file_uploader("Upload Signal", type=["csv"], accept_multiple_files=True)
        if uploadSignal:
            # TODO: Browse signal function
            print("Browse signal function")

        with st.form("generate_signal"):
            st.write("Generate Signal")
            signalTitle = st.text_input("Signal Title", )
            freqVal = st.slider("Frequency")
            ampVal = st.slider("Amplitude")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Generate")
            if submitted:
                # TODO: Generate signal function

                st.success("Generated Successfully")

