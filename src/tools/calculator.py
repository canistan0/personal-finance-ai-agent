def sum_amounts(items):
    return sum(item["amount"] for item in items)

def percentage(value, percent):
    return (value * percent) / 100