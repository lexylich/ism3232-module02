import os

records = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Equipment",
        "amount": 1250.00,
        "status": "Pending",
    },
    {
        "id": 2,
        "name": "Pens",
        "category": "Supplies",
        "amount": 45.00,
        "status": "Approved",
    },
    {
        "id": 3,
        "name": "Monitor",
        "category": "Equipment",
        "amount": 2400.00,
        "status": "Pending",
    },
    {
        "id": 4,
        "name": "Chairs",
        "category": "Furniture",
        "amount": 800.00,
        "status": "Pending",
    },
    {
        "id": 5,
        "name": "Server",
        "category": "IT",
        "amount": 5200.00,
        "status": "Approved",
    },
]

LIMIT = 1000
HIGH = 2000

total = 0.0
flagged = []
high_value = []

for r in records:
    if r["status"] == "Pending":
        print(r["name"], r["amount"])
        total += r["amount"]
        if r["amount"] > LIMIT:
            flagged.append(r)
        if r["amount"] > HIGH:
            high_value.append(r)

summary = (
    f"Pending total: ${total:,.2f}\n"
    f"Flagged: {len(flagged)}\n"
    f"High value: {len(high_value)}\n"
)
print(summary)

os.makedirs("data", exist_ok=True)
with open("data/week6_summary.txt", "w") as f:
    f.write(summary)
