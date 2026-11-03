import json
import random
from datetime import datetime, timedelta
from pathlib import Path

NUM_ORDERS = 100_000
random.seed(42)

CATEGORIES = [
    "Electronics",
    "Clothing",
    "Home",
    "Beauty",
    "Sports"
]

COUNTRIES = [
    "Ukraine",
    "Poland",
    "Germany",
    "USA",
    "France"
]

STATUSES = [
    "completed",
    "pending",
    "cancelled",
    "shipped"
]

PAYMENT_METHODS = [
    "card",
    "cash",
    "paypal"
]


def generate_order(order_id):

    order_date = datetime(2025, 1, 1) + timedelta(
        days=random.randint(0, 600)
    )

    quantity = random.randint(1, 10)
    unit_price = round(random.uniform(10, 1000), 2)

    order = {
        "order_id": order_id,
        "customer_id": random.randint(1, 10000),
        "product_id": random.randint(1, 1000),
        "category": random.choice(CATEGORIES),
        "order_date": order_date.strftime("%Y-%m-%d"),
        "quantity": quantity,
        "unit_price": str(unit_price),
        "total_amount": str(round(quantity * unit_price, 2)),
        "status": random.choice(STATUSES),
        "country": random.choice(COUNTRIES),
        "payment_method": random.choice(PAYMENT_METHODS)
    }

    return order


def introduce_errors(order):

    if random.random() < 0.03:
        order["customer_id"] = None

    if random.random() < 0.03:
        order["quantity"] = "three"

    if random.random() < 0.02:
        order["quantity"] = -5

    if random.random() < 0.03:
        order["unit_price"] = "-100"

    if random.random() < 0.03:
        order["order_date"] = "2026-15-45"

    if random.random() < 0.03:
        order["order_date"] = "15/05/2026"

    if random.random() < 0.03:
        order["status"] = "done"

    if random.random() < 0.03:
        order["country"] = " UKRAINE "

    if random.random() < 0.02:
        order["category"] = "Unknown"

    if random.random() < 0.03:
        order["total_amount"] = "999999"

    return order


def generate_dataset():

    orders = []

    for order_id in range(1, NUM_ORDERS + 1):

        order = generate_order(order_id)

        order = introduce_errors(order)

        orders.append(order)

        # Introduce duplicate records
        if random.random() < 0.02:
            orders.append(order.copy())

    output_path = (
        Path(__file__).resolve().parent.parent
        / "data"
        / "raw"
        / "orders.json"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            orders,
            file,
            indent=2,
            ensure_ascii=False
        )

    print(f"Generated {len(orders)} orders")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    generate_dataset()