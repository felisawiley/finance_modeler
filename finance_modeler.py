#api_key = ""
 
import os
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import numpy as np
import plotly.graph_objects as go

API_KEY = ""

def get_stock_data(stock_symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, _ = ts.get_daily_adjusted(stock_symbol, outputsize='compact')
    return data['5. adjusted close'].iloc[-1]

def plot_investment_growth(stock_symbol, share_fraction):
    stock_price = get_stock_data(stock_symbol)
    investment_full_share = stock_price
    investment_fractional_share = stock_price * share_fraction

    years = np.arange(0, 11)
    annual_rate_of_return = 1.06

    full_share_value = investment_full_share * (annual_rate_of_return ** years)
    fractional_share_value = investment_fractional_share * (annual_rate_of_return ** years)

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=years, y=full_share_value, mode='lines+markers', name='Full Share'))
    fig.add_trace(go.Scatter(x=years, y=fractional_share_value, mode='lines+markers', name=f'Fractional Share ({share_fraction})'))

    fig.update_layout(
        title=f"Investment Growth Over 10 Years: {stock_symbol}",
        xaxis_title="Years",
        yaxis_title="Investment Value ($)",
        hovermode="x unified",
        legend_title="Investment Type"
    )

    fig.show()

stock_symbol = input("Enter the stock symbol: ").upper()
share_fraction = float(input("Enter the fraction of share you want to buy (0 to 1): "))

plot_investment_growth(stock_symbol, share_fraction)
