import streamlit as st
import plotly.graph_objects as go


class signalGraph:
    def __init__(self):
        self.fig = go.Figure()
        self.fig.update_layout(xaxis_title="time", yaxis_title="Amplitude")
        self.fig.update_xaxes(showgrid=False, automargin=True)
        self.fig.update_yaxes(showgrid=False, automargin=True)

        self.fig.update_layout(
            height=450,
            margin={
                'l': 0,
                'r': 0,
                'b': 0,
                't': 0
            }
        )


        if not (st.session_state.currentSignal['signal'].empty):
            self.fig.add_trace(go.Scatter(
                x=st.session_state.currentSignal['signal'].iloc[:, 0],
                y=st.session_state.currentSignal['signal'].iloc[:, 1],
                mode='lines',
                name='lines'))

        st.plotly_chart(self.fig, use_container_width=True)
