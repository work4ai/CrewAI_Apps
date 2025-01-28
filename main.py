import yfinance as yf
import streamlit as st
from crewai import Crew, Agent, Task, Process
from langchain_groq import ChatGroq
from datetime import datetime
import pandas as pd

# Initialize CrewAI with LLama 70B and Groq API KEY
#crew_ai = CrewAI(api_key="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", model="LLama-70B")
crew_ai = ChatGroq(model_name="llama3-70b-8192", groq_api_key=<YOUR-API-KEY>)

# Function to fetch basic stock information
def fetch_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "name": info.get("shortName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "summary": info.get("longBusinessSummary")
    }


# Function to perform fundamental analysis
def fundamental_analysis(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "P/E Ratio": info.get("forwardPE"),
        "EPS": info.get("trailingEps"),
        "Revenue Growth": info.get("revenueGrowth")
    }


# Function to conduct risk assessments
def risk_assessment(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "Volatility": info.get("beta"),
        "Sharpe Ratio": info.get("sharpeRatio")
    }


# Function to perform technical analysis
def technical_analysis(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    sma = hist["Close"].rolling(window=50).mean()
    rsi = compute_rsi(hist["Close"])
    macd = compute_macd(hist["Close"])
    return {
        "SMA": sma,
        "RSI": rsi,
        "MACD": macd
    }


# Helper functions for technical analysis
def compute_rsi(series, period=14):
    delta = series.diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def compute_macd(series, short_period=12, long_period=26, signal_period=9):
    short_ema = series.ewm(span=short_period, adjust=False).mean()
    long_ema = series.ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_period, adjust=False).mean()
    return macd - signal_line


# Function to fetch recent news articles for stocks
def fetch_news(ticker):
    news = yf.Ticker(ticker).news
    return news


# Function to combine all analyses into comprehensive stock reports
def generate_stock_report(ticker):
    stock_info = fetch_stock_info(ticker)
    fundamental_info = fundamental_analysis(ticker)
    risk_info = risk_assessment(ticker)
    technical_info = technical_analysis(ticker)
    news_info = fetch_news(ticker)

    report = {
        "Stock Information": stock_info,
        "Fundamental Analysis": fundamental_info,
        "Risk Assessment": risk_info,
        "Technical Analysis": technical_info,
        "Recent News": news_info
    }

    return report


# Streamlit UI for user input and displaying results
st.title("Comprehensive Stock Analysis Report")
ticker_input = st.text_input("Enter Stock Ticker Symbol:", value="AAPL")

if st.button("Generate Report"):
    report = generate_stock_report(ticker_input)

    st.subheader("Stock Information")
    st.write(report["Stock Information"])

    st.subheader("Fundamental Analysis")
    st.write(report["Fundamental Analysis"])

    st.subheader("Risk Assessment")
    st.write(report["Risk Assessment"])

    st.subheader("Technical Analysis")
    st.write(report["Technical Analysis"])

    st.subheader("Recent News")
    for article in report["Recent News"]:
        st.write(
            f"{article['title']} - {article['publisher']} ({datetime.fromtimestamp(article['providerPublishTime'])})")
