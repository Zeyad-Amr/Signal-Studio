import streamlit as st
import plotly.graph_objects as go


class signalGraph:
    def __init__(self):

        self.fig = go.Figure()
        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)
        if 'figureSpot' not in st.session_state:
            self.figureSpot = st.plotly_chart(
                self.fig, use_container_width=True)
            st.session_state.figureSpot = self.figureSpot
