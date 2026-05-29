import pandas as pd
import re
import os

BASE_PATH = os.path.join(
    os.path.dirname(__file__),
    ".."
)

DATA_PATH = os.path.join(BASE_PATH, "data")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

os.makedirs(OUTPUT_PATH, exist_ok=True)


def normalize_name(name):
    if pd.isna(name):
        return ""

    name = str(name).lower().strip()

    # Remove punctuation
    name = re.sub(r"[^\w\s]", "", name)

    # Replace multiple spaces
    name = re.sub(r"\s+", " ", name)

    return name


# --------------------------
# Load files
# --------------------------

customers = pd.read_excel(
    os.path.join(DATA_PATH, "customers.xlsx")
)

sales = pd.read_csv(
    os.path.join(DATA_PATH, "sales.csv")
)

tickets = pd.read_csv(
    os.path.join(DATA_PATH, "support_tickets.csv")
)


# --------------------------
# Normalize names
# --------------------------

customers["normalized_name"] = customers["customer_name"].apply(normalize_name)
sales["normalized_name"] = sales["customer_name"].apply(normalize_name)
tickets["normalized_name"] = tickets["client"].apply(normalize_name)


# --------------------------
# Export cleaned versions
# --------------------------

customers.to_excel(
    os.path.join(OUTPUT_PATH, "cleaned_customers.xlsx"),
    index=False
)

sales.to_excel(
    os.path.join(OUTPUT_PATH, "cleaned_sales.xlsx"),
    index=False
)

tickets.to_excel(
    os.path.join(OUTPUT_PATH, "cleaned_support_tickets.xlsx"),
    index=False
)


print("✅ Cleaned files created successfully")
print("📁 cleaned_customers.xlsx")
print("📁 cleaned_sales.xlsx")
print("📁 cleaned_support_tickets.xlsx")