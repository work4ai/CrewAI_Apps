import yfinance as yf
import streamlit as st
from crewai import Crew, Agent, Task, Process
from datetime import datetime
import pandas as pd
from langchain_groq import ChatGroq

# Initialize GROQ LLM
GROQ_API_KEY = "<GROQ_API_KEY>"  #Your API KEY

llm = ChatGroq(
    model_name="llama3-70b-8192",
    groq_api_key=GROQ_API_KEY,
    verbose=True
)

# Functions for stock analysis
def fetch_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "name": info.get("shortName"),
        "sector": info.get("sector"),
        "market_cap": info.get("marketCap"),
        "summary": info.get("longBusinessSummary")
    }

def fundamental_analysis(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "P/E Ratio": info.get("forwardPE"),
        "EPS": info.get("trailingEps"),
        "Revenue Growth": info.get("revenueGrowth")
    }

def risk_assessment(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "Volatility": info.get("beta"),
        "Sharpe Ratio": info.get("sharpeRatio")
    }

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

def technical_analysis(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    sma = hist["Close"].rolling(window=50).mean()
    rsi = compute_rsi(hist["Close"])
    macd = compute_macd(hist["Close"])
    return {
        "SMA": sma.iloc[-1],  # Latest SMA value
        "RSI": rsi.iloc[-1],  # Latest RSI value
        "MACD": macd.iloc[-1]  # Latest MACD value
    }

def fetch_news(ticker):
    news = yf.Ticker(ticker).news
    news_info = []
    for item in news:
        news_item = {
            "title": item.get("title", "No title available"),  # Default to "No title available" if title is missing
            "publisher": item.get("publisher", "No publisher available"),  # Default to "No publisher available" if publisher is missing
            "time": datetime.fromtimestamp(item.get("providerPublishTime", 0))  # Default to 0 timestamp if missing
        }
        news_info.append(news_item)
    return news_info

# Define Task for stock analysis
stock_analysis_task = Task(
    description="Perform fundamental, technical, and risk analysis on a given stock ticker.",
    expected_output="Detailed stock report including fundamental analysis, risk assessment, technical indicators, and recent news."
)

# Define Agent to handle the task
stock_analysis_agent = Agent(
    role="Stock Analysis Agent",
    tasks=[stock_analysis_task],
    llm=llm,  # Using GROQ LLM
    goal="Analyze stocks and generate comprehensive reports.",
    backstory=(
        "The agent specializes in analyzing financial and technical data for stocks. "
        "It gathers and processes relevant data to create a detailed report."
    ),
    verbose=True
)

'''
# Define Process to execute the task
stock_analysis_process = Process(
    agents=[stock_analysis_agent]
)
'''
# Streamlit UI
st.title("Comprehensive Stock Analysis with GROQ LLM and CrewAI")
ticker_input = st.text_input("Enter Stock Ticker Symbol:", value="AAPL")

if st.button("Generate Report"):
    # Gather data for stock report
    stock_info = fetch_stock_info(ticker_input)
    fundamental_info = fundamental_analysis(ticker_input)
    risk_info = risk_assessment(ticker_input)
    technical_info = technical_analysis(ticker_input)
    news_info = fetch_news(ticker_input)

    # Combine into a report
    report = {
        "Stock Information": stock_info,
        "Fundamental Analysis": fundamental_info,
        "Risk Assessment": risk_info,
        "Technical Analysis": technical_info,
        "Recent News": news_info
    }

    # Display the results
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
        st.write(f"{article['title']} - {article['publisher']} ({article['time']})")
