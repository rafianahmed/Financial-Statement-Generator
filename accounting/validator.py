def validate_balance_sheet(assets, liabilities_equity):
    return abs(
        assets["Total Assets"] - liabilities_equity["Total Liabilities & Equity"]
    ) < 1e-6
