def generate_cash_flow(inputs, net_income):
    capex = inputs["capex"]
    debt_issued = inputs["debt_issued"]

    operating_cf = net_income
    investing_cf = -capex
    financing_cf = debt_issued

    net_cash = operating_cf + investing_cf + financing_cf

    return {
        "Operating Cash Flow": operating_cf,
        "Investing Cash Flow": investing_cf,
        "Financing Cash Flow": financing_cf,
        "Net Change in Cash": net_cash
    }
