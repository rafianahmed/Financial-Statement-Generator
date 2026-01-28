def generate_balance_sheet(inputs, cash, retained_earnings):
    fixed_assets = inputs["capex"]
    debt = inputs["debt_issued"]

    assets = {
        "Cash": cash,
        "Fixed Assets": fixed_assets,
        "Total Assets": cash + fixed_assets
    }

    liabilities_equity = {
        "Debt": debt,
        "Retained Earnings": retained_earnings,
        "Total Liabilities & Equity": debt + retained_earnings
    }

    return assets, liabilities_equity
