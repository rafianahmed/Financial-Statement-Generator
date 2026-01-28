import streamlit as st
import pandas as pd

from accounting.income_statement import generate_income_statement
from accounting.cash_flow import generate_cash_flow
from accounting.balance_sheet import generate_balance_sheet
from accounting.validator import validate_balance_sheet

st.set_page_config(page_title="Financial Statement Generator", layout="wide")

st.title("📊 Financial Statement Generator")

st.sidebar.header("Input Financial Data")

inputs = {
    "revenue": st.sidebar.number_input("Revenue", 0.0, step=1000.0),
    "cogs": st.sidebar.number_input("COGS", 0.0, step=1000.0),
    "opex": st.sidebar.number_input("Operating Expenses", 0.0, step=1000.0),
    "tax_rate": st.sidebar.slider("Tax Rate", 0.0, 0.5, 0.25),
    "capex": st.sidebar.number_input("Capital Expenditure", 0.0, step=1000.0),
    "debt_issued": st.sidebar.number_input("Debt Issued", 0.0, step=1000.0),
}

income = generate_income_statement(inputs)
net_income = income["Net Income"]

cash_flow = generate_cash_flow(inputs, net_income)
cash = cash_flow["Net Change in Cash"]

assets, liabilities_equity = generate_balance_sheet(
    inputs, cash, retained_earnings=net_income
)

st.header("Income Statement")
st.table(pd.DataFrame.from_dict(income, orient="index", columns=["Amount"]))

st.header("Cash Flow Statement")
st.table(pd.DataFrame.from_dict(cash_flow, orient="index", columns=["Amount"]))

st.header("Balance Sheet")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Assets")
    st.table(pd.DataFrame.from_dict(assets, orient="index", columns=["Amount"]))

with col2:
    st.subheader("Liabilities & Equity")
    st.table(pd.DataFrame.from_dict(liabilities_equity, orient="index", columns=["Amount"]))

if validate_balance_sheet(assets, liabilities_equity):
    st.success("✅ Balance Sheet Balances")
else:
    st.error("❌ Balance Sheet Does NOT Balance")
