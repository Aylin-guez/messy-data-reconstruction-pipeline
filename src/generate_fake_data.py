from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

# --------------------------
# Configuración
# --------------------------

NUM_CUSTOMERS = 50

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data"
)

os.makedirs(DATA_PATH, exist_ok=True)

# --------------------------
# Clientes base
# --------------------------

customers = []

for customer_id in range(1, NUM_CUSTOMERS + 1):

    name = fake.name()

    customers.append({
        "customer_id": customer_id,
        "customer_name": name,
        "email": fake.email(),
        "phone": fake.phone_number()
    })

customers_df = pd.DataFrame(customers)

# --------------------------
# Customers.xlsx
# --------------------------

customers_df.drop(columns=["customer_id"]).to_excel(
    os.path.join(DATA_PATH, "customers.xlsx"),
    index=False
)

# --------------------------
# Función para romper nombres
# --------------------------

def messy_name(name):

    options = [
        name,
        name.upper(),
        name.lower(),
        name.replace(" ", ", "),
        f"{name.split()[0]} {name.split()[-1][0]}.",
        f"{name.split()[0][0]}. {name.split()[-1]}"
    ]

    return random.choice(options)

# --------------------------
# Sales.csv
# --------------------------

sales = []

for _ in range(300):

    customer = random.choice(customers)

    sales.append({
        "customer_name": messy_name(customer["customer_name"]),
        "order_id": fake.uuid4(),
        "amount": round(random.uniform(50, 5000), 2)
    })

sales_df = pd.DataFrame(sales)

sales_df.to_csv(
    os.path.join(DATA_PATH, "sales.csv"),
    index=False
)

# --------------------------
# Support Tickets.csv
# --------------------------

tickets = []

for _ in range(200):

    customer = random.choice(customers)

    tickets.append({
        "client": messy_name(customer["customer_name"]),
        "ticket_id": fake.uuid4(),
        "priority": random.choice(
            ["Low", "Medium", "High"]
        )
    })

tickets_df = pd.DataFrame(tickets)

tickets_df.to_csv(
    os.path.join(DATA_PATH, "support_tickets.csv"),
    index=False
)

print("✅ Fake datasets generated")
print("📁 customers.xlsx")
print("📁 sales.csv")
print("📁 support_tickets.csv")