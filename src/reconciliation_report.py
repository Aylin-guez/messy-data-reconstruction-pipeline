import pandas as pd
import os

BASE_PATH = os.path.join(
    os.path.dirname(__file__),
    ".."
)

OUTPUT_PATH = os.path.join(BASE_PATH, "output")

customers = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_customers.xlsx")
)

sales = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_sales.xlsx")
)

tickets = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_support_tickets.xlsx")
)

master = pd.read_excel(
    os.path.join(OUTPUT_PATH, "reconstructed_master_table.xlsx")
)

# --------------------------
# Metrics
# --------------------------

total_customers = len(customers)
total_sales = len(sales)
total_tickets = len(tickets)

matched_sales = master["number_of_orders"].gt(0).sum()
matched_tickets = master["number_of_tickets"].gt(0).sum()

sales_match_rate = round(
    matched_sales / total_customers * 100,
    2
)

ticket_match_rate = round(
    matched_tickets / total_customers * 100,
    2
)

report = pd.DataFrame(
    {
        "Metric": [
            "Customers",
            "Sales Records",
            "Support Tickets",
            "Matched Customers (Sales)",
            "Matched Customers (Tickets)",
            "Sales Match Rate %",
            "Ticket Match Rate %"
        ],
        "Value": [
            total_customers,
            total_sales,
            total_tickets,
            matched_sales,
            matched_tickets,
            sales_match_rate,
            ticket_match_rate
        ]
    }
)

report.to_excel(
    os.path.join(
        OUTPUT_PATH,
        "reconciliation_report.xlsx"
    ),
    index=False
)

print(report)
print()
print("✅ reconciliation_report.xlsx created")