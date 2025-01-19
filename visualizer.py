"""
Module for creating visualizations of DSCOVR data
"""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from typing import List

class DSCOVRVisualizer:
    def create_mag_plot(self, df: pd.DataFrame) -> go.Figure:
        """Create magnetometer data plot"""
        fig = go.Figure()
        
        components = ['Bx', 'By', 'Bz', 'Bt']
        colors = ['blue', 'red', 'green', 'purple']
        
        for component, color in zip(components, colors):
            fig.add_trace(
                go.Scatter(
                    x=df['timestamp'],
                    y=df[component],
                    name=component,
                    line=dict(color=color)
                )
            )
        
        fig.update_layout(
            title="Magnetic Field Components",
            xaxis_title="Time (UTC)",
            yaxis_title="Magnetic Field (nT)",
            hovermode='x unified'
        )
        return fig

    def create_plasma_plot(self, df: pd.DataFrame) -> go.Figure:
        """Create solar wind plasma plot"""
        fig = go.Figure()
        
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['density'],
                name='Proton Density',
                yaxis='y1'
            )
        )
        
        fig.add_trace(
            go.Scatter(
                x=df['timestamp'],
                y=df['speed'],
                name='Solar Wind Speed',
                yaxis='y2'
            )
        )
        
        fig.update_layout(
            title="Solar Wind Parameters",
            xaxis_title="Time (UTC)",
            yaxis_title="Density (n/cc)",
            yaxis2=dict(
                title="Speed (km/s)",
                overlaying='y',
                side='right'
            ),
            hovermode='x unified'
        )
        return fig

    def create_statistics_table(self, df: pd.DataFrame, parameters: List[str]) -> go.Figure:
        """Create statistical summary table"""
        stats = df[parameters].describe()
        
        fig = go.Figure(data=[go.Table(
            header=dict(
                values=['Statistic'] + parameters,
                fill_color='paleturquoise',
                align='left'
            ),
            cells=dict(
                values=[stats.index] + [stats[param] for param in parameters],
                fill_color='lavender',
                align='left'
            )
        )])
        
        fig.update_layout(
            title="Statistical Summary",
            margin=dict(l=0, r=0, t=30, b=0)
        )
        return fig
