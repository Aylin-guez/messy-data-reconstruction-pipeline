import pandas as pd
import os

BASE_PATH = os.path.join(
    os.path.dirname(__file__),
    ".."
)

DATA_PATH = os.path.join(BASE_PATH, "data")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

os.makedirs(OUTPUT_PATH, exist_ok=True)

customers = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_customers.xlsx")
)

sales = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_sales.xlsx")
)

tickets = pd.read_excel(
    os.path.join(OUTPUT_PATH, "cleaned_support_tickets.xlsx")
)

# --------------------------
# Sales summary
# --------------------------

sales_summary = sales.groupby(
    "normalized_name",
    as_index=False
).agg(
    total_sales=("amount", "sum"),
    number_of_orders=("order_id", "count")
)

# --------------------------
# Tickets summary
# --------------------------

tickets_summary = tickets.groupby(
    "normalized_name",
    as_index=False
).agg(
    number_of_tickets=("ticket_id", "count"),
    high_priority_tickets=(
        "priority",
        lambda x: (x == "High").sum()
    )
)

# --------------------------
# Merge everything
# --------------------------

master = customers.merge(
    sales_summary,
    on="normalized_name",
    how="left"
).merge(
    tickets_summary,
    on="normalized_name",
    how="left"
)

master["total_sales"] = master["total_sales"].fillna(0)
master["number_of_orders"] = master["number_of_orders"].fillna(0).astype(int)
master["number_of_tickets"] = master["number_of_tickets"].fillna(0).astype(int)
master["high_priority_tickets"] = master["high_priority_tickets"].fillna(0).astype(int)

master.to_excel(
    os.path.join(OUTPUT_PATH, "reconstructed_master_table.xlsx"),
    index=False
)

print("✅ Reconstructed master table created")
print("📁 reconstructed_master_table.xlsx")