def generate_income_statement(inputs):
    revenue = inputs["revenue"]
    cogs = inputs["cogs"]
    opex = inputs["opex"]
    tax_rate = inputs["tax_rate"]

    gross_profit = revenue - cogs
    ebit = gross_profit - opex
    tax = ebit * tax_rate
    net_income = ebit - tax

    return {
        "Revenue": revenue,
        "COGS": -cogs,
        "Gross Profit": gross_profit,
        "Operating Expenses": -opex,
        "EBIT": ebit,
        "Tax": -tax,
        "Net Income": net_income
    }
