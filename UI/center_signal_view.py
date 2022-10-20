import streamlit as st
from matplotlib import pyplot as plt
import numpy as np


class centerSignalView:
    def __init__(self):
        with open("./styles/style.css") as source:
            style = source.read()

        st.markdown(f"""
        <style>
        {style}
        </style>
        """, unsafe_allow_html=True)

        fig = plt.figure()
        plt.style.use(
            "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
        x = np.linspace(0, 10, 50)

        plt.plot(x, np.sin(x), color="#5891C7")
        plt.scatter(x, np.sin(x), color="#ED0000")
        st.write(fig)
